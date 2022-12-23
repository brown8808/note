from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터키를 누르기 위한 임포트?


# browser = webdriver.Chrome("./chromedriver.exe") # 위치에 있는 크롬 드라이버를 사용하여 제어
browser = webdriver.Chrome() # 같은 경로에 있으므로 경로 지정 없이도 크롬을 제어

browser.get("http://naver.com") # 해당 주소의 크롬창을 생성

# elem = browser.find_element_by_lik_text("카페")
# elem


elem = browser.find_element(By.LINK_TEXT, "카페") # 원하는 엘리먼트 지정
# elem

elem.get_attribute("href")
elem.get_attribute("class")

elem.click() # 클릭 
# browser.back() # 뒤로가기
# browser.forward() # 앞으로 가기
# browser.refresh() # 새로고침

# elem = browser.find_element(By.ID, "query") # 네이버 검색창에
# elem.send_keys("나도코딩") # 나도코딩 글자입력
# elem.send_keys(Keys.ENTER) # 엔터
# elem = browser.find_element(By.TAG_NAME, "a") # 원하는 품목 선택
# elem = browser.find_elements(By.TAG_NAME, "a") # a 태그를 포함하는 엘리먼트를 모두 가져오기

# for e in elems:
#     e.get_attribute("href") # 태그 다 가져오기


browser.get("http://daum.net")
elem = browser.find_element(By.NAME, "q") # 네임이 지정된 경우 네임으로 가져오기
elem.send_keys("나도코딩")
elem.clear()
elem.send_keys("오우예아")
elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()
browser.save_screenshot('daum.png')
browser.close()
browser.quit()

# SeleniumWithPython 구글링하면 다나옴