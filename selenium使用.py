from selenium import webdriver
# 实例化浏览器驱动
chrome = webdriver.Chrome()
# 访问页面
chrome.get("http://www.baidu.com")
# 获取输入框元素
inputs = chrome.find_element_by_id("kw")
# 获取“”百度一下按钮元素
button = chrome.find_element_by_id("su")
# 对元素进行操作，给输入框传入搜索内容
inputs.send_keys("python")
# 对元素进行操作，进行点击
button.click()
# 关闭浏览器
chrome.close()

