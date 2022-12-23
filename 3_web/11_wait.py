from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




browser = webdriver.Chrome()
browser.get('https://flight.naver.com/')
browser.maximize_window()


# 가는날 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(1)
# browser.find_elements(By.LINK_TEXT('가는날 선택')).click()

# 가는 날 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/button').click()
# browser.find_elements(By.LINK_TEXT, '1'[1]).click()
time.sleep(1)

# 오는 날 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/button').click() 
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click() # 제주 선택

time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click() # 항공권 검색 클릭
# browser.find_element(By.LINK_TEXT, '항공권 검색').click()

# 로딩을 기다리는 방법
# time.sleep(10) # 이건 너무 김



try: 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')))
    print(elem.text)
except:
    print("실패했어요")



# 첫 번째 결과 출력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')c
# print(elem.text) # element 내에 있는 text 부분을 출력


# time.sleep(2)
# browser.quit()