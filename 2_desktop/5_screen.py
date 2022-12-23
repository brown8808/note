# -*- coding: utf-8 -*-

import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot() # 스크린샷 캡쳐
# img.save("screenthot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 386,255 30,30,30 #1E1E1E

pixel = pyautogui.pixel(386, 255)
print(pixel)

# print(pyautogui.pixelMatchesColor(386, 255, (30,30,30))) # RGB 값이 같은지 체크
print(pyautogui.pixelMatchesColor(386, 255, pixel))

