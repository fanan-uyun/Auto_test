from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# 简易版

def ConfigDriver():
    options = Options()
    options.add_argument('--headless')  # 以所谓的headless模式打开chrome
    return options


def BuildDriver():
    return webdriver.Chrome(chrome_options=ConfigDriver())


def hits():
    chrome = BuildDriver()


    chrome.get("https://blog.csdn.net/z_ipython")


    url_a = chrome.find_element_by_css_selector("#mainBox > main > div.article-list > div:nth-child(2) > h4 > a").click()
    # print(url_a.get_attribute("href"))


    chrome.close()


# xpath://*[@id="mainBox"]/main/div[2]/div[2]/h4/a
# css选择器 :nth-child(n) 选择器匹配父元素中的第 n 个子元素

for i in range(100):
    hits()