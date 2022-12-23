import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate() # 띄운 메모장을 바로 입력할 수 있게 활성화

# pyautogui.write("12345") # 활성화된 메모장에 입력
# pyautogui.write("NadoCoding", interval=0.2)

# pyautogui.write("나도코딩") # 한글 입력이 안됨

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.3)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, la 순서대로 적고 enter 입력
# automatetheboringstuff with python 구글링 후 챕터 20 들어간 후 ctr + f attri 검색하면 다 보임

# 특수 문자
# # shift 4 - > $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다.

# 조합키 (Hot Key) ctrl + a
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# # 간편한 조합키
# pyautogui.hotkey("ctrl", "a") 

#### 한글 입력 ####
import pyperclip
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 단어를 붙여넣기

def my_write(text):  # 함수 제작
    pyperclip.copy(text) # 파이퍼 클립을 이용해 특정 텍스트 복사
    pyautogui.hotkey("ctrl", "v") # 복사한 텍스트를 핫키를 이용해 붙여넣기


my_write("오늘 수업 끝~~~!") # 결과물

# 자동화 프로그램 종료
# ctrl + alt + del 