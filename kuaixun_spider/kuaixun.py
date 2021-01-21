# _*_  coding:utf-8  _*_
# @ 功能描述：爬一下网页链接
# @ Time： 2021/1/20 16:25
# @ 作者：yagami_yue
# @ 版本信息：0.0.1
import re

from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    baseurl = "https://kuaixun.eastmoney.com/yw.html"
    # driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe")
    driver = webdriver.Chrome()
    driver.get(baseurl)
    for i in range(20):
        web_soup = BeautifulSoup(driver.page_source, "lxml")
        pat_link = re.compile('<a class="media-title" href="(.*?)">')
        # print(web_soup)
        soup = web_soup.prettify()
        # print(soup)
        for item in pat_link.findall(soup):
            print(item)
            with open('url.txt', 'a') as f:
                f.write(item)
                f.write('\n')
        next_page = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/a[8]')
        next_page.click()









