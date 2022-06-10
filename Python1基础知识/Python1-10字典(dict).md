# Python1-10字典(dict)

## 1 字典基本

#### 1.1 定义

1.字典(dictionary)是一种映射类型，字典用"{ }"标识。字典中每个元素由索引(key)和它对应的值value组成。

2.不允许同一个键出现两次，键必须不可变（可以用数字，字符串或元组）

3.字典是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。 

4.两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

#### 1.2 创建

##### 1.2.1 大括号包裹键值对创建字典对象

```python
# 基本格式
字典名={键1:值1,键2:值}   #键key   值value
```

##### 1.2.2 使用dict()函数创建字典对象

```python
# 举例
a_dict = {"姓名": "张三", "年龄": 20, "体重": 172, "身高": 172}
b_dict = {} # 创建空字典
```

注意：

​	将可迭代对象转化为字典时，要求可迭代对象中每个元素的长度为2。

## 2 字典元素访问

#### 2.1定义

字典是无序的，因此不支持索引、切片等操作。

主要通过字典对象[键]获取对应的值。此外，字典还提供了获取所有键值对、所有键、所有值等方法。

#### 2.2 访问指定字典元素

```python
# 主要有d[key] 或d.get(key)   输入键，返回值。
# 方法1： 
a_dict[“姓名”] #输出值：张三
# 方法2： 
a_dict.get(“姓名”) #若字典中没有key值，get则返回None（空值）
```

#### 2.3 访问字典所有《键》

```python
# 基本格式
d.keys()
```

#### 2.4 访问字典的所有《值》

```python
# 基本格式
d.values()
```

#### 2.5 访问字典所有《键值对》

```python
# 基本格式
d.items()   #返回的结果是元组组成的列表
```

#### 2.6 遍历字典

```python
#基本格式
for i in a_dict.keys():
    print(i,a_dic[i])
```

###### 举例1

```python
a_dict = {"姓名": "张三", "年龄": 20, "体重": 172, "身高": 172}
for i in a_dict.keys():
    print(i,a_dic[i])
```

###### 举例2

```python
# 求成绩总分
# 方法一
score={"语文":90,'数学':55,"英语":70,"计算机":50,"python":87}
s=0
for i in score.values():
    s=s+i
print(s)

# 方法二
sum(score.values())  #字典求和
```

## 3 字典常用操作

#### 3.1 添加和修改字典元素值

##### 3.1.1 方法一

```python
# 基本格式
字典对象[key]=值   #键若存在修改值 ，不存在则添加元素
```

```python
a_dict[“年龄”]=21
```

##### 3.1.2 方法二

```python
# 基本格式
字典对象.update(字典对象)
```

```python
a_dict.update(d_dict)
```

###### 举例1

```python
a_dict = {"姓名": "张三", "年龄": 20, "体重": 172, "身高": 172}
d_dict = dict([("体重", 156), ("身高", 177),("爱好",["跳舞","画画"])])
#在a_dict中增加民族
a_dict["民族"]="汉族"
print(a_dict)
#用d_dict更新a_dict
a_dict.update(d_dict)
print(a_dict)
```

#### 3.2 删除字典元素

##### 3.2.1 方法一

```python
# 基本格式
del 字典对象[key]
```

###### 举例1

```python
# 删除a_dict["爱好"]
del a_dict["爱好"]
a_dict
```

##### 3.2.2 方法二

```python
# 基本格式
字典对象. (key,[default])
#从字典中删除指定的键，返回该键对应的值,若key不存在返回default值
```

```python
a_dict.pop(“年龄”,"无此健")
```

#### 3.3 清除字典所有元素

```python
#基本格式
字典对象.clear()
```

```python
a_dict.clear()、
```

## 4 字典推导式

#### 4.1 定义

字典推导式的写法是放在一对大括号中。表达式中包含键和值两部分，并分别指定这两部分的值。

#### 4.2 语法形式1

