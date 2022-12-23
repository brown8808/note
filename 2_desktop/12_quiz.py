import pyautogui
import sys
import pyperclip


pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 누르기


# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1번째것만 가져오기
if window.isMaximized == False:
    window.maximize() # 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# # 흰 영역 클릭
# pyautogui.click(200, 200, duration=0.5)

btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200) # 고정된 이미지를 찾은 후 상대좌표를 통해 클릭

def my_write(text):  # 함수 제작
    pyperclip.copy(text) # 파이퍼 클립을 이용해 특정 텍스트 복사
    pyautogui.hotkey("ctrl", "v") # 복사한 텍스트를 핫키를 이용해 붙여넣기


my_write("참 잘했어요") 



# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음

# 항상 confidenc=0.8 < 정확도를 낮춰서 이미지를 찾는 방법을 활용
# 이미지 찾기보다는 단축키 활용을 무조건 추천!
