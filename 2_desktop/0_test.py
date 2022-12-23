import pyautogui
import pygetwindow as gw

for win in gw.getAllTitles():
    print(win)


# for win in pyautogui.getAllWindows(): # 모든 윈도우 정보 가져오기
#     print(win)

# for win in pyautogui.getWindowsWithTitle('쿠팡플렉스'): # 타이틀에 '쿠팡플렉스' 를 포함하는 모든 윈도우 정보 가져오기
#     print(win)

