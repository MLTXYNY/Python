# Python1-4语句

## 1 条件语句if

#### 1.1 单分支语句

```python
#基本格式1
if (条件判断):       #此处的括号可以省略
    程序代码块
#如果代码区块只有一道指令则可以写成如下格式。
#基本格式2
if (条件判断): 程序代码区块
```

###### 举例1

```python
#举例
age = 18    # 变量（年龄）赋值为18
#格式1：
if age<40:   # 判断是否小于40岁
    print("小于40岁")    # 条件成立则输出
#格式2：
if age<40:print("小于40岁")   # 和上面一样，不过因为只有一个条件语句所以是可以放一行来写的。
#基本输出
'''
小于40岁
小于40岁
'''
```

###### 举例2

```python
#举例{输出一个用户数的绝对值(只用if单支结构)}
num = int(input("输入任意整值："))
if num < 0:        # 判断是否小于0，如果小于，则通过下面的语句进行绝对值转换，如果大于0则直接跳过改语句进入下面的输出语句。
    num=abs(num)         # 调用abs函数 还有此行可以合并到上面一行。
print("绝对值是%d"%num)  # 输出方式一
print(f"绝对值是{num}")  # 输出方式二
#基本输出
'''
输入任意整值：10
绝对值是10
'''
```

#### 1.2 双分支语句

```python
#基本格式
if 条件判断:
    程序代码区块一       #T（正确，或者说条件成立）
else:
    程序代码区块二       #F（错误，上面的条件不成立）
```

###### 举例1

```python
#举例{年龄判断}
age = int(input("请输入年龄："))   # 用户输入年龄（数）
if age < 18:
    print("未成年")
else:
    print("成年")
```

###### 举例2

```python
#举例{奇偶数的判断}
num = int(input("输入任意整值："))    # 用户输入数
rem = num % 2     # 用户输入的数除以2看能不能除整除
if rem == 0:      # 如果可以整除则是偶数
    print("%d是偶数"%num)
else:             # 不可以整除，是奇数
    print("%d是奇数"%num)
```

#### 1.3 多分支语句

```python
#基本格式
if 条件判断一:
    程序代码区块一:
elif 条件判断二:
    程序代码区块二:
#省略...
else:
    程序代码区块N:
```

**注意：**运算符优先级没有把握时可以添加括号进行区分。

###### 举例1

```python
# 举例
"""
有一地区的票价收费标准是100元。
但是如果小于等于6岁或大于等于80岁，收费是打2折。
但是如果是7-12岁或者60-79岁，收费是打5折。
"""
age = int(input("请输入年龄："))   #输入
piao = 100     # 基础票价收费标准
if age<=6 or age>=80:        # 此处对应题目第二行 这里还可以写为(age<=6) or (age>=80)  
    piao=piao*0.2            # 打2折计算
    print(f"票价为{piao}")  # 输出票价 
elif age>=60 or age<=12:     # 此处对应题目第3行
    piao=piao*0.5            # 打5折计算
    print(f"票价为{piao}")  # 输出票价
else:                       #上面两个不成立时执行这个语句块
    print(f"票价为{piao}")
```

###### 举例2

```python
# 举例
# 用户输入字符然后告诉用户所输入的字符是大写字母还是小写字母，阿拉伯数字或者其他字符。
# 方法1
ch = input("请输入单个字符")
if ord(ch) >= ord("A") and ord(ch)<=ord("Z"):
    print("这是大写字符")
elif ord(ch) >= ord("a") and ord(ch)<=ord("z"):
    print("这是小写字符")
elif ord(ch)>=ord("0") and ord(ch)<=ord("9"):
    print("这是数字")
else:
    print("这是特殊字符")
# 方法2
cc = input("请输入单个字符")
if "a"<=cc<="z":
    print(f"这个是小写字母")
elif "A"<=cc<="Z":
    print(f"这个是大写字母")
elif "0"<=cc<="9":
    print(f"这个是数字")
else:
    print("这是特殊字符")
```

