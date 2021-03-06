# Python1-8列表(list)

## 1 列表基本定义

#### 1.1 定义

1.List（列表）有序可变序列，元素在一对中括号[ ]中，用逗号分隔。

2.**同一个列表中元素的数据类型可以各不相同**，可以同时包含整数、实数、字符串等基本类型的元素，也可以包含列表、元组、字典、集合、函数以及其他任意对象。

#### 1.2 列表的创建

##### 1.2.1 用[ ]创建列表

```python
A = ['python','中国',"a",2000] 
B = [["AA",1],["BB",2]]  # 例表嵌套
C = []   # 空例表
```

```python
a = 1
b = [3,4]
L1 = [a,b] #根据a,b值创建一个列表，第1个元素是一个可变列表子对象
print(L1)
```

##### 1.2.2 list()函数转换

可转换的对象：元组，range对象，字符串或其他类型的可迭代对象

```python
A = list(range(1,10))
B = list("abcde")   #字符串可以迭代
```

**特殊的：**split

###### 举例1

```python
n=input("以逗号分隔输入5个数：")
n_list=n.split(",")   #split
print(n_list)      
```

输出结果：

```python
以逗号分隔输入5个数：4,i,h,8,h<br/>['4', 'i', 'h', '8', 'h']
```

##### 1.2.3 删除

```python
# 基本格式
del 列表对象名
```

## 2 列表访问

#### 2.1 列表索引从0开始

##### 2.1.1访问元素

```python
# 基本格式
列表对象[i]
```

说明：**i:**从左到右索引**i默认 0 开始**，从右到左索引**i默认 -1 开始**

##### 2.1.2查找元素

```python
# 基本格式
列表对象.index(元素值)
```

说明：返回索引位置

##### 2.1.3 特殊（元组嵌套）

```python
#访问list中的某个姓名
std_list=[['张宁', 90], ['李明', 87]]
print(std_list[0][0])    # 第一个的第一个元素
# 输出>>>'张宁'
```

#### 2.2 切片访问

##### 2.2.1格式

```python
# 基本格式
列表对象[start:end:step]
```

##### 2.2.2说明：

| **start** | **起始位置索引**        | **省略时表示包含end前的所有元素**                            |
| --------- | ----------------------- | ------------------------------------------------------------ |
| **end**   | **结束位置索引**        | **结果中不包含结束位置对应的元素，省略时表示包含start后的所有元素** |
| **step**  | **表示是步长，默认为1** | **正数表示从左到右，负数表示从右到左**                       |

###### 举例1

```python
a = list(range(1, 10))  #1，2，3，4，5，6，7，8，9，10
print(a)     # 输出列表
print(a[1:5])    # 输出第1，2，3，4号元素即 [2, 3, 4, 5]
print(a[-1:-4:-2])    # 输出从右边开始到第4个元素中间隔为-2的元素即-1，-3号元素[9, 7]
print(a_list[::-1])   # 反向输出所有元素
print(a_list[4:])     # 输出第4号元素开始到最后的所有元素
```

```python
print(a_list[-2:2:2]) #输出从-2号元素到2号(-7号）元素之间的元素，因此步长应该为负数，所以输出是空列表
print(a_list[-8:6:2]) #输出从-8号元素到6号（-3号）元素之间的元素，即-8，-6，-4号元素值 [2, 4, 6]
```

###### 举例2

```python
# 练习：访问a_list中的最后两个元素,访问前面3个元素，访问3，4，5号元素
a_list = list(range(1, 10))
print(a_list)          # 输出列表 
print(a_list[-1:-3:-1])     # 访问最后两个元素
print(a_list[:3])           # 访问前面3个元素 
print(a_list[2:5])          # 访问3，4，5号元素
# 输出格式
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8]
[1, 2, 3]
[3, 4, 5]
'''
```

#### 2.3 列表元素遍历用操作

##### 2.3.1 用for循环遍历

###### 举例1

```python
#求b_list中所有整型元素的个数
b_list = ['physics', 'chemistry', 1997, 2000]
c=0
for i in b_list:
    if  isinstance(i,int):
        print(i)
        c=c+1
print(f"总共有{c}个")
# 输出格式
'''
1997
2000
总共有2个
'''
```

###### 举例2

