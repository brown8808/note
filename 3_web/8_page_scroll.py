import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 엔터키를 누르기 위한 임포트?

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home')

# '무선마우스' 입력
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div[1]/input').send_keys('무선마우스')

# 검색 버튼 클릭
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/button[2]/svg/path').click() # 안되네...

elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input') # 엘리먼트를 나눠서..
elem.send_keys('무선마우스') # '무선마우스' 입력

time.sleep(1) # 글자 입력하자마자 클릭이 안된다면 슬립 1초정도 적용

elem.send_keys(Keys.ENTER) # 검색 버튼 클릭을 우회한 ENTER 처리

# 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)') # 1920 * 1080 <- 내모니터 해상도인데 세로로 1080 만큼 내린다는 뜻..! (1page 정도 화면만큼 내리는것)
# browser.execute_script('window.scrollTo(0, 2080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

#### 동적 페이지에 대해서 마지막까지 스크롤 반복 수행 ####
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

time.sleep(interval)

# 반복 수행
while True: # 무한 반복
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면
        break # 반복문 탈출 (모든 스크롤 동작 완료)

    prev_height = curr_height # 지금 높이를 과거 높이에 저장



# 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')


time.sleep(5)
browser.quit()