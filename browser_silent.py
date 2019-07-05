from selenium import webdriver

# 实例化谷歌浏览器设置选项
browser_option = webdriver.ChromeOptions()

# 添加启动参数，设置浏览器静默模式，不弹出浏览器，后台运行
# browser_option.add_argument('headless')
# browser_option.add_argument('--headless')
# browser_option.add_argument('--disable-gpu')
# 隐藏‘Chrome正在受到自动软件的控制’提示
browser_option.add_argument('disable-infobars')

# 浏览器实例化，并将选项传给浏览器
browser = webdriver.Chrome(chrome_options=browser_option)

# 访问页面
browser.get("https://www.baidu.com")

# 关闭浏览器
browser.close()