```python
"""
建立一个空列表，添加如下所示的元素：
12,21,'python',77,86,33.6,{name:Jack},'66',88
要求：1、打印原列表；2、只保留整数元素，并按降序排序后展示。
"""
yi = [12,21,'python',77,86,33.6,{'name':'Jack'},'66',88]
print("输出原列表")
print(yi)    # 输出原列表
for i in range(len(yi)-1,-1,-1):
    if not isinstance(yi[i],int):       # 判断列表元素，因not如果为真则为假。 if isinstance(yi[i],(float,str,dict,list,tuple))
        del yi[i]       # 删除元素
print(yi)    # 验证列表  
yi.sort(reverse=True)      # 排序
print("只保留整数元素，并按降序排序后展示")
print(yi)
# 输出格式
'''
输出原列表
[12, 21, 'python', 77, 86, 33.6, {'name': 'Jack'}, '66', 88]
[12, 21, 77, 86, 88]
只保留整数元素，并按降序排序后展示
[88, 86, 77, 21, 12]
'''
```

###### 举例3

```python
# 输入一个姓名，显示其成绩
std_list=[['张宁', 90, 85, 78], ['李明', 87, 97, 75], ['王一', 89, 65, 70]]
name=input("name:")
for i in std_list:
    if name==i[0]:
        print(i)
        break
else:
    print("姓名输入错误")
# 输出格式
'''
name:张宁
['张宁', 90, 85, 78]
'''
```

###### 举例4

```python
# 创建一个列表，求列表中数值型数据的平均值
n_list = [12, 45, "a", 56.8, 78]
s = c = 0
for i in n_list:
    if isinstance(i, int) or isinstance(i, float):
        s += i
        c += 1
avg = s / c
print(avg)
# 输出格式
'''
47.95
'''
```

###### 举例5

```python
#练习，创建一个包含5个元素的成绩列表，显示不及格的元素，并求及格的个数
x_list=[45,65,85,99,75]
n=0
for i in x_list:
    if i<60:
        print(i)
    else:
        n=n+1
print(n)
# 输出格式
'''
45
4
'''
```

## 3 列表常用操作

#### 3.1 列表修改元素

##### 3.1.1 单个元素修改

```python
# 基本格式
# 通过索引进行定位，然后指定新的内容，数据类型不限。
a_list[2] = "A"
```

```python
# 修改单个元素
a_list = list(range(1, 10))
a_list[2] = "A"       # 第三个
a_list[4] = [1, 2, 3]    # 第四个
print(a_list)
# 输出格式
'''
[1, 2, 'A', 4, [1, 2, 3], 6, 7, 8, 9]
'''
```

##### 3.1.2连续元素修改

通过切片指定连续区域，然后设置新的内容，必须是可迭代对象，迭代对象中元素个数不限。

```python
# 基本格式
a_list[2:4] = ["A", "B", "C", "D"]
a_list[1:3] = 5    # 赋的值不是可迭代对象，所以出错
```

```python
#修改连续多个元素,赋的值必须是可迭代对象，但元素值的个数不限制
#a_list[1:3] = 5# 赋的值不是可迭代对象，所以出错
a_list = list(range(1, 10))
a_list[2:4] = ["A","B","C","D"]
print(a_list)
```

##### 3.1.2 非连续区域进行修改

通过切片指定非连续区域，然后设置新的内容，必须是可迭代对象，并且迭代对象中元素个数与非连续区域元素个数相同。

``` python
# 基本格式
a_list[2:6:2] = ["A", "B"]      
a_list[2:6:2] = ["A","B","C"]   # 赋的值有3个值，而列表中修改的是2个元素，不相同而出错
```

#### 3.2 列表增加元素

##### 3.2.1 添加元素

append()方法

```python
append(‘Google’)     # 在列表末尾添加1个元素
```

##### 3.2.2 插入元素

insert()方法

```python
b_list.insert(3, 13) # 在第3个元素插入13
```

#### 3.3 列表删除元素

##### 3.3.1 del 列表名[i]      #    i指定位置

```python
del list[2]            # 删除list列表第2个元素
```

##### 3.3.2 pop方法

```python
b_list.pop()            # 删除list列表最后1个元素
```

##### 3.3.3 remove()方法

```python
b_list.remove(‘Google’)            # 删除list列表值为’Google’的元素
```

#### 3.4 列表复制

##### 3.4.1 直接复制

