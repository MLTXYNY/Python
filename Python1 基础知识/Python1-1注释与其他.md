# Python1-1注释与其他

## 1Python注释

#### 1.1 四基础注释方法

1.第一种方法

```python
# 注释内容
```

2.第二种方法

```python
'''
注释内容
'''
```

3.第三种方法

```python
"""
注释内容
"""
```

4.第四种方法

```python
#输出格式
def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)
#输出格式
'''
这是文档字符串
'''
```

注意：注释应该放在函数的第一行 


注意：下面的可以先不看，了解就行。

## 2 其他一

#### 2.1 一行多个语句

```python
#举例格式
print("狗叫什么");print("没用的")   #使用；分隔开。

#输出格式
'''
狗叫什么
没用的
'''
```

#### 2.2一个语句分成多行

```python
#注释与其他2.2
a = b = c = 10
x = a + b + c + 12
print(x)     #输出x
#方法一（使用“/”）
y = a +\    #
    b +\
    c +\
    12
print(y)
#方法二（使用括号）
z = (a +    #此处可以加上批注
     b +
     c +
     12)
print(z)

#输出格式（输出相同）
'''
42
42
'''
```

## 3 其他二

#### 3.1 查看python版本与程序位置

```python
import sys
print(sys.version)
sys.executable
```

#### 3.2 查看安装的包

```python
pip list
```

#### 3.3 环境变量使用不了需要更新pip

```python
# pip更新代码
python -m pip install --upgrade pip
#拓展：
#在某一代码条件下需要更改TempFiles的环境变量在C盘以外，或者全英文路径下，推荐就D或其他盘的主目录创建TempFiles文件夹即可。
```

#### 3.4 Python笔记本

```python
#1.Jupyter实验室安装
pip install jupyterlab
#命令启动 JupyterLab：
jupyter-lab
#2.Jupyter 笔记本安装
pip install notebook
#要运行笔记本：
jupyter notebook
#3.安装Voilà：
pip install voila
```
