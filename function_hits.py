from selenium import webdriver
import time
import threading
# 优化版

# 定义后台运行浏览器驱动函数
def ConfigDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 以所谓的headless模式打开chrome
    return options

# 博客点击函数
def blog_hits():
    chrome = webdriver.Chrome(chrome_options=ConfigDriver())
    article_url = 'https://blog.csdn.net/z_ipython/article/details/'
    url_end = ['94449197', '94391460', '94356954', '94326201', '94297081', '94006620', '93647013', '93332794', '93300845',
         '93110641','92843270','92408758','92400819','92170504','90726626']
    # js代码，window代表浏览器对象，open方法用于打开一个新的浏览器窗口或查找一个已命名的窗口
    js = 'window.open("https://blog.csdn.net/z_ipython");'
    '''
    webdriver自带的2个调用javascript的方法:
        ①webdriver.execute_script(script,*args)  同步执行js代码
            如果JavaScript代码的执行时间较短，可以选择同步执行，因为Webdriver会等待同步执行的结果，然后再运行其它的代码
        ②webdriver.execute_async_script(script,*args)  异步执行js代码
            如果JavaScript代码的执行时间较长，可以选择异步执行，因为Webdriver不会等待其执行结果，而是直接执行下面的代码
    '''
    chrome.execute_script(js)
    for i in range(15):
        res = article_url + url_end[i]
        chrome.execute_script('window.open("{}");'.format(res))

        # print('window.open("{url}");'.format(url=res))

        time.sleep(2)
    # 退出驱动程序并关闭每个关联的窗口
    chrome.quit()

# 循环
def timework():
    while True:
        blog_hits()
        time.sleep(20)


if __name__ == "__main__":
    # 多线程任务处理
    t = threading.Thread(target=timework())
    t.start()
