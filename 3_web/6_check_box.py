import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
browser.switch_to.frame('iframeResult') # frame 전환시 목적 XPATH 상위 iframe 에서 neame-"~~~~" < 이 부분 우클릭 후 복사

# elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]') # frame 전환
elem = browser.find_element(By.ID, 'vehicle1') # ID 로 접근 가능

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()

else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)

browser.quit()
