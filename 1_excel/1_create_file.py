from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴
ws.title = "new~" # sheet 의 이름을 변경
wb.save("sample.xlsx") # 시트 저장
wb.close() #시트 닫음

