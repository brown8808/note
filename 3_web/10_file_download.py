from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 저장 경로 지정을 위한 임포트

chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'C:\HH'})  # 원하는 경로에 저장하기 위한 

import time
browser = webdriver.Chrome(options=chrome_options) # 평소와 달리 뒤에 괄호안에 옵션스를 넣어줌
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
browser.maximize_window()

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()