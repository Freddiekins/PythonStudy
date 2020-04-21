# 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
# 将当前img目录所有以.png结尾的后缀名改为.jpg.
import os

path = os.getcwd()
os.chdir(path + "/homework3/img")
files = os.listdir()
for f in files:
    a = os.path.splitext(f)
    if a[1] == '.png':
        newname = a[0] + '.jpg'
        os.rename(f, newname)
