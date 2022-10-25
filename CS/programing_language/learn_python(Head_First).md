# Head First Python

## 第 1 章

```python

# BIF
dir()  # 列出一个对象的属性
help() # 访问 Python 文档

```

## 第 2, 3 章

### 数据类型与结构

> 数字，字符串和对象

> list
> dict
> set
> tuple

- sorted()
- from pprint import pprint ( pretty print )
#### list
```python
l1 = []
l2 = list('很好用')
l3 = [x for x in [1,3,4,5]]

l.append()
l.remove()
l.pop()
l.insert()
l.extend()

l_copy = l.copy()

l[::]
l[0:max:1]
l[-max:-1:-1]

```

#### dict 无序
```python
d1 = {}
d2 = dict(a=1, b=2)

d[key]
d.items()
d.setdefault(key, value)

pprint(d)

```

#### set 无序
```python
s1 = set()   # 空集
s2 = {1,2,3}

u = s.union(set(word))        # 并集
d = s.diffrence(set(word))    # A - B
i = s.intersection(set(word)) # 交集

```

#### tuple 有序
```python
t1 = (1,)


```

### 第 4 章

#### 函数

> 模块
- import 是按 标准库 -> site-packages -> 当前目录 的顺序查询
- 安装自定义模块
  1. 创建一个发布描述 
     1. setup.py
        1. from setuptools import setup
        2. setup(参数) 
     2. README.txt
  2. 生成发布文件 python setup.py
  3. 安装发布文件 pip install xxx.zip

> 值调用与引用调用 是否为可变参数


### 第 6 章

> 文件

- open 函数的模式
  1. r:  0 (不删除)
  2. r+: 0 (会覆盖内容)
  3. w:  0
  4. w+: 0
  5. a:  末尾
  6. a+: 末尾
  
- f.tell
- f.seek: 改变指针位置
- f.truncate: 删除指针后（包含）的内容，不改变指针位置
