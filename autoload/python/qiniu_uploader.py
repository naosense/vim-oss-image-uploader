# -*- coding: utf-8 -*-

from qiniu import Auth, put_file
from qiniu.compat import is_py2, is_py3


def upload(access_key, secret_key, bucket_name, prefix, image_path):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 上传到七牛后保存的文件名
    index = image_path.rfind('/')
    if index == -1:
        index = image_path.rfind('\\')

    key = prefix + '/' + image_path[index + 1:]

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, image_path)
    # print(ret)
    # print(info)

    if is_py2:
        assert ret['key'].encode('utf-8') == key
    elif is_py3:
        assert ret['key'] == key

    return key

