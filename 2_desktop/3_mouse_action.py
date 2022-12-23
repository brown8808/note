# -*- coding: utf-8 -*-

import pyautogui
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())


# pyautogui.click(64, 17) # 해당 좌표를 마우스 클릭
# pyautogui.mouseDown()
# pyautogui.mouseUp()  # 이걸 합친게 mouseclick()

# pyautogui.doubleClick() # 더블클릭
# pyautogui.click(clicks=30) # 더블, 혹은 다중 클릭으로 활용 가능


# # 드레그를 위한 이벤트
# pyautogui.moveTo(100, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(200, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태
# pyautogui.drag(100, 0) #현재 위치 기준으로 100, 0 만큼 이동 *빠른 동작으로 drag 수행이 안될때는 duration으로 시간 설정
# pyautogui.dragTo(200, 300, duration=0.5) #절대 좌표 기준으로 드레그

# pyautogui.rightClick() # 우클릭

# # 스크롤을 위한 이벤트
# pyautogui.middleClick() # 스크롤
pyautogui.scroll(-300) # 양수는 위 방향으로, 음수면 아래 방향으로 300만큼 스크롤