**上例解析：**

​		ord()函数主要用来返回对应字符的ASCII码
​		chr()主要用来表示ascii码对应的字符他的输入时数字
​		bin()二进制，oct()八进制，hex()十六进制

#### 1.4 分支语句嵌套

```python
#基本格式:
if 条件判断一:
    if 条件判断A:
        程序代码区块A:
    else :
        程序代码区块B:
else:
    程序代码区块二:
```

注意缩进！！！注意缩进！！！注意缩进！！！，在一些编辑器中还要求要统一的缩进方式不能混用，，例如：用了空格的缩进那么后面的代码也只能用空格来控制缩进不能混用。

###### 举例1

```python
'''
1 测试一年是否为闰年
2 闰年的条件为可以被4整除
3 并且除以100时余数不为0或是除以400时余数为0
4 必须同时符合两个条件。
'''
year=int(input("请输入年份："))
rem4=year%4      # 条件2
rem100=year%100  # 条件3
rem400=year%400  # 条件3
if rem4 == 0:    
    if rem100 != 0 or rem400 == 0:     # 条件4  除以100时余数不为0或是除以400时余数为0
        print("%s是闰年"%year)
    else :
        print("%s不是闰年"%year)
else:
    print("%s不是闰年"%year)
```

###### 举例2

```python
"""
1 成绩从百分制变换到等级制。
2 要求先判断成绩是否在0和100之间
3 大于90为A
4 大于80为B
5 大于70为C
6 大于60为D
7 小于60为E
"""
score = float(input("输入分数"))
if score > 100 or score < 0:
    y = "成绩必须在0~100分之间"
else:
    if score >= 90:y = 'A'
    elif score >= 80:y = 'B'
    elif score >= 70:y = 'C'
    elif score >= 60:y = 'D'
    else: y = 'E'
print("等级为",y)
```

## 2 for循环

#### 2.1 基本for循环

for可以将整个对象内的元素遍历（也可以说是迭代），遍历期间同时记录或输出每次遍历的状态或者轨迹。
**迭代(iteration)：**重复执行。;

```python
#基本格式：
for var in 可迭代对象:      #var为元素。
	程序代码区块
else:                 #可以加入条件语句
    程序代码区块
```

**可迭代对象（iterable object）：**可以是列表，元组，字典，集合，range()函数。

###### 举例1

```python
#基本案例遍历列表
zms = ["1","2","3","4","5"]    # "1"和1写法都可以
for zm in zms:
    print(zm)
```

#### 2.2 常用的range()函数

range()函数产生一个等差数列，又称为可迭代对象。可以用来做循环计数器。【只有迭代时的计数指针需要内存节省内存空间】

##### 2.2.1 range()函数

```python
#基本格式：
range(start,stop,step)
```

| 参数  |                                |
| ----- | ------------------------------ |
| start | 默认为1，如果省略掉则从0开始。 |
| stop  | 等差范围（stop-1）             |
| step  | 预设为1                        |

###### 案例1

```python
# 输出1到10
# 正向
for a in range(1,10+1):print(a)    #加给1才可以输出到10
# 反向
for a in range(10,-1,-1):print(a)
```

**1.当range只有一个参数时**

```python
range(n)    #产生0，1，2....n-1的可迭代对象内容。
```

**2.当range只有两个参数时**

```python
range(start,end)    
#start是起始值,end-1是终止值。
```

**3.当range有三个参数时**

```python
range(start,end，step)   #step是间隔值。
```

###### 举例2

```python
#输入一个正整数n,这个程序会输出从1到n的总和。
n = int(input("请输入整数："))
total = sum(range(n+1))
print("从1到%d的总和是="%n,total)
```

​        此程序的工作原理并不是一次预留存储1-n的内存空间，只有一个内存空间，每次迭代的指针放在此空间执行，然后num运算，增加工作效率并且节约内存空间

