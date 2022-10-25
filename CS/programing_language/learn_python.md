# 慕课网 #

课程项目：原生爬虫
主流应用：爬虫,大数据,AI,测试,Web,脚本处理

pythonic
Simple is better than complex
Now is better than never.Although never is ofen better than right now

``` python
x,y = y,x

```

* 常用方法: len(),id(),ord(),bool(),type()

## 数据类型 ##

### Number类型 ###

* int,float,long
* 进制表示与转换:
  * a = 0b1010,b = 0o12,c = 0xa
  * bin(num),int(num),hex(num),oct(num)
* 算术运算
  * 空为False
  * 乘*,乘方**;除/,取整//,取余%

### 组 ###

* 序列:str,list,tuple
* 操作:索引, 切片
  * 字符串(str)
    * ' "" ',"  ' '  "
    * 转义字符: (\n...
    * 换行输入: '''...''' 'hello\ 利用()
    * 原始字符串: r('...')
    * 字符串的运算: +,*('one'+'two', 'one'*3)
    * 切片: str = "hello world" str[0:5:1] (包头不包尾) str[6:] str[6:11]
  * 列表(list)
    * list[0]得到的值类型为值本身,list[0:1]则是一个列表
    * 常用方法: list.append(),list.insert() list.pop() list[2] = a
* 无序:
  * 集合: 
    * set 没有索引,不能切片
    * 不重复: {1,1,2,2,3,3}
    * 求差集: {} - {} 交集 {} & {} 并集 {} | {}
    * 定义空集: set()
    * 因为无序: {1,2,3} == {2,1,3}
  * 字典
    * key:value

### 条件判断 ###

* 表达式: 运算符和操作数的组合
* 3种判断: 值(value)的判断,身份(id)的判断,类型(type)的判断: isinstance(variable,(type))
* 'abc' < 'abc' 以第一个能判断的值的判断做结果
* and: 判断False直到最后一个; or: 判断True直到最后一个
* in: 'value' in {'key': 'value'} 为False 即以key判断
* is 和 == 的区别: 身份(id)比较 与 值的比较

### 变量 ###

* 变量是指向某块有值的内存即引用
* 值类型(不可变): int,str,tuple; 引用类型(可变): list,set,dict

### 运算符 ###

* 优先级: 算术运算符,比较运算符,逻辑运算符(not and or)

### 一些规范 ###

* python中形式常量 constant 常量 全部大写
* snippet

```python
# 输出为True的值
a = 1 b = 0

a or b

if:

else:

```

### 包,模块 ###

* 导入时会执行 __init__.py
  * 利用 __all__ = ['module1',] 在其他文件导入这个包时导入需要的模块;
  
    ``` python 
    if __name__ == "__main__":
    ```
  
  * 在 __init__.py 中批量导入
* 命名空间
* __all__ = ['','',] 当使用 * 时导入的变量
* 循环引入

### 函数(def) ###

* 输入: 参数(形参,实参)
  * 1 必须参数 (必须在默认参数之前)
  * 2 关键字参数 add(y=1, x=2)
  * 3 默认参数
  * 4 可变参数(*iterables, **iterables)
    * 传入的是一个 tuple
* 输出: 返回值(return)
  * 任意类型
  * 默认为 None

```python
# 序列解包
from sys import argv       # 参数 argv = []
first,second,third = argv  # 解包 列表中的参数个数和解包个数要相同
```

```python
def funcname(parameter_list):
  pass
  
  return 0
```

### 类(class) ###

* 类最基本的作用是 封装
* 类和对象: 类(cls), 实例化 -> 某个对象(self) (类(模板) > 对象(具体)))
* 行为: 方法(函数)
  * 构造函数( __init__(self, ) ): 返回None, 实例化时自动调用
  * 类方法, 实例方法, 静态方法
    * 类方法: @classmethod 调用类方法: ClassName.class_func()
    * 静态方法: @staticmethod
* 特征:数据成员(属性(变量))
  * 类变量, 实例变量  (类与模块的变量不太一样)
    * 访问类变量, ClassName.variable, self.__class__.variable, cls.variable
    * 访问实例变量, self.variable
* 类中的函数: 称为方法, 必要参数 self, 引用类内部属性需要self.xxx
* 类只负责定义不负责执行, 类的模块一般只写类
* 建议通过方法修改成员变量
* 成员可见性: 公开, 私有(__func, __variable)(假私有, 改个名 _ClassName__variable)
  * object1.__variable = 0 (新创建了一个实例变量)
* 继承(python有多继承), 封装, 多态
  * class ClassName(FatherClass)
  * super(ClassName, self).__init__()

```python
class ClassName(object):
    property1 = 'hello'               # 类属性
    property2 = 0

  # 构造函数
    def __init__(self, property1, property2):   # 先在实例变量(self.property)的字典(__dict__)里寻找,若没有则到类变量寻找,若没有再向父类里寻找...
        self.property1 = property1
        self.property2 = property2
        pass

    # 行为
    def func1(self):
        print(self.property1, self.property2)

        return 0

    @classmethod
    def class_func(cls):      # 类方法 cls: 类本身
        pass
```

### 正则表达式 ###

