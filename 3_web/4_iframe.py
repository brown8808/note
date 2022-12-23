import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # 프레임 전환

elem = browser.find_element(By.XPATH, '//*[@id="html"]') # 전환된 프레임에 대한 실행
elem.click()

browser.switch_to.default_content() # 다시 상위로 빠져나옴


time.sleep(5) # 5초 대기
browser.quit()




# //*[@id="html"]

