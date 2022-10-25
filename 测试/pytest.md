# pytest

> Pytest使用教程 @ABTester (bilibili)

## P1-2

```python
# - pytest 检测的命名规则
#   1.测试文件:  test_*
#   2.测试类:   Test*
#   3.测试方法: test*
def test_1():    # pytest directory 将递归寻找符合命名规则的方法测试
    asssert True
```

## P3 命令行参数

| 参数                | 作用                         | 使用                  |
|---------------------|------------------------------|-----------------------|
| \-\-collection-only | 收集需要测试的方法，且不执行 |                       |
| -k expression       | 匹配 k 表达式的方法          | -k "test_1 or test_2" |
| -m mark             | 执行标记方法                 | @pytest.mark.P1       |
| -x                  | 失败后立即结束               |                       |
| -v                  | 显示执行的详细信息           |                       |
| \-\-maxfail=num     | 最大错误次数                 |                       |
| -s                  | 打印 print 信息              |                       |
| \-\-lf              | 只打印错误信息               |                       |
| \-\-ff              | 都打印                       |                       |

## P4-7 fixture

```python
@pytest.fixture # 固定常用的功能
def foo():
    return 'something'

def test_x(foo):
    assert foo == 'something'

# 参数化 ddt 数据驱动
@pytest.mark.parametrize('arg1, arg2', [], ())
def test_ddt(arg1, arg2):
```

