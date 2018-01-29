
# pip
> 列出已安装的包  pip freeze or pip list
> 导出requirements.txt  pip freeze > <目录>/requirements.txt
> 安装包
在线安装 `pip install <包名> 或 pip install -r requirements.txt`
```
# 安装1.9版本的django
pip install django==1.9
# 安装版本号大于1.9的django，注意有引号
pip install "django>1.9"
pip install "django>=1.9"
```

安装本地安装包
pip install <目录>/<文件名> 或 pip install --use-wheel --no-index --find-links=wheelhouse/ <包名>
<包名>前有空格
可简写为  pip install --no-index -f=<目录>/ <包名>

> 卸载包  pip uninstall <包名> 或 pip uninstall -r requirements.txt
> 升级包  pip install -U <包名>
> 升级pip pip install -U pip
> 显示包所在的目录  pip show -f <包名>
> 搜索包  pip search <搜索关键字>
> 查询可升级的包 pip list -o
> 下载包而不安装  pip install <包名> -d <目录> 或 pip install -d <目录> -r requirements.txt
> 打包  pip wheel <包名>