```python
#基本格式
字典名={键表达式:值表达式 for 变量 in 已有序列 if 条件}
```

```python
nopass={k:v for k,v in score.items() if v<60 }
```

###### 举例1

```python
# 现有一个字典包含了课程名和成绩，将不及格的元素赋给另一个字典,并显示
# 方法一
nopass={}
score={"语文":90,'数学':55,"英语":70,"计算机":50,"python":90}
for i in score.keys():
    if  score[i]<60:
        nopass[i]=score[i]
print(nopass)   
# 方法二
nopass={k:v for k,v in score.items() if v<60}
print(nopass)
```

#### 4.3 语法形式2

```python
#基本格式
字典名={键表达式:值表达式1 if 条件 else 值表达式2 for 变量 in 已有序列 }
```

```python
newscore={k:v+5 if v<60 else v for k,v in score.items()
```

###### 举例1

```python
# 将不及格的分数加5分，及格的不变
score={"语文":90,'数学':55,"英语":70,"计算机":50,"python":90}
a={k:v+5 if v<60 else v for k,v in score.items()}
print(a)
```

## 5 字典排序

#### 5.1 定义（使用sorted()方法）

系统中提供的**sorted()方法**可以对字典进行排序。字典排序大致可以分为**按照键进行排序**和**按照值进行排序**两种。

| **按键排序**       | **sorted(a_dict.items(), key=lambda item:item[0], reverse=True) # lambda为匿名函数** |
| ------------------ | ------------------------------------------------------------ |
| **按值排序**       | **sorted(a_list.items(), key=lambda item: item[1], reverse=True)** |
| **返回值**         | **是一个包含(key，value)的元组的列表**                       |
| **key**            | **指定排序关键字,使用匿名函数，item[0]表示键，item[1]表示值** |
| **a_dict.items()** | **是包含key，value的元组**                                   |
| **reverse**        | **指定顺序，True为降序，默认为False为降序**                  |

###### 举例1

```python
# 已知某次考试成绩结果如下，其中键表示学生姓名，值为对应的成绩。
a_dict = {"A": 70, "C": 85, "E": 90, "B": 66, "G": 82, "F": 77, "D": 54}

# 按照学生姓名进行排序，从小到大排序
a_dict = {"A": 70, "C": 85, "E": 90, "B": 66, "G": 82, "F": 77, "D": 54}
sorted(a_dict.items(),key=lambda item:item[0],reverse=True)

# 按照学生成绩降序进行排列
sorted(a_dict.items(),key=lambda item:item[1],reverse=False)
```

###### 举例2

```python
# 统计一个字符串中每个字符出现的频数，用字符为键，频数为值的字典存放
txt_str = "abcdeebbaa"
fre_str = {i:txt_str.count(i) for i in txt_str }
print(fre_str)
# 获取频数最多的字符
max_fre={i:v for i ,v in fre_str.items() if v==max(fre_str.values())}
print(max_fre)
```

## 6 字典常用函数

#### 6.1 len()

列出字典以及字典内的字典元素个数

#### 6.2 fromkeys()

 建立一个字典的方法

```python
# 基本格式
mane_dict=dict.fromkeys(seq[,value])      #使用seq序列建立字典，序列内容就是字典的键,如果没有value就用None当字典键的值
```

###### 举例1

```python
# 将列表转成字典
seq1 = ['name','city']     #定义列表
list_dict1 = dict.fromkeys(seq1)    #没有指定value值，则输出空值
print("字典1",list_dict1)
list_dict2 = dict.fromkeys(seq1,'chicago')    #指定了value值，则输出值
print("字典2",list_dict2)

# 将元组转成字典
seq2 = ['name','city']    #定义元组
tup_dict1 = dict.fromkeys(seq2)      #没有指定value值，则输出空值
print("字典3",tup_dict1q)
tup_dict2 = dict.fromkeys(seq2,'New York')  
print("字典4",tup_dict2)
```