* 元字符, 字符集
* (匹配字符串的一些内置方法: in, index()...)
* re(regular expression)正则表达式模块
  * re.findall('', str, re.I | re.S)
  * 'str': 普通字符 '\d': 元字符
* 字符集 (都是单个字符)
  * 'a[1-9]c', 'a[^1-9]c'
  * 概括字符集
    * \d [0-9] 数字字符, \D [^0-9] 非数字字符
    * \w [0-9a-zA-Z\_] 单词字符 \W 非单词字符
    * \s [   ] 空白字符, \S
    * . 匹配除换行符 \n 之外其他所有字符
* 数量词 贪婪 '[a-z]{3,6}' 非贪婪(?) '[a-z]{3,6}?' 匹配
  * 'x*' 对x匹配0次或无限次
  * 'x+' 匹配1次或无限次
  * 'x?' 匹配0次或只有1次(去重) re.findall('python?', str)
* 边界匹配(^ $)
  * '10001' '^000' '000$'
* 组
  * () 且关系 [] 或关系 (r.group(0, 1, 2))
* re.sub('', '', str, )

```python
language = 'PythonC#JavaC#PHPC#'

def convert(value):
    matched = value.group()

    return matched

r = re.sub('', convert, language) # 把函数当成参数传入方法中, 对经过函数处理返回的数据进行替换
print(r)
```

### JSON ###

* 数据格式对应数据类型
* 反序列化

json    =>  python
object      dict
array       list
string      str
number      int,float
true        True
false       False
null        None

### 枚举(Enum) ###

* 是一个类(不能实例化, 单例模式)
* 枚举类型(ENUM.VARIABLE1), 枚举名字(VARIABLE1), 枚举的值(1)
* 比较 ENUM.V1 == ENUM.V2 ENUM.V1 is ENUM.V2

```python
from enum import Enum
from enum import IntEnum,unique     # 不允许相同值的枚举类型 @unique class ENUM(IntEnum):

class ENUM(Enum):  # 如果要写枚举，则要继承Enum
    VARIABLE1 = 1   # 常量，不可变
    VARIABLE2 = 2   # 不能使用相同名称
    VARIABLE1_ALIAS = 1 # VARIABLE1 的别名
print(CLASS.VARIABLE1.name) # .value, .name

for v in ENUM.__members__:
    print(v)

a = 1
ENUM(a) # 类似类型转换 只能转成枚举类中存在的类型
```

### 闭包 ###

* 一切皆对象
* 闭包 = 函数 + 环境变量(不受外部变量影响)(要引用了环境变量才能称作为闭包)
* 保存现场(记忆变量)(例3)

```python
# 例1
def curve_pre():
    a = 25               # 环境变量
    def curve(x):
        return a*x*x
    return curve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))

# 例2
def f1():
    a = 10
    def f2():
        a = 20  # a 被认为是一个局部变量
    return f2

f = f1()
print(f.__closure__)

# 例3
origin = 0

def factory(pos):
    def go(step):
        nonlocal pos            # 非局部变量
        new_pos = pos + step
        pos = new_pos           # 在这里赋值之后被认作是局部变量不会从上一层找
        return pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist(5))
print(tourist(6))
```

### 函数式编程 ###

* 三元表达式 r = True if x == 1 else False
* lambda parameter_list: expression (以":"分割 左边为参数，右边为表达式 (算子
* map(fun, *iterables)(是个类)(只能使代码变得简洁, 不能提升代码效率)
* reduce(function, sequence, initial)(map/reduce)
* filter(func, iterable)

```python
from functools import reduce

list_x = [1, 2, 3, 4, 5]
list_y = [1, 2, 3, 4, 5]
r = map(lambda x, y: x*x + y, list_x, list_y)
print(list(r))

r = reduce(lambda x, y: x + y, list_x)      # 连续调用第一个参数的函数(((1+2)+3)+4)+5) 列表前两项作为参数x, y, 返回结果作为下一次执行 lambda 的参数x, 再取列表下一项作为y
```

### 装饰器 ###

* 对函数添加某个功能

```python
import time
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator                      # 将装饰器的功能添加到了 f1 中并不改变 f1 的调用写法
def f1():
    print('This is a function')

f1()
```

### 爬虫 ###

* 步骤
  * 前奏
    * 明确目的
    * 找到数据对应网页
    * 分析网页结构找到数据所在标签位置
  * 模拟HTTP请求, 向服务器发送请求, 获取服务器返回的HTML
  * 用正则表达式提取数据

### 杂技 ###

* 字典模仿switch

```python
day = 0

def get_monday():
    return 'monday'

def get_sunday():
    return 'sunday'

def get_default():
    return 'Unkown'

switcher = {
    0: get_monday,
    1: get_sunday,
}
day_name = switcher.get(day, get_default)()
print(day_name)

```

* 列表推倒式
  * b = [i**2 for i in a if i >= 5]
  * d = {key:value for key, value in students.items()}
* None [] '' False 本质不同

```python
class Test():
    # 由这两个内置方法决定类的布尔值
    def __bool__(self):
        return False
    def __len__(self):
        return 5

print(bool(Test()))
```

![xx]('E:\Snipaste_2020-10-16_15-15-34.png')