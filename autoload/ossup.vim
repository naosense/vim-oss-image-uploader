if !has("python") && !has("python3")
    echoerr "Vim has to be compiled with +python or +python3 to run this"
    finish
endif

if exists("g:oss_image_uploader_loaded")
    finish
endif

if !exists("g:oss_image_uploader_type")
    echoerr "Not set g:oss_image_uploader_type"
    finish
endif

if g:oss_image_uploader_type ==# "ali"
    if !exists("g:ali_image_uploader_access_key")
        echoerr "Not set g:ali_image_uploader_access_key"
        finish
    endif

    if !exists("g:ali_image_uploader_secret_key")
        echoerr "Not set g:ali_image_uploader_secret_key"
        finish
    endif

    if !exists("g:ali_image_uploader_end_point")
        echoerr "Not set g:ali_image_uploader_end_point"
        finish
    endif

    if !exists("g:ali_image_uploader_bucket_name")
        echoerr "Not set g:ali_image_uploader_bucket_name"
        finish
    endif

    if !exists("g:ali_image_uploader_bucket_domain")
        echoerr "Not set g:ali_image_uploader_bucket_domain"
        finish
    endif
elseif g:oss_image_uploader_type ==# "qiniu"
    if !exists("g:qiniu_image_uploader_access_key")
        echoerr "Not set g:qiniu_image_uploader_access_key"
        finish
    endif

    if !exists("g:qiniu_image_uploader_secret_key")
        echoerr "Not set g:qiniu_image_uploader_secret_key"
        finish
    endif

    if !exists("g:qiniu_image_uploader_bucket_name")
        echoerr "Not set g:qiniu_image_uploader_bucket_name"
        finish
    endif

    if !exists("g:qiniu_image_uploader_bucket_domain")
        echoerr "Not set g:qiniu_image_uploader_bucket_domain"
        finish
    endif
elseif g:oss_image_uploader_type ==# "net"
    if !exists("g:net_image_uploader_access_key")
        echoerr "Not set g:net_image_uploader_access_key"
        finish
    endif

    if !exists("g:net_image_uploader_secret_key")
        echoerr "Not set g:net_image_uploader_secret_key"
        finish
    endif

    if !exists("g:net_image_uploader_end_point")
        echoerr "Not set g:net_image_uploader_end_point"
        finish
    endif

    if !exists("g:net_image_uploader_bucket_name")
        echoerr "Not set g:net_image_uploader_bucket_name"
        finish
    endif

    if !exists("g:net_image_uploader_bucket_domain")
        echoerr "Not set g:net_image_uploader_bucket_domain"
        finish
    endif
else
    echoerr "g:oss_image_uploader_type can only be 'ali', 'qiniu' or 'net'"
    finish
endif

let g:oss_image_uploader_loaded = 1

let s:plugin_root_dir = fnamemodify(resolve(expand("<sfile>:p")), ":h")

python << EOF
import sys
import vim
from os.path import normpath, join
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, 'python'))
sys.path.insert(0, python_root_dir)
import main
EOF

function! ossup#upload()
python <<EOF
main.upload_all()
EOF
endfunction
