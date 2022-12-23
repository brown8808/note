import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png") # 해당 파일을 활용하여 화면에 일치하는 좌표를 탐색
#print(file_menu) # 해당 좌표를 반환
pyautogui.click(file_menu) # 해당 좌표를 클릭

# edit_menu = pyautogui.locateOnScreen("edit_menu.png")
# pyautogui.click(edit_menu)

#print(edit_menu) # 해당 이미지를 못찾으면 "None" 으로 반환

# w3 schoolscheckbox 검색 후 try in yourself 클릭

#  같은 이미지 모두 클릭 원할시!
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=1)



#### 속도 개선 ####
# 1. GrayScale 흑백전환 후 비교(약 30퍼센트 정도 개선)

# edit_menu = pyautogui.locateOnScreen("edit_menu.png",grayscale=True)
# pyautogui.click(edit_menu)

# 2. 범위 지정

# edit_menu = pyautogui.locateOnScreen("edit_menu.png", region=(x, y, whdth, heigth))
# pyautogui.click(edit_menu)
# pyautogui.mouseInfo()

# 3. 정확도 조정
# edit_menu = pyautogui.locateOnScreen("edit_menu.png", confidence=0.9) #90%
# pyautogui.click(edit_menu)

# 자동화 대상이 바로 보여지지 않는 경우

# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
# import time
# import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# def find_target(img_file, timeout=30):
#     start = time.time()
#     target = None
#     while target is None:
#         target = pyautogui.locateOnScreen(img_file)
#         end = time.time()
#         if end - start > timeout:
#             break
#     return target

# def my_click(img_file, timeout=30):
#     target = find_target(img_file, timeout)
#     if target:
#         pyautogui.click(target)
#     else:
#         print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate program.")
#         sys.exit()

# # pyautogui.click(file_menu_notepad)

# my_click("file_menu_notepad.png", 10)


