# -*- coding: utf-8 -*-

import os
import re
import vim
import utils


IMAGE_PATTERN = re.compile(r'!\[.*\]\((.*)\)')

oss_type = vim.eval('g:oss_image_uploader_type')

is_ali = (oss_type == 'ali')
is_qiniu = (oss_type == 'qiniu')

access_key = None
secret_key = None
end_point = None
bucket_name = None
bucket_domain = None

if is_ali:
    import ali_uploader
    access_key = vim.eval('g:ali_image_uploader_access_key')
    secret_key = vim.eval('g:ali_image_uploader_secret_key')
    end_point = vim.eval('g:ali_image_uploader_end_point')
    bucket_name = vim.eval('g:ali_image_uploader_bucket_name')
    bucket_domain = vim.eval('g:ali_image_uploader_bucket_domain')
elif is_qiniu:
    import qiniu_uploader
    access_key = vim.eval('g:qiniu_image_uploader_access_key')
    secret_key = vim.eval('g:qiniu_image_uploader_secret_key')
    bucket_name = vim.eval('g:qiniu_image_uploader_bucket_name')
    bucket_domain = vim.eval('g:qiniu_image_uploader_bucket_domain')

image_cnt = 0


def upload_all():
    global image_cnt
    image_cnt = 0
    current_buffer = vim.current.buffer
    end_line = int(vim.eval('line("$")'))
    for l in seq(1, end_line + 1):
        upload_line(l, current_buffer)

    if image_cnt > 0:
        vim.command('redraw | echom "Done! Upload %d images"' % image_cnt)
    else:
        vim.command('redraw | echom "No local image"')


def upload_line(n, current_buffer):
    file_name, extension = os.path.splitext(vim.eval('expand("%")'))
    line_str = current_buffer[n - 1]
    it = re.finditer(IMAGE_PATTERN, line_str)
    for match in it:
        image_src = match.group(1)
        if not image_src.startswith('http'):
            key = None
            if is_ali:
                key = ali_uploader.upload(access_key, secret_key, end_point, bucket_name, file_name, image_src)
            elif is_qiniu:
                key = qiniu_uploader.upload(access_key, secret_key, bucket_name, file_name, image_src)

            current_buffer[n - 1] = line_str.replace(image_src, bucket_domain + '/' + key)
            global image_cnt
            image_cnt += 1
            # 使用单引号，确保不会对\进行转义
            vim.command('redraw | echom \'Upload %s success\'' % image_src)


def seq(start, end):
    if utils.is_py2:
        return xrange(start, end)
    elif utils.is_py3:
        return range(start, end)
