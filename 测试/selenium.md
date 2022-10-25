# selenium

- driver = webdriver.Chrome()
- element.get_attribute("value")

- random.sample('1234567890abcdef', 5)

- element.location()     # 坐标偏差原因：缩放比例。。。



## PO 模型

- 页面，用例分离
- Case Data Page
- PageBase 定位方法类

## unittest

```python
import unittest

class Case():
    def setUp(self):        # 每条前置
        pass
    def tearDown(self):     # 每条后置
        pass
	@classmethod
    def setUpClass(cls):    # 所有 case 执行前置
        pass
	@classmethod
    def tearDownClass(cls): # 所有 case 执行后置
        pass
    @unittest.skip('description')
    def test_01(self):
        pass
    
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Case('test_01'))
    unittest.TextTestRunner().run(suite)
```

## 思路

- 框架工具 - UI自动化 - 使用方法 - PO模型

- 处理对象: 注册页面
- 配置文件 config.ini - configparser.ConfigParser [section] option=value