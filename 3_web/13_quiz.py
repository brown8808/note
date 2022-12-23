from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys # 엔터키를 누르기 위한 임포트?

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/') # 해당 사이트의 브라우저 오픈

# browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click() # "Learn HTML"을 클릭
# browser.find_element(By.LINK_TEXT, 'Learn HTML').click() # 텍스트를 찾아서 클릭 
# browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[text()="Learn HTML"]').click() # 텍스트가 다수일 경우 제일 확실한 방법 xpath 찾아서 그 태그안에서 text값을 가져옴 가장 베스트
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[contains(text(), "Learn")]').click() # 특정 단어를 포함하는 텍스트를 선택하는 방법

time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()
time.sleep(1)

first_name = "나도"  # 이런식으로 변수 저장으로도 입력 가능


browser.find_element(By.NAME, 'firstname').send_keys("나도")

browser.find_element(By.NAME, 'lastname').send_keys("코딩")

browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="Canada"]').click()

time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys("퀴즈를 완료하였습니다.")
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()


time.sleep(3)
browser.quit()