```python
# 基本格式
L2 = L1 
#L1与L2指向的是同一个列表，修改L2元素时，L1元素也改变。
```

###### 举例1

```python
L2=L1             #L2与L1存放的是同一列表的指针
L2[0]=5            #列表的第0个元素改为5
L2[1][0]=0          #列表的第1个元素子对象列表第0个元素改为0
L2.append(12)       #列表添加一个新元素12
L1,L2           # L2与L1元素均发生改变
#输出
#([5, [0, 4], 12], [5, [0, 4], 12])
```

##### 3.4.2 浅拷贝

没有拷贝子对象（子对象是列表、字典等可变对象），修改L2子对象元素L1子对象元素也会改变。

```python
# 基本格式
L2 = L1.copy()
L2 = L1[:]
```

###### 举例1

```python
# 浅拷贝一
a=1
b=[3,4]
L1=[a,b]
#浅拷贝，L1[1]子对象是列表会随着L2修改而变化，L1其他元素不会L1变化
L2=L1.copy()
L2[0]=5
L2[1][0]=0
L2.append(12)
L1,L2
```

###### 举例2

```python
#浅拷贝二
a=1
b=[3,4]
L1=[a,b]
#浅拷贝，L1[1]与L2[1]指的是相同列表，修改L2[1]元素时L1[1]也会改变，但其他元素不会变化
L2=L1[:]      #浅拷贝
L2[0]=5       #L2[2]改变为5，但L1[2]不会变
L2[1][0]=0    #L2[1]是一列表子对象，并没有拷贝，所以L1[0]也改为了0
L2.append(12) 
L1,L2         #L1与L2子对象元素值同时发生改变，L1其他元素没有改变
```

##### 3.4.3 深拷贝

包含对象里面的子对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变

```python
# 基本格式
L2=copy.deepcopy(L1)  
#预先导入copy模块：import copy
```

###### 举例1

```python
#深拷贝
a=1
b=[3,4]
L1=[a,b]
import copy
L2=copy.deepcopy(L1)      #L1,L2是完全不相同的变量
L2[0]=5
L2[1][0]=0
L2.append(12)
L1,L2            #L2修改时，L1不会变化
```

## 4 列表常用方法

#### 4.1 方法

| 方法sorted                   | 说明                                                         | 例:m=[1,2,3]                                           |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| append(X)                    | 末尾添加元素X                                                | m.append(4)<br />m为[1,2,3,4]                          |
| extend(X)                    | 一次添加多个元素至列表尾部                                   | m.extend(4,5,6)                                        |
| insert(index,X )             | index指定位置插入X<br />该位置后索引都加1<br />index为正大于列表长则在后面添加X<br />index为负小于列表长度的相反数，则在列表头部添加 | m.insert([0,0])<br />m为[0,1,2,3]                      |
| remove(X)                    | 删除第一个为X的元素，该元素之后所有元素前移并且索引减1，不存在X则抛出异常。 | m.remove(2)<br />m为[1,3]                              |
| pop(index)                   | 删除并返回列表中下标为index的元素，不指定则为-1，弹出最后一个元素，如果弹出中间一个元素，则后面索引减1。<br />index不是[-L，L]区间上的整数则抛出异常 | x=pop()<br />删除最后一个元素3，X值赋予3<br />m为[1,2] |
| clear()                      | 清空列表，删除列表中所以元素，保留列表对象                   | m.clear()                                              |
| index(X)                     | 返回列表中第一个值为X的元素索引<br />若不存在值为X的元素则抛出异常。 | m.index(3)                                             |
| count(X)                     | 返回X在列表中的出现次数                                      | m.count(2)                                             |
| reverse()                    | 对列表所有元素进行原地逆序，首尾交换                         | m.reverse()<br />m.为[3,2,1]                           |
| sort(key=None,reverse=False) | 对列表所有元素进行原地逆序,key原来指定排序规则，False为升序，True表示降序。 | m.sort(reverse=True)<br />[3,2,1]                      |

###### 举例1

```python
# 求出list5列表每个学生的总分,将姓名与总分添加到一个新的列表
std_list=[['张宁', 90, 85, 78], ['李明', 87, 97, 75], ['王一', 89, 65, 70]]
zf=[]
for i in std_list:
    zf.append([i[0],sum(i[1:])])
print(zf)
```

## 5 内置函数

#### 5.1 函数

| 函数sort                   | 作用                                                         | 举例m=[1,2,3,2]                |
| -------------------------- | ------------------------------------------------------------ | ------------------------------ |
| len(列表)                  | 获取列表中元素的个数                                         | len(m)   #4个                  |
| max(列表)                  | 获取列表最大元素，前提是列表中元素可比较。                   | max(m)                         |
| min(列表)                  | 获取列表最小元素，前提是列表中元素可比较。                   | min(m)                         |
| sum(列表)                  | 列表元素求和，前提是可以执行加法运算。                       | sum(m)                         |
| reversed(列表)             | 列表逆序，返回一个可迭代对象。                               | reveresd(m)                    |
| sorted(列表，key，reverse) | 对列表中元素进行排序，返回一个新列表前提是元素之间可比较，否则会报错，默认为升序。 |                                |
| coumerate(列表)            | 生成一个枚举对象，每个元素为索引和值形成的元组。             |                                |
| zip(列表，列表)            | 生成一个zip对象，每个元素为列表中对应位置元素形成的元组。    | zip([1,2],[5,6])#[[1,5],[2,6]] |

**注意:**

​        列表的sorted方法与内置函数sort的区别，部分内置函数也可以用于元组、字典与集合。

## 6 列表运算符

#### 6.1 运算符

| 方法         | 作用                                           | 举例 |
| ------------ | ---------------------------------------------- | ---- |
| 列表1+列表2  | 合并并且返回一个新列表                         |      |
| 列表*X       | 复制X份，并且返回一个新列表                    |      |
| 元素 in 列表 | 判断【列表】中是否存在【元素】，存在则返回True |      |

###### 举例1

```python
# 编写程序，求每个同学总分，并添加到每个学生成绩
std_list=[["张宁",90,85,78],["李明",87,97,75],["王一",89,65,70]]
list_avg=[]
for i in std_list:
    i.append(sum(i[1:]))
print(std_list)  
```

## 7 列表推导式

#### 7.1 定义

列表推导式利用已有列表快速生成满足特定需求的列表。
列表推导式在逻辑上相当于一个循环，只是形式更加简洁。

#### 7.2 语法形式1

##### 7.2.1 基本格式

```python
#基本格式
[表达式  for 表达式中的变量  in 已有序列 if 条件]
```

###### 举例1

```python
# 生成简单列表
a_list = [i*i for i in range(1, 10)]
print(a_list)
```

###### 举例2

将c_list每个元素加2分

```python
# 方法1
c_list=[90,56,70,80,55,44]
b=[]
for i in c_list:
    b.append(i+2)
print(b)
```

列表推导式方法

```python
# 方法2
c_list=[90,56,70,80,55,44]
m=[i+2 for i in c_list ]
print(m)
```

###### 举例3

列表元素之间的运算

```python
#方法1;
english=[90,56,70,80,55,44]
math=[80,92,70,80,55,44]
zf_list=[]
for i,j in zip(english,math):
    zf_list.append(i+j)
print(zf_list)
# zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
```

列表推导式方法

```python
#方法2：
english=[90,56,70,80,55,44]
math=[80,92,70,80,55,44]

zf_list=[i+j for i,j in zip(english,math)]
print(zf_list)
```

#### 7.3语法形式2

```python
#基本格式
[表达式1 if 条件 else 表达式2 for 表达式中的变量  in 已有序列 ]
```

## 8 作业

#### 8.1 创建一个列表[110,'dog','cat',120,'apple'] 

```python
a_list=[110,'dog','cat',120,'apple']
a_list
```

#### 8.2 在列表中关于'dog'和'cat'之间插入一个空列表

```python
a_list.insert(2,[])
a_list
```

#### 8.3 删除列表中'apple'

```python
a_list.remove('apple')
a_list
```

#### 8.4 查找出列表中的数值110的位置，并增大10倍

```python
b_list=[i*10 if i==110 else i for i in a_list ]
print(b_list)
```

#### 8.5 输出列表

```python
print(a_list)
```

#### 8.6 将列表中数值取出来创建一个新列表（并按升序排列），字符串取出来创建另一个新列表

```python
a=[i for i in b_list if isinstance(i,int)]
b=[i for i in b_list if isinstance(i,str)]
a=sorted(a)
print(a)
print(b)
```
