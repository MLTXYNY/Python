# Python1-3输出与输入

## 1 输出

#### 1.1 print输出1

Print是python里很基本很常见的一个操作，它的操作对象是一个字符串。

```python
#基本格式
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=Flalse)
```

| 参数    |                                             |                                             |
| ------- | ------------------------------------------- | ------------------------------------------- |
| objects | 表示可以一次输出多个表达式。                | 输出多个表达式时，需要用 , 分隔。           |
| sep     | 多个表达式之间间隔符                        | 默认值是一个空格。                          |
| end     | 用来设定以什么结尾                          | 默认值是换行符 \n，我们可以换成其他字符串。 |
| file    | 默认值是换行符 \n，我们可以换成其他字符串。 | 默认sys.stdout：表示屏幕输出                |
| flush   | 是否清除数据流的缓冲区                      | 预设是不清除                                |

```python
#举例
print("hello world")
new=open("talk.text","w")    #以写方式新建打开new.text文件
print("hello","bye",sep="*",file=new)  #将输出结果hello*bye保存到new指向talk.text文件
```

#### 1.2 print输出2

```python
#基本格式
print("%格式符1%格式符2……"%(表达式1，表达式2))
```

|   参数   |                       |
| :------: | --------------------- |
| %格式符1 | 指定表达式1的输出格式 |
|    %d    | 十进制整数            |
|    %s    | 字符串                |
|    %f    | 浮点数                |
|    %o    | 八进制                |
|    %x    | 十六进制              |

```python
#举例格式
a=b=3.2
print("%4.2f+%4.2f=%6.2f" %(a,b,a+b))  # 6.2f表示宽度为6，小数2位的浮点数
#输出格式
'''
3.20+3.20=  6.40
'''
```

#### 1.3 print输出3

```python
#基本格式
print(f"{}")
```

```python
#举例
a=1
b=2
S=a+b
P=a*b
print(f"Sum of a and b is {S}, and product is {P}")
#输出格式
"""
Sum of a and b is 3, and product is 2
"""
```

给变量设定输出格式，如输出为3.000000,在变量的后面加上:nf就是{S:f}

## 2.输入

#### 2.1 input()输入

Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。

```python
#基本格式
input("提示信息")
```

```python
#举例
a = input("请输入一个数")
print(a)  
#输出格式
'''
（a是输入多少输出多少）
'''
```

**功能**：显示提示信息，用户输入数据做为返回值

**返回值**：输入的数据

#### 2.2 input()输入拓展

```python
#基本案例
c =1
a,b=map(int,input("请输入两个整数(逗号分隔):").split(','))
print(a,b,c,sep="se")
#基本输出
'''
请输入两个整数(逗号分隔):45,7
45se7se1
'''
```

#### 2.3 eval()输入

```python
#基本格式
变量 = eval("表达式")     #返回表达式结果
```

```python
#基本a
#eval()结合input()使用 获取用户输入的数字
a = eval(input("请输入一个数:"))
print(a*2)
```



