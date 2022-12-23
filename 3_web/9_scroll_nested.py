from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()



# 방법 2 : 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지 마세요
# print("type : ",type(xy)) # dict
# print("value : ", xy)

# 스크롤 하지 않아도 클릭은 됨

elem.click()

time.sleep(5)
browser.quit()