import pyautogui

#마우스 이동
pyautogui.moveTo(200, 100) # 지정한 위치(가로x, 세로y)로 마우스를 이동
pyautogui.moveTo(100, 200, duration=0.5) # 0.5초 동안 100, 200 위치로 마우스를 이동


# pyautogui.moveTo(100, 100, duration=0.25)

# 상대 좌표로 이동 (현재 커서가 있는 위치로부터)
# pyautogui.move(100, 100, duration=0.5)
# print(pyautogui.position()) #  point (x, y)

p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y   <- 위와 똑같이 좌표 출력

