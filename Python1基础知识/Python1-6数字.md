# Python1-6数字

## 1 int(整数)

#### 1.1 定义

只有一种整数类型 int，表示为长整型，没有 python2 中的 Long，如 1。

#### 1.2 数值类型转换（数据类型作为函数名）

```python
#基本格式
int(x)
#或
int(x,[base=n]) #将x转换为一个十进制整数。base=n 表示将n进制的字符串转换成十进制整数，省略自动识别
```

###### 举例1

```python
x=0b1010
int(x)    #  输出10
x="0x3F2"
int(x,base=16) #  输出1010
```

## 2 float（浮点型）

#### 2.1 定义

必须带有小数部分，小数部分可以是0，例如1010.0。表示方法有一般表示（只有十进制）和科学计数法。数值范围和小数精度受不同计算机系统的限制，一般认为没有范围限制。有不确定尾数。如 1.23、3E-2。

#### 2.2 数值类型转换（数据类型作为函数名）

```python
#基本格式
float(x)
```

###### 举例1

```python
#举例
float(100)  ##输出100.0
```

## 3 complex（复数）

#### 3.1 定义

c=complex(1,2)，如 1 + 2j、 1.1 + 2.2j。

#### 3.2 数值类型转换（数据类型作为函数名）

```python
#基本格式
complex(x)        #将x转换到一个复数，实数为x，虚数为0。
complex(x, y)     #将x和y转换到一个复数，实数部分为x，虚数部分为y。
```

## 4 Bool（布尔）

#### 4.1 定义

(True等价于1，False等价于0）如 True

## 5 空值：None

#### 5.1 定义

表示该值是一个空对象，空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。可以将None赋值给任何变量，也可以给None值变量赋值。

## 6 两个内置函数

#### 6.1 type函数

```python
#基本格式
type(变量等...)
```

```python
#举例
type(True)
##返回‘bool’
```

#### 6.2 isinstance函数

```python
#基本格式
isinstance(数值,类型符)
```

```python
#举例
isinstance(23,int)
##返回True
```

###### 举例1

```python
x = 2
y = True
z = 1.23
c = complex(1,2)
type(c)   ##输出complex
isinstance(z,float)   ##s
```

####  6.3 数值型函数

- Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
- Python math 模块提供了许多对浮点数的数学运算函数。
- Python cmath 模块包含了一些用于复数运算的函数。
- cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
- 要使用 math 或 cmath 函数必须先导入：import math

#### 7 四种整数类型：十进制、二进制、八进制和十六进制

| 进制种类 | 引导符号 | 描述           | 函数  |
| -------- | -------- | -------------- | ----- |
| 十进制   | 无       | 1-10           |       |
| 二进制   | 0b或0B   | 0-1            | bin() |
| 八进制   | 0o或0O   | 0-7            | otc() |
| 十六进制 | 0x或0X   | 0-9a-f或0-9A-F | hex() |

注意：不同进制的整数之间可以直接运算

```python
(0x3F2+1010)/0o1762
# 结果：2.0
```

#### 8 实训：输入半径，计算并输出面积

```python
#python计算圆的面积
#引入pi的两种方法：
# 方法一： 
import math
print(math.pi)
# 方法二： 
from math import pi
print(pi)
# 计算圆的面积的代码： #计算圆的面积
from math import pi
r=float(input('输入半径的长度：'))
area=pi*r**2
print('输出圆的面积： %d米'%area)
3.141592653589793
3.141592653589793
```

