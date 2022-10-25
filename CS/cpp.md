# C++

## P1-

- precompile(.i) - compile(.s) - assemble(.o) - link(.out)
- int main()不是必须要 return (特例)
- else if() = else     if() 
- static 类或结构体内/外部使用static
  - 外部：extern int s_Variable
  - 内部：静态变量需要在外部定义
- 双冒号 :: 
  1. namespace
  2. 类体外定义
  3. 类静态变量引用
  4. 全局变量 ::a


## 

```c++
// const 用法 只读
// 1
const int a;
int const a;
// 2
const int* p;
int const* p;
int* const p;
// 3
class Foo
{
public:
    int m_x;

    void GetX() const
    {
        // can't use m_x from outside
        return m_x;
    }
}
```
