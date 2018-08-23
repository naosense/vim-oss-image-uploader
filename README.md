## Vim Markdown 图片上传插件（已支持阿里云、七牛）

主要是为了写markdown时方便图片的上传，不必打开浏览器，执行一系列重复动作：上传图片-复制外链-替换文件中图片url等，现在一条命令就可完成上述工作，省下的时间喝杯茶吧！

### 安装准备

如果你使用的是阿里云，需要安装阿里云官方的[python-sdk](https://github.com/aliyun/aliyun-oss-python-sdk?spm=a2c4g.11186623.2.4.324a585ehG97Wl)，可以用命令安装：

```
pip install oss2
```

如果你用的是七牛云，请安装七牛官方的[python-sdk](https://github.com/qiniu/python-sdk)，相应命令如下：

```
pip install qiniu
```

当然你也可以下载安装包进行手动安装。

### 安装

如果你使用[pathogen](https://github.com/tpope/vim-pathogen)，可以这样：

```
git clone git@github.com:pingao777/vim-oss-image-uploader.git
```

如果你没有使用任何插件管理工具，将autoload和plugin里的文件拷贝到你Vim的同名文件夹即可。

### 设置

```vim

" =========阿里云配置变量=========
" 设置oss服务类型为阿里
let g:oss_image_uploader_type = "ali"
" 设置你的Access Key
let g:ali_image_uploader_access_key = ""
" 设置你的Secret Key
let g:ali_image_uploader_secret_key = ""
" end point
let g:ali_image_uploader_end_point = ""
" 要上传的存储空间名字
let g:ali_image_uploader_bucket_name = ""
" 存储空间的域名
let g:ali_image_uploader_bucket_domain = ""

" =========七牛云配置变量=========
" 设置oss服务类型为七牛
let g:oss_image_uploader_type = "qiniu"
" 设置你的Access Key，对应控制面板-密钥管理的AK
let g:qiniu_image_uploader_access_key = ""
" 设置你的Secret Key，对应控制面板-密钥管理的SK
let g:qiniu_image_uploader_secret_key = ""
" 要上传的存储空间名字
let g:qiniu_image_uploader_bucket_name = ""
" 存储空间的域名
let g:qiniu_image_uploader_bucket_domain = ""
```

在命令行输入`:OssUploadImg`或绑定一个快捷键：

```vim
autocmd filetype markdown nnoremap <leader>up :OssUploadImg<cr>
```
