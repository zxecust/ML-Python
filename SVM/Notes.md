# 一些问题及其解决方法

[TOC]

## Sublime 配置 Python 环境

### 问题

在使用Sublime配置Python环境中遇到了一些问题，在这里记录。

电脑安装了Anaconda，参考网络上的教程配置了Sublime和Anaconda的环境，但是在使用numpy和matplotlib的过程中总是报错：
```python
import numpy as np
import matplotlib.pyplot as plt
```
报错为：
```
DLL load failed while importing _multiarray_umath: 找不到指定的模块
```

试过了修改numpy和matplotlib版本等方法依然无法解决这个问题，最后选择安装python，重新配置环境。

### Python 环境配置

系统为Windows 11。

#### 安装Python
Python官网上下载的64位安装包，默认安装，此处我选择的是Python3.9。

#### 配置系统变量
打开cmd，输入python，如果未能直接进入python命令行，说明系统环境变量未配置好，可以输入：
```cmd
set PATH=C:\Users\zixuan\AppData\Local\Programs\Python\Python39
```

PATH后面是Python的实际安装路径，默认路径如上。

#### 安装相应的模块

使用 pip 安装相应的模块，如果在命令行直接使用pip报错，可以使用：
```cmd
python -m pip install packagename
```

如果使用默认的pip源，下载会比较慢，可以改用国内的源，比如这里，我使用的是清华的镜像源，使用方法是在pip命令后面直接添加指令：

```cmd
python -m pip install packagename -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 配置Sublime

新建编译系统，在配置文件中输入：
```
{
    "cmd": ["C:/Users/zixuan/AppData/Local/Programs/Python/Python39/python.exe","-u","$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
}
```

其中`"C:/Users/zixuan/AppData/Local/Programs/Python/Python39/python.exe"`是Python的默认安装路径，应该修改为实际安装路径。

保存为“Python39.sublime-build”，并在编译系统中选择新配置的Python39，按下Ctrl+B就可以进行编译。