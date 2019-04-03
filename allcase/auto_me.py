# __Author:HYH
# DATE:2019/4/3

from appium import webdriver
import time

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'X2P0215714000990',  # 设备ID 使用adb devices 查看
                'platformVersion': '5.1',  # 系统版本
                'appPackage': 'com.ultrapower.android.me.ry',  # 包名
                'appActivity': 'com.ultrapower.android.login.SplashActivity'  # 入口Activity
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(5)  # app启动后等待5秒，方便元素加载完成

size = driver.get_window_size()
width = size['width']
height = size['height']

# login
# 输入帐号
driver.find_element_by_id('com.ultrapower.android.me.ry:id/login_account_auto').clear()
driver.find_element_by_id('com.ultrapower.android.me.ry:id/login_account_auto').send_keys('xmhuyaohui')
# 输入密码
driver.find_element_by_id('com.ultrapower.android.me.ry:id/login_password_et').clear()
driver.find_element_by_id('com.ultrapower.android.me.ry:id/login_password_et').send_keys('hyh2019')
# 登录用户
driver.find_element_by_id('com.ultrapower.android.me.ry:id/login_btn_text').click()
time.sleep(5)

# card
# 点击应用
driver.find_element_by_id('com.ultrapower.android.me.ry:id/bottomBar2').click()
time.sleep(1)
# 点击“常用-第一个应用”，进入应用页面
driver.find_element_by_id('com.ultrapower.android.me.ry:id/appLogo').click()
time.sleep(3)
# 点击“play card”
driver.find_element_by_id('com.ultrapower.android.me.ry:id/tvmenu').click()
time.sleep(4)
# 点击最上角返回按钮，返回至应用主页
driver.find_element_by_id('com.ultrapower.android.me.ry:id/ivBack').click()
time.sleep(1)

# logout
# 点击“更多”
driver.find_element_by_id('com.ultrapower.android.me.ry:id/bottomBar4').click()
time.sleep(1)
# 向上滑动页面
driver.swipe(width*0.5, height*0.9, width*0.5, height*0.3)
time.sleep(1)
# for i in range(2):    # 增加滑动次数，因为有时滑动不明显。这一步很有效果。2可以是更改的，如果滑动的少，可以增加滑动次数的。
#     print(i)
#     time.sleep(5)
#     driver.swipe(x1, y1, x1, y2)
# 点击“退出当前帐号”
driver.find_element_by_id('com.ultrapower.android.me.ry:id/btn_exit').click()
time.sleep(1)
# 确认退出
driver.find_element_by_id('com.ultrapower.android.me.ry:id/yes').click()
time.sleep(2)
driver.quit()