#### 2.3 进阶的for循环

##### 2.3.1 for的循环嵌套

```python
# 基本格式
for 变量 in 对象:       #外层循环
    ...
    for 变量 in 对象:   #内层循环
        ...
```

###### 举例1

```python
# 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print("%d*%d=%-3d"%(i,j,result),end=" ")  
        #%-3d表达的是每一个输出预留3格。
    print()
```

###### 举例2

```python
# 绘制直角三角形
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("*",end="")
    print()
```

##### 2.3.2 for...else循环

```python
#基本格式
for 变量 in 对象:
    程序代码区块1
    if 条件表达式：     #如果条件表达式是T，则离开循环
        程序代码区块2
        break        #下面有介绍
    程序代码区块3
else:
    程序代码区块4      #最后一次循环条件表达式是F则执行
```

###### 举例1

```python
# 测试一个数字N是否是质素
# 质素条件：2是质素。N不可被2至n-1的数字整除。
N = int(input("请输入大于1的整数做质素测试："))
if N == 2:                       #2是质素所以直接输出 
    print("%d是质素"%N)
else:
    for n in range(2,N):         #用2...N-1当除数测试
        if N % n == 0:           #如果整除则不是质素
            print("%d不是质素"%N)
            break                  #离开循环
    else:                         #否则是质素
        print("%d是质素"%N)
```

## 3 while循环

#### 3.1 基本while循环

while循环会一直循环，直到条件运算为False才会离开循环。

```python
#基本格式
while 条件运算:    #假如条件运算为1时进行循环
    程序区块
```

###### 举例1

```python
# while案例1：猜数字游戏。
num = 30     #正确的数字
guess = 0   #初始值  guess(猜到)
while guess != num:
    guess = int(input("请猜1-100间的数字："))   #输入的数guess
    if guess > num:       #比较
        print("请猜小一点")
    elif guess < num:     #比较
        print("请猜大一点")
    else:                 
        print("恭喜答对了")
```

###### 举例2

```python
while索引值变化的观察
index = 1    #索引值
while index <= 5:    #5次循环
    print("第%d次while循环"%index)    # 输出
    index += 1   #每次加1
```

#### 3.2 嵌套while循环

```python
#基本格式
while 条件运算：       #外层循环   
    ...
    while 条件运算:
        ...        #内层循环
```

###### 举例1

```python
# 打印九九乘法表
i = 1           #设定i的初始值
while i <= 9:         #当i大于9跳出外层循环
    j = 1              #设定j初始值
    while j <= 9:        #当j大于9跳出内层循环
        result = i * j
        print("%d*%d=%-5d"%(i,j,result),end=" ")  #%-5空五个字符
        j += 1        #内层循环加1
    print()            #换行输出
    i += 1                  #外层循环加一
```

#### 3.3 while循环条件表达式与对象

```python
#基本格式
while 条件表达式:       #与有关的条件表达式（列表，元组，字典）
    程序区块
```

###### 举例1

```python
fruits = ['apple','orange','apple','banana','apple']   #列表
fruit = 'apple'                 #指定元素
print("删除前的fruits",fruits) 
while fruit  in fruits:         #只要列表里面有apple循环就继续。
    fruits.remove(fruit)       #remove() 函数用于移除列表中某个值的第一个匹配项。
print("删除后的fruits",fruits)

#输出格式
'''
删除前的fruits ['apple', 'orange', 'apple', 'banana', 'apple']
删除后的fruits ['orange', 'banana']
'''
```

## 4 break语句

在while循环和for循环中都可以用，一般在if结构，被执行后整个循环提前结束。

## 5 continue语句

在while循环和for循环中都可以用，一般在if结构，被执行后整个循环提前结束。

## 6 pass语句

空语句，保存结构完整性，占位符。

## 7 else语句

在while循环和for循环中都可以用。

