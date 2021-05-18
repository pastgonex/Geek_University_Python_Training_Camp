from selenium import webdriver
import time

global browser
try:
    browser = webdriver.Chrome()  # 找到chromedriver.exe, 然后通过他拉起Chrome浏览器
    # 需要安装 chrome driver, 和浏览版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://www.douban.com')
    time.sleep(1)

    # switch_to_frame 已经弃用 改为 switch_to.frame()
    browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('10086@qq.com')
    browser.find_element_by_id('password').send_keys('QQ10086')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    browser.close() # 最后关闭浏览器
