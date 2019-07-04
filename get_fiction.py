from time import sleep
from selenium import webdriver

# 定义爬取小说函数
def get_fiction(url):
    chrome = webdriver.Chrome()

    chrome.get(url)
    titles = chrome.find_element_by_css_selector("body > div.reader-main > div.paper-box.paper-article > h1").text
    print(titles)
    texts = chrome.find_elements_by_xpath("//div[@id='contentWp']")
    for t in texts:
        content = t.text
        # print(t.text)
    sleep(2)
    url_a = chrome.find_elements_by_xpath("//a[@class='next']")
    if url_a:
        with open("xiaoshuo.txt","a",encoding="utf-8") as f:
            f.write('\n'.join([titles,content]))
            f.write('\n\n')

        a = url_a[0].get_attribute("href")
        get_fiction(a)
    else:
        chrome.close()
        return
    # for a in url_a:
    #     print(a.get_attribute("href"))


get_fiction("https://xiaoshuo.sogou.com/chapter/8739377987_286371239440388/")



