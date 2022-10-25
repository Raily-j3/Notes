# Appium

- Android
- SDK，Java，adb，Client - Server - Device
- 定位：id, class, name, index
- 操作：点击，输入，长按，滑动，多点触控

## adb常用命令

``` cmd
adb version
adb tcpip 5555                 # 用 USB 连接后 在使用同一局域网WIFI连接 adb connect <IP>
adb connect					   # 夜神PORT 62001 62025 + n
adb devices					   # 连接设备列表
adb -s [IP]:[PORT] shell  		# exit -s: select
adb install ${PATH}.apk
adb uninstall {package_name} 	# /data/app 不带 -1; -k: 保留配置缓存
adb push/pull {src} {dst}	    # 上传/下载 文件
adb shell pm list package       # 安装包列表
adb shell screencap / 		   # 屏幕截图
adb start-server/kill-server    # 服务的启动/关闭
netstat -ano | findstr "5037"  # 查看端口占用情况 
```

## aapt命令 ( Android Asset Package Tool)

- activity ≈

```cmd
aapt dump badging xxx.apk | findstr "launchable-activity"
```

## appium 必要依赖

- Node.js
- Appium
- Appium-Python-Client
- JDK
- Android SDK

## 常用Capability ( 需要自动化的平台和应用 )

- platformName
- platfromVersion
- deviceName
- app
- udid
- noReset
- appPackage
- appActivity
- appMaitActivity

## 定位

- id
- name
- class
- List定位
- 相对定位
- Xpath定位
- UIaotomator定位
  - driver.find_element_by_android_uiautomator('new UiSelector().resourceId("xxx")')
- H5页面元素定位
  - 混合开发 app 的 H5 页面不能进行 uiautomator 定位（只能定位原生元素）
  - context
  - WebView
  - contexts = driver.contexts
  - print(contexts)
  - driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
- Toast
  - cnpm install appium-uiautomator2-driver
  - desired_caps['automationName'] = 'uiautomator2'
- FrameLayout
- LinearLayout
- RelativeLayout
- AbsoluteLayout
- TableLayout
- TextView
- ImageView

## 元素等待

- sleep
- 隐式等待：driver.implicitly_wait
- 显示等待：from selenium.webdriver.support.ui import WebDriverWait
  - WebDriverWait(driver, {sec}).until(lambda x:x.find_element_by_id('xxx')

## 滑动操作

- 获取尺寸：get_size 

  - x = driver.get_window_size()['width']
  - y = driver.get_window_size()['height']

- 两点之间的滑动：driver.swipe(x1,y1,x2,y2,1000)

- 连续滑动：TouchAction

- from appium.webdriver.common.touch_action import TouchAction

  - press(x, y)
  - longpress(x, y, duration)
  - tap(x, y)
  - move_to()
  - wait(ms)
  - release()
  - perform()

## 多点触控

  - MultiAction
  - from appium.webdriver.common.multi_action import MultiAction
  - MultiAction.add(*touch_action).perform()

## 坑

- 找不到元素，页面转换需要等待一定时间。
- 同 id 有多个元素。。。
- 

## 常用方法

``` python
from appium import webdriver

driver = webdriver.Remote(URL, desired_capabilities)

# 元素定位, 操作
xx_btn = driver.find_element(self, by, value)
xx_text = driver.find_element_by_id(value)
xx_btn.click()
xx_text.send_keys('xxx')

# 滑动屏幕
driver.get_window_size()[width]
driver.swipe(x1, y1, x2, y2, sec)
driver.get_screenshot_as_file(file_path)


```





## Monkey



- 