#### 6.3 get()

搜寻字典的值，如果键存在则返回该键的值，如果不存在则返回默认值。

```python
#基本格式
value = dict.get(key[,default=none])   # key就是要搜寻的键，如果找不到就返回default的默认值（None）
```

###### 举例1

```python
fruits={'Apple':20,'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ",ret_value1)        #输出：Value = 25
ret_value2 = fruits.get('Grape')
print("Value = ",ret_value2)        #输出: Value = None
ret_value3 = fruits.get('Grape',10)
print("Value = ",ret_value3)        #输出：Value = 10
```

#### 6.4 setdefault()

与get()相同，不同之处在于get()方法不会改变字典内容。

使用setdefault()方法时若所搜寻的键不存在，将键-值加入字典 ,如果设有默认值则将键：默认值加入字典，如果没有设定值 

```python
# 基本格式
value = dict.setdefault(key[,default=none])   #dict是欲搜寻的字典
```

```python
# key在字典里面
fruits = {'Apple':20,'Orange':25}
vaule = fruits.setdefault('Orange')     
print("Value = ",valuel)       # 输出：Value = 25
print("fruiuts字典",fruits)     # 输出：fruiuts字典{'Apple':20,'Orange':25}
```

```python
# 'age'键不存在
person = {'name':'John'}

age = person.setdefault('age')
print("增加age键",person)    # 输出：增加age键{'name':'John'}
print("age=",age)           # 输出：age = None

sex = person.setdefault('sex','Male')
print("增加sex键",person)     # 输出：增加sex{'name':'John','age':None,'sex':'Male'}
print("sex = ",sex)          # 输出：sec = Male 
```

#### 6.5 pop()

删除字典元素

搜寻删除的元素的键，找到时就将该元素从字典删内删除，同时将删除的值回传，当找不到key时则传回default设定的内容，如果没有设定值则传回KeyError。

```python
# 基本格式
value = dict.pop(key[,default])     # dict是欲删除元素的字典
```

###### 举例1

```python
# 同时元素存在的应用
fruits = {'apple':20,'banana':15,'orange':22}
value = fruits.pop('orange')
print("传回删除元素的值",value)       # 传回删除元素的值 22
print("删除后返回字典的内容"，fruits)  # 删除后返回字典的内容{'apple':20,'banana':15}
```

###### 举例2

```python
# 同时元素不存在的应用
fruits = {'apple':20,'banana':15,'orange':22}
value = fruits.pop('grape','does not exist')
print("传回删除元素的值",value)       # 传回删除元素的值 does not exist
print("删除后返回字典的内容"，fruits)  # 删除后返回字典的内容{'apple':20,'banana':15，'orange':22}
```

## 7 作业

#### 7.1 创建一个某科目成绩组成的字典对象{'张三':96,'李明':50,'王文':95.5,'刘静一':58,'王宁':None}

```python
a_dict={'张三':96,'李明':50,'王文':95.5,'刘静一':58,'王宁':None}
print(a_dict)
```

#### 7.2 向字典增添一个学生成绩，将张三的成绩改为88

```python
a_dict["张三"]=88
a_dict["xx"]=100
print(a_dict)
```

#### 7.3 删除王宁

```python
del a_dict["王宁"]
a_dict
```

#### 7.4 将王文分数改为整数

```python
a_dict["王文"]=int(a_dict["王文"])
a_dict
```

#### 7.5 输入姓名，查询分数

```python
a=input("请输入名字:")
if a in a_dict.keys():
    print(a_dict[a])
else:
    print("输入错误")
```

#### 7.6 将不及格的分数均改为60分，其他分数不变，然后求出最高分的姓名

```python
b={k:v=60 if v<60 else v for k,v in a_dict.items()}
print(b)
```

#### 7.7 按成绩降序排列

```python
sorted(a_dict.items(),key=lambda item:item[1],reverse=False)
```

