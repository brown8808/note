# https://wikidocs.net/117435 트레이드 가이드



# apend	리스트에 추가
# del	리스트에서 삭제
# insert	리스트에 순서를 지정하여 추가
# 리스트[ ]	단어 묶음
# 튜플( )	수정 불가 리스트(리스트보다 메모리를 덜먹음)
# 인덱싱[0]	리스트나 튜플의 단어 가져오기
# 슬라이싱[0:4]	원하는 순서에 맞는 글자 가져옴
# int	정수
# float	실수
# str	문자
# dict	딕셔너리   # 딕셔너리는 순서가 없는 자료임 따라서 인덱싱이 안됨 오직 key를 통해서만 value에 접근 가능
# key	BTC
# value	8300000
# prices['BTC'] = 8300000	
# del prices['XRP']	
# price.keys()	key 값만 얻기
# price.value()	value 값만 얻기
# :	콜론
# if / elif / else	조건 추가
# >	비교 연산
# =	대입 연산
# ==	비교 연산
# for문	들여쓰기
# range(시작 값, 끝 값, 오프셋)	
# 파라미터 = 매개변수 /  외부로부터 투입되는 데이터

# 비교 연산자	의미
# ==	같다.
# !=	같지 않다.
# >	    크다.
# <	    작다.
# >=	크거나 같다.
# <=	작거나 같다.
	
# 논리 연산자	의미
# and	그리고
# or	또는
# not	~아닌


cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}

# for ticker, price in cur_price.items(): # for 문에는 key값과 value값이 포함되어 있음
#     print(ticker, price)

# for ticker in cur_price: # ticker 변수는 딕셔너리의 key값 중 하나를 바인딩
#     print(ticker, cur_price[ticker]) # ticker 변수가 바인딩하는 값과 cur_price 딕셔너리에서 ticker 변수가 바인딩하는 key에 대응되는 value 값을 화면에 출력

ripple = [511, 516, 508, 505, 503] # ripple 변수는 파이썬 리스트를 바인딩

# for close in ripple: # close는 파이썬 리스트의 값 중 하나를 바인딩
#     if close >=510:  # close >= 510 인지 조건을 확인
#         print(close) # 위의 조건들을 만족하는 경우 close가 바인딩한느 값을 화면에 출력

# while 조건문 : ~ 동안, 조건문을 만족하는 동안 수행문1, 2, 3을 계속 반복

# num = 1 # 변수가 정수 값 1을 바인딩
# while True: # 조건식을 만족하는지 확인, 그냥 True라고 적었으므로 항상 참
#     print(num) # 변수가 바인딩 하는 값을 출력
#     num = num + 1 # 한바퀴 돌때마다 num은 1씩 증가


# num = 1
# while True:
#     if num== 100 : num이 100과 같다면 정지
#         break
#     print(num)
#     num = num + 1

# num = 1
# while True:
#     num = num + 1
#     if num >= 10 : # 10보다 작은수는 출력하지 않음 11부터 +1씩 출력
#         print(num)

# num = 1
# for num in range(21):
#     print(num)
#     num = num + 1


# def hap(a, b): # 함수의 이름은 hap이고 함수는 a, b 라는 두 개의 입력값을 입력받습니다.
#     ret = a + b # 입력받은 a, b를 더한 값을 ret라는 변수가 바인딩합니다.
#     return ret # ret 변수가 바인딩하는 값을 함수 외부로 전달(리턴)합니다.

# result = hap(3, 4)
# print(result)

# def print_ohlc(open, high, low, close):
#     print("시가: ", open)
#     print("고가: ", high)
#     print("저가: ", low)
#     print("종가: ", close)

# print_ohlc(100, 120, 80, 90)

# def print_ohlc(ohlc):
#     print("시가: ", ohlc[0])
#     print("고가: ", ohlc[1])
#     print("저가: ", ohlc[2])
#     print("종가: ", ohlc[3])

# xrp_ohcl = (100, 120, 80, 90)
# print_ohlc(xrp_ohcl)

# 최소 주문 수량

# def get_min_order(ticker): # 문자열로 된 티커를 입력받음, 변수는 ticker
#     pass # 아직 함수의 기능을 생각해보지 않았기 때문에 pass라고 적음

# get_min_order("BTC")

# def get_min_order(ticker): # 함수 이름은 get_min_order이고 함수 인자는 한 개로 ticker라는 변수가 바인딩
#     get_min_order = None # min_order라는 변수는 아무 값도 없음을 의미하는 파이썬 타입인 None 타입 객체를 바인딩
#     if ticker == "ETC": # ticker라는 변수가 "ETC"라는 문자열을 바인딩하는지 확인
#         min_order = 0.1 # min_order라는 변수가 0.1이라는 float(실수) 객체를 바인딩
#     elif ticker == "ETH":
#         min_order = 0.5
#     elif ticker == "BTC":
#         min_order = 0.01
#     elif ticker == "XRP":
#         min_order = 10
#     else:
#         min_order = 0.005
#     return min_order # min_order 변수가 바인딩하는 값을 함수 외부로 출력(리턴)

# min_order = get_min_order("BTC")
# print(min_order)

# def mygop(a, b):
#     ret = a * b
#     return ret

# ret = mygop(3, 4)
# print(ret)

# 모듈을 불러올때는 '모듈명.함수이름'으로 호출
# import 모듈 / 모듈 불러오기
# import 모듈 as 새이름 / 모듈을 불러와 새 이름으로 정의
# from 모듈 import 함수 / 모듈을 불러와 코드를 간결하게 사용
# from 모듈 import * / 와일드 카드를 사용하여 모듈안의 모든 것(*)을 임포트하는 방식

# import datetime
# now = datetime.datetime.now()
# print(now)

# print(now + datetime.timedelta(hours=10)) # 현재 시간이 저장된 now 변수에 10시간을 더하는 코드
# print(now - datetime.timedelta(minutes=30)) # 30분 전의 시간을 계산



######### SSL 인증 오류 때문에 실행 불가능한 함수 #########

# 빗썸의 ticker API 결과값을 requests 모듈을 사용하여 가져오기
# import requests # 모듈을 사용하기 위해서 import
# resp = requests.get('https://api.bithumb.com/public/ticker/BTC') # requests 의 get() 함수로 전달한 URL의 웹페이지를 호출
# print(resp.content) # 콘솔에서 해당 내용을 확인 가능

# ch03/03_01.py
# pos = 0 # pos 변수는 슈퍼마리오의 위치를 저장

# def forward(pos): # forward() 함수는 슈퍼 마리오의 현재 위치를 입력받은 후 20만큼 이동한 위치를 리턴
#     return pos + 20

# pos = forward(pos) # forward() 함수를 호출하여 pos 값을 20 증가
# print(pos) # pos 변수가 바인딩하는 값을 출력


# 상기와 동일한 메서드이나 객체 지향 프로그래밍 방식의 코드


# ch03/03_02.py
# class SuperMario: # 라인 1~5: class라는 키워드를 통해 슈퍼 마리오 타입을 선언
#     def __init__(self): 
#         self.pos = 0
#     def forward(self):
#         self.pos = self.pos + 20

# mario = SuperMario() # 슈퍼 마리오 객체를 생성
# mario.forward() # forward() 메서드(함수)를 호출
# print(mario.pos) # 슈퍼 마리오의 현재 좌표를 출력

# 오락실에서 동전을 넣으면 슈퍼마리오가 생성되는 것처럼 mario = SuperMario() 타입의 객체를 생성
# mario.forward() 함수를 호출하여 생성된 슈퍼 마리오를 앞으로 이동함 /n 
# 슈퍼 마리오에 관련된 모든 것이 mario라는 변수를 통해서 이뤄지며 우리는 슈퍼 마리오 내부에 있는 위치값에 대해 신경 쓸 필요가 없음

# ch03/03_03.py
# p1_pos = 0
# p2_pos = 0

# def forward(pos):
#     return pos + 20

# p1_pos = forward(p1_pos)
# p2_pos = forward(p2_pos)

# 슈퍼 마리오 두 명이 필요하면 단순히 객체를 두번 생성하면됨

# ch03/03_04.py
# class SuperMario:
#     def __init__(self):
#         self.pos = 0
#     def forward(self):
#         self.pos = self.pos + 20

# mario_p1 = SuperMario()
# mario_p2 = SuperMario()
# mario_p1.forward()
# mario_p2.forward()

# 객체가 생성되었다면 앞으로 이동하는 메서드인 forward()를 호출할 수 있음
# 클래스는 데이터(pos = 0)와 함수(forward())를 묶어서 관리하는 것이 핵심

# a = 3 # a라는 변수는 int 객체 3을 바인딩
# print(type(a)) # a 변수가 바인딩하는 객체의 타입을 화면에 출력
# print(a.bit_length()) # bit_length() 메서드를 호출하여 a 변수가 바인딩하는 값인 3에 대한 비트 길이를 화면에 출력 = 2

# class는 데이터와 데이터를 처리하는 함수로 구성됨
# 문자열이라는 데이터에 대해서 이를 효과적으로 처리하기 위한 여러 함수 upper(), lower(), count()가 클래스 안에 정의되어 있음
# 따라서 우리는 점(.)을 찍고 upper()와 같이 쓸 수 있는 것
# b = 'python'
# print(type(b))
# print(b.upper())

# 클래스 정의 및 객체 생성
# class Myclass: # Myclass라는 이름의 클래스를 정의
#     pass

# obj = Myclass() # MyClass 타입의 객체를 생성하고 이를 obj라는 변수가 바인딩
# print(id(obj)) # obj 변수가 바인딩하는 객체의 주소를 화면에 출력

# class 붕어빵틀:
#     pass

# 붕어빵1 = 붕어빵틀()
# 붕어빵2 = 붕어빵틀()

# 클래스를 정의하는 행위는 붕어빵 틀을 만든 것과 유사, 붕어빵 틀은 여러번 붕어빵을 구울 수 있지만 붕어빵 틀을 사용해서 붕어빵을 구워야함
# MyClass는 붕어빵 틀, obj라는 변수는 틀에서 구워진 붕어빵을 가리키는데 이를 인스턴스, 객체, 오브젝트라고함

# ch03/03_05.py
# class MyClass: # MyClass를 정의
#     def method(self): # MyClass 안에 method라는 이름의 함수를 정의
#         print('method') # 화면에 출력

# obj = MyClass() # 객체 생성
# obj.method() # 함수 호출

# 메서드의 첫 번째 인자는 반드시 self라는 키워드를 사용해야함
# 클래스 안쪽에 들여 쓰기 된 함수를 메서드라고 부름

# ch03/03_06.py
# class MyClass:
#     def add(self, a, b):
#         return a + b

# obj = MyClass()
# ret = obj.add(3, 4)
# print(ret)

# 붕어빵에 팥소 넣기
# class 붕어빵틀: # 붕어빵틀 생성
#     def 팥소넣기(self, 팥소): # 팥소넣기라는 메서드를 정의
#         self.팥소 = 팥소 # 메서드 인자로 전달된 팥소를 self.팥소라는 변수가 바인딩

# 붕어빵1 = 붕어빵틀()
# 붕어빵2 = 붕어빵틀()

# 붕어빵틀.팥소넣기(붕어빵1, "초코맛팥소")
# 붕어빵틀.팥소넣기(붕어빵2, "딸기맛팥소")

# 붕어빵1.팥소넣기('초코맛팥소') # 이렇게 호출하면 알아서 인터프리터가 메서드를 변환해줌
# 붕어빵2.팥소넣기('딸기맛팥소')
# print(붕어빵1.팥소) # self.팥소 = 팥소
# print(붕어빵2.팥소) # self에는 어떤 붕어빵인지 구분하기 위한 값이 입력되고, 팥소에는 붕어빵에 넣고자 하는 팥소가 입력됨
# self 자리에 팥소를 넣고자 하는 객체(붕어빵1인지 붕어빵2인지)를 넘겨주고 팥소 자리에 '초코맛팥소'나 '딸기맛팥소'를 넘겨준 것을 확인
# 핵심! 어떤 클래스가 정의되면 해당 클래스 타입의 객체를 여러 개 만들 수 있음 이때 클래스 안에 정의된 메서드는 붕어빵 각각에 존재하는게 아니라 모든 붕어빵에서 공유할 수 있도록
# 클래스 내부에 있음

# class 붕어빵틀:
#     def __init__(self): # 언더바2개로 시작하는 이름은 특별한 의미 (초기화자), 첫 번째 인자는 self
#         self.팥소 = "초코맛팥소"


# ch03/3_07.py
# class Customer: # 해당 클래스를 정의
#     def __init__(self, id, name): # 초기화자에서 self, id, name을 입력받음
#         self.id = id # 초기화자로 입력된 id 값을 self 변수가 바인딩하는 객체의 id로 저장
#         self.name = name # 초기화자로 입력된 name 값ㅇ들 self 변수가 바인딩하는 객체의 name으로 저장

# Customer1 = Customer(1, "김은수")
# Customer2 = Customer(2, "이영희")

# class book:
#     def __init__(self, 책제목, 저자, 역자, 출판사, ISB10):
#         self.책제목 = 책제목
#         self.저자 = 저자
#         self.역자 = 역자
#         self.출판사 = 출판사
#         self.ISB10 = ISB10

# book1 = book(1, "금니")

# print(book1.책제목)

# ch03/03_08.py
# class Parent:
#     def sing(self):
#         print("sing a song")

# class LuckyChild(Parent):
#     pass
# class UnLuckyChild:
#     pass




# father = Parent() # Parent 클래스의 객체를 생성하고 이를 father라는 변수가 바인딩
# father.sing() # Parent 클래스의 sing() 메서드를 호출
# luckyboy = LuckyChild()
# luckyboy.sing()

# unluckyboy = UnLuckyChild()
# unluckyboy.sing()

# ch03/03_10.py
# class Parent:
#     def sing(self):
#         print('sing a song')

# class LuckyChild(Parent):
#     def dance(self):
#         print('shuffle dance')

# luckyboy = LuckyChild()
# luckyboy.sing()
# luckyboy.dance()

# 파이썬에서 주로 사용되는 GUI 모듈
# Tklnter
# wxPython
# PyQt

# class Car:
#     def __init__(self, model, year): # 초기화자는 클래스로부터 객체가 생성될 때 자동으로 호출됨
#         self.model = model
#         self.year = year

# # 클래스로부터 객체가 생성되면, 해당 객체는 고유의 메모리 공간을 갖음
# sonata = Car('SONATA', 2017)
# g80 = Car('G80', 2018)

# print(sonata.year, sonata.model)

# ch03/03_12.py
# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv) # QApplication 객체 생성
# label = QLabel('Hello')
# label.show()
# app.exec_() # 이벤트 루프 생성

#  PyQt로 프로그래밍을 작성할 때는 일반적으로 다음 두가지가 필요
# QApplication 클래스의 인스턴스
# 이벤트 루프 / 종료되지 않으려면 for문이나 While문이 필요한데 GUI 프로그램에서는 이를 '이벤트 루프'라고 함

# ch-3/3_13.py
# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)

# btn = QPushButton('Hello') # 버튼 객체 생성
# btn.show()

# app.exec_() # 이벤트 루프 생성

# 화면에 보이는 부분을 변경하고자 한다면 QApplication 객체를 생성한 후, 그리고 루프 생성 전에 코드를 작성하면 됨

# btn 과 같은 컴포넌트를 PyQt에서는 위젯이라고함 / 위젯은 사용자 인터페이스를 구성하는 가장 기본적인 부품 역할

# ch03/03_14.py
# import sys
# from PyQt5.QtWidgets import *

# class MyWindow(QMainWindow): # 최상위 위젯 윈도우를 위한 QMainWindow 클래스를 상속 / 윈도우 처음부터 만들기 어려움
#     def __init__(self):
#         super().__init__() # super()는 파이썬 내장함수

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()


# ch03/03_15.py
# import sys
# from PyQt5.QtWidgets import * # 파이큐티파이브에서 큐티위젯에 관한 모든 것을 임포트
# from PyQt5.QtGui import * # Qicon을 쓰기 위한 임포트

# class MyWindow(QMainWindow): 
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(100, 200, 300, 400) # 시작x, 시작y, 시작부터 가로, 시작부터 세로
#         self.setWindowTitle('PyQt5') # 실행시 윈도우 타이틀의 기본값은 'python'
#         self.setWindowIcon(QIcon('capture_start.png')) # 설정한 이미지를 아이콘으로 사용

#         btn = QPushButton("버튼1", self) # 버튼이 윈도우 위에 표시되길 원하니 윈도우 = self라는 변수가 바인딩 하고 있으므로 self를 넘겨주면 됨
#         btn.move(10, 10) # QPushButton 클래스의 move() 메서드를 사용하여 버튼의 위치 지정

#         btn2 = QPushButton('버튼2', self) # 버튼을 하나 더 생성
#         btn2.move(10, 40) # 추가로 생성한 버튼이 기존의 버튼과 같은 위치에 출력되지 않도록 위치를 move()메서드를 사용해 변경

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# ch03/03_19.py
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # 위젯 생성 코드
#         self.setGeometry(100, 200, 300, 200) # 위치, 크기 설정
#         self.setWindowTitle('PyQt') # WindowTitle 설정
#         self.setWindowIcon(QIcon('capture_end.png')) # WindowIcon 설정

#         btn = QPushButton('버튼1', self) # 버튼 객체 생성
#         btn.move(10, 10) # 버튼 위치 지정
#         btn.clicked.connect(self.btn_clicked) # 클릭 이벤트 생성 / 이벤트 루프가 메서드를 호출하는 것을 '콜백 함수'라고 부름

#     # 이벤트 처리 코드
#     def btn_clicked(self):
#         print('버튼 클릭')

# # QApplication 객체 생성 및 이벤트 루프 생성 코드
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# 파이썬에서 UI 파일을 읽어 윈도우를 출력해주는 코드를 구현
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5  import uic

# form_class = uic.loadUiType("window.ui")[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.inquiry) # 조회 버튼을 누르면 '조회 버튼 클릭' 이라는 문자열을 콘솔에 출력
#                                                       # MyWindow 클래스의 초기화자(init)에 clicked 이벤트 처리 코드를 추가 
#     def inquiry(self):
#         print('조회 버튼 클릭')
    

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# ch03/03_23.py
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# import pykorbit

# form_class = uic.loadUiType('window.ui')[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.inquiry)

#     def inquiry(self):
#         price = pykorbit.get_current_price('BTC') # pykorbit 모듈의 get_current_price() 함수를 호출 / 함수의 인자로 'BTC'를 넘겨주면 해당 현재가를 호출 / price 변수가 바인딩
#         self.lineEdit.setText(str(price)) # 호출한 price 변수를 위젯에 출력
#         print(price)

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# self.timer = QTimer(self)
# self.tiemer.start(1000)  # 인터벌을 1초로 설정
# self.timer.timeout.connect(self.timeout) # 1초에 한번 self.timeout()이라는 메서드를 호출


# def timeout(self):
#     cur_time = QTime.currentTime()
#     str_time = cur_time.toString('hh:mm:ss')
#     self.statusBar().showMessage(str_time)


# ch03/03_25.py
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.timer = QTimer(self)
#         self.timer.start(1000)
#         self.timer.timeout.connect(self.timeout)

#     def timeout(self):
#         cur_time = QTime.currentTime()
#         str_time = cur_time.toString('hh:mm:ss')
#         self.statusBar().showMessage(str_time)

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()


# ch03/03_26.py
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from PyQt5.QtCore import *
# import pykorbit

# form_class = uic.loadUiType('window.ui')[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        
#         self.timer = QTimer(self)
#         self.timer.start(1000)
#         self.timer.timeout.connect(self.inquiry)

#     def inquiry(self):
#         cur_time = QTime.currentTime()
#         str_time = cur_time.toString('hh:mm:ss')
#         self.statusBar().showMessage(str_time)
#         price = pykorbit.get_current_price('BTC')
#         self.lineEdit.setText(str(price))

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# BTC price 자동 호출

# PyQt는 위젯에 정의된 이벤트를 시그널(signal)이라고 부르고 이벤트가 발생할 때 호출되는 함수나 메서드를 슬롯(slot)이라고 부름

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# class MySignal(QObject): # 사용자 정의 시그널(clicked와 같은)을 만들기 위해 MySignal이라는 클래스를 정의
#     signal1 = pyqtSignal() # 그리고 해당 클래스에서 pyqtSignal 객체를 생성
# # 주의할 점은 pyqtSignal 객체를 인스턴스 변수로 만드는 것이 아니라 클래스 변수로 만들어야함
#     def run(self): # MySignal 클래스에는 run()이라는 메서드 = 내가 정의한 시그널인 'signal1'에서 emit() 메서드를 호출
#         self.signal1.emit() 

# class MyWindow(QMainWindow): 
#     def __init__(self):
#         super().__init__()

#         mysignal = MySignal() # MySignal 객체로부터 'signal1' 이벤트가 발생하면 이벤트 루프는 signal1_emitted()라는 메서드를 호출
#         mysignal.signal1.connect(self.signal1_emitted) 
#         mysignal.run() # run() 메서드를 호출 > emit() 메서드를 호출 > 그 순간에 'signal1' 이벤트가 발생

#     @pyqtSlot() # 이것은 데커레이터 : 간단하게 '시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다' 라고 이해 / 데커레이터는 말 그대로 '장식자'라는 의미로 메서드에 추가로 어떤 장식을 해둔 것
#     def signal1_emitted(self):
#         print('signal1 emitted')

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# class MySignal(QObject):
#     signal1 = pyqtSignal()
#     signal2 = pyqtSignal(int, int) # 'signal2'라는 객체를 만들었는데 이때 전달하고자하는 데이터 타입을 기술함

#     def run(self):
#         self.signal1.emit()
#         self.signal2.emit(1, 2) # 'signal2'라는 이름의 시그널을 발생할 때 정수 값 두 개를 같이 보낼 수 있다는 점 / emit() 메서드를 호출 후 시그널 발생 시 슬롯으로 값을 넘겨줌

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         mysignal = MySignal()
#         mysignal.signal1.connect(self.signal1_emitted)
#         mysignal.signal2.connect(self.signal2_emitted)
#         mysignal.run()

#     @pyqtSlot() # 슬롯은 시그널이 발생할 때 호출당하는 콜백 함수 / 이때 시그널로부터 데이터가 전송되기 때문에 이를 메서드의 인자를 통해 받아줌
#     def signal1_emitted(self):
#         print('signal1_emitted')

#     @pyqtSlot(int, int)
#     def signal2_emitted(self, arg1, arg2):
#         print('signal2 emitted', arg1, arg2)

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

# 우리가 하는건 스크래핑(특정한 데이터만을 웹사이트로부터 가져오는 행위)
# 이제 배울건 크롤링(다수의 정보를 가져오는 행위)
# HTML(HyperText Markup Language), CSS(Cascading Style Sheets), Javascript라는 3요소로 구성

# import requests

# url = 'http://www.naver.com'
# response = requests.get(url) # response 변수는 get() 함수의 반환 값인 Response 객체를 바인딩
# print(response.text) # Response 객체는 클래스이기 때문에 점을 찍으면 클래스의 메서드 또는 프로퍼티에 접근 가능

# ch04/04_01.py
# import requests
# from bs4 import BeautifulSoup
  
# url = "http://finance.naver.com/item/main.nhn?code=000660"
# html = requests.get(url).text
  
# soup = BeautifulSoup(html, "html5lib")
# tags = soup.select("#_per")
# tag = tags[0]
# print(tag.text)

# ch04/04_03.py
# import requests
# from bs4 import BeautifulSoup

# url = 'http://finance.naver.com/item/main.nhn?code=000660'
# html = requests.get(url).text

# soup = BeautifulSoup(html, 'html5lib')
# tags = soup.select('#_dvr')
# tag = tags[0]
# print(tag.text) # 이걸 위한 위의 모든 변수들

# ch04/04.py
# import requests
# from bs4 import BeautifulSoup

# def get_per(code):
#     url = 'http://finance.naver.com/item/main.nhn?code=' + code
#     html = requests.get(url).text

#     soup = BeautifulSoup(html, 'html5lib')
#     tags = soup.select('#_per')
#     tag = tags[0]
#     return float(tag.text)

# def get_dividend(code):
#     url = 'http://finance.naver.com/item/main.nhn?code=' + code
#     html = requests.get(url).text

#     soup = BeautifulSoup(html, 'html5lib')
#     tags = soup.select('#_dvr')
#     tag = tags[0]
#     return float(tag.text)
#     # 풀면 이렇게 됌? BeautifulSoup(requests.get('http://finance.naver.com/item/main.nhn?code=' + code).text,'html5lib').select('#_dvr').text

# print(get_per('000660'))
# print(get_dividend('000660'))

# ID가 지정되지 않은게 많으므로 아래의 형식으로 활용
# tag = soup.select('Copy selector 기입')

# https://api.korbit.co.kr/v1/ticker/detailed                                 코빗 RestfulAPI
# currency_pair=btc_krw                                                       필요 함수

# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw           함수 이름과 파라미터를 '?'로 연결하면 전체 주소
# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=xrp_krw           wnth Rmxqnqnsdp xrp 로 변경하면 리플의 현재가를 얻어옴

# 위를 딕셔너리로 변환


# import requests
# r = requests.get('https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw')
# print(r.text) # r.text 값은 딕셔너리처럼 보이지만 확인해보면 문자열 객체(str)임
# print(type(r.text))

# request의 get() 함수로 얻어온 데이터는 파이썬 딕셔너리처럼 생긴 문자열 타입으로 'JSON' 포맷이라고 함
# Response 객체는 json() 메서드를 호출하여 JSON 포맷의 데이터를 딕셔너리로 변환할 수 있음

# ch04/04_08.py
# import requests
# r = requests.get('https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw')
# bitcoin = r.json()
# print(bitcoin)
# print(type(bitcoin)) # class가 'dict'로 바뀐걸 확인 가능

# print(bitcoin['last'])

# timestamp 항복은 최종 체결 시각을 의미 / 1970년 1월 1일부터 지난 시간(초)을 의미

# ch04/04/09.py
# import requests
# import datetime

# r = requests.get('https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw')
# bitcoin = r.json()

# timestamp = bitcoin['timestamp'] # bitcoin 딕셔너리 객체에서 'timestamp'키를 통해 값을 얻어옴
# date = datetime.datetime.fromtimestamp(timestamp/1000) # fromtimestamp() 함수를 사용해서 timestamp 값을 datetime 객체로 변환
# print(date)

# t = date.strftime('%y/%m/%d %H:%M:%S')
# print(t)

# 판다스(Pandas)

# Pandas 모듈은 1차원 데이터를 다루는 Series 타입과 2차원 데이터를 위한 DataFrame 타입을 제공
# 1차원 데이터 Series는 한 행 또는 한 열에 있는 데이터

# from pandas import Series
# data = [100, 200, 300, 400] # data 라는 변수가 파이썬 리스트를 바인딩
# s = Series(data) # Series 객체가 생성. 생성된 Series 객체를 s라는 변수가 바인딩
# print(s) # 객체 출력
# print(type(s))

# 날짜별로 종가를 저장하기 위해서는 Series 객체를 생성할 때 index 파라미터롤 날짜를 넘겨주면 됨
# ch04/04_10.py
# from pandas import Series
# date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] # 각 날짜를 문자열로 표현하고 이를 리스트 객체로 만듬
# xrp_close = [512, 508, 512, 507, 500] # 리플의 종가를 리스트로 만듬
# s = Series(xrp_close, index=date) # 리플의 종가를 갖고 Series 객체를 생성하는데 이때 인덱스 값으로 날짜를 지정
# print(s)

# s 라는 변수는 Series 객체를 바인딩 / 출력된 값을 확인시 인덱스로 정숫값 대신 문자열로 표현된 날짜가 사용된 것을 확인 가능
# Seires 객체 생성시 index 파라미터를 따로 지정하지 않으면 데이터는 0부터 시작하는 정소 인덱스를 갖게됨
# index 파라미터를 지정했으므로 key-value 처럼 index-value라는 관계를 갖고 저장됨

# print(s[0])
# print(s['2018-08-01'])
# 따라서 이렇게 표현 가능

# ch04/04_11.py
# from pandas import Series

# date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
# xrp_close = [512, 508, 512, 507, 500]
# s = Series(xrp_close, index=date)

# print(s.index) # 인덱싱
# print(s.values) 
# print(s[[2, 4]])
# print(s[['2018-08-02', '2018-08-04']])
# print(s['2018-08-01': '2018-08-03']) # 슬라이싱
# print(s[0:2]) # 정수 인덱싱을 사용해 원하는 데이터만 슬라이싱

# from pandas import Series

# date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
# xrp_close = [512, 508, 512, 507, 500]
# s = Series(xrp_close, index=date)

# s['2018-08-06'] = 490 # 딕셔너리와 동일하게 추가할 Key에 값을 대입해서 Series에 데이터를 추가
# print(s.drop('2018-08-01')) # Series 클래스의 drop 메서드로 '2018-08-01' 키와 값을 삭제
# print(s)

# Series의 연산
# my_list = [100, 200, 300, 400]
# print(my_list / 10) # 리스트, 튜플, 딕셔너리는 저장된 값에 사칙연산을 직접 적용할 수 없음 / 에러 발생
# new_list = []
# for val in my_list:
#     new_list.append(val/10)

# print(new_list) # 새로운 리스트를 만들고 반복문을 사용하는 것 보다 쉬움 / 이것이 Pandas를 사용하는 이유
# 파이썬의 기본 자료 구조는 반복문을 사용해서 모든 값을 가져온 후에 나누기 연산을 적용하고, 그 결과를 새로운 리스트에 저장

# DataFrame 생성
# from pandas import DataFrame # 가로축과 세로축이 있는 2차원 데이터를 저장하는 자료구조
# data = {'open': [100, 200], 'high': [110, 210]} # data라는 변수는 파이썬 딕셔너리를 바인딩
# df = DataFrame(data)                            # DataFrame 객체가 생성되고 df 변수에 바인딩
# print(df)                                       # df라는 변수가 바인딩하는 객체의 타입을 출력
# 위 코드 실행시 두 개의 열과 두 개의 행으로 구성된 DataFrame 객체를 확인 가능 / 인덱스는 0부터 순차 증가하는 숫자로 자동 맵핑

# from pandas import DataFrame
# data = {'open': [737, 750], 'high': [755, 780], 'low': [700, 710], 'close': [750, 770]}
# df = DataFrame(data, index=['2018-01-01', '2018-01-02']) # DataFrame 객체를 생성할 떄, index 파라미터로 날짜(문자열 리스트)를 넘겨줌
# df.to_excel(r'C:\HH\ohlc-2.xlsx') # DataFrame 객체를 액셀로 저장하는 메서드
# print(df)

# import pandas as pd
# df = pd.read_excel(r'C:\HH\ohlc-2.xlsx') # 판다스가 제공하는 read_excel 함수는 엑셀 파일을 읽어 DataFrame 객체로 변환
# print(df)

# read_exel, to_exel

# ch04/04_20.py
# import pandas as pd
# url = 'https://finance.naver.com/item/sise_day.nhn?code=066570' # 이거 그냥 이사이트는 못가져옴 / 가져오는 방법 즐찾에 추가
# # df = pd.read_html(url) # 이건 에러뜸
# df = pd.read_html(url, encoding='cp949') # read 함수의 인자에 인코딩을 바꿔줌
# print(df[0])
# print(df[0].dropna(axis=0)) # 다음 코드에서 axis 값으로 0을 지정했기 때문에 0행 전체를 삭제 후 출력

# ch04/04_21.py
# from pandas import DataFrame
# data = {'open': [730, 750], 'high': [775, 780], 'low': [700, 710], 'close': [750, 770]} #  data 변수를 리스트로 지정
# df = DataFrame(data, index=['2018-01-01', '2018-01-02']) # 인덱스로 날짜 묶음
# print(df['open']) # open 키로 날짜별 벨류 가져오기
# print(df.loc['2018-01-01']) # DataFrame의 loc라는 특수한 메서드를 사용해서 하나의 행을 가져오기 / loc 메서드에 특정 인덱스를 넘겨주면 해당하는 행의 데이터가 Series로 반환
# print(df.iloc[0]) # iloc 메서드로 같은 값을 얻어올 수 있음

# DataFrame을 사용할 때 Series를 새롭게 생성해서 데이터를 추가하는 것 보다는 기존 데이터를 활용해서 데이터를 추가하는 일이 빈번하게 일어남
# ch04/04_23.py
# from pandas import * # 미리 생성된 DataFrame에 새로운 Column을 추가할 수도 있음 / Series 객체를 사용
# data = {'open': [730, 750], 'high': [775, 780],  'low': [700, 710], 'close': [750, 770]}
# df = DataFrame(data)
# s = Series([300, 400]) # DataFrame에 추가할 Series 객체를 생성
# df['volume'] = s # DataFrame에 volume 이란 이름으로 Series 객체를 추가함
# df.loc[2] = (100, 200, 300, 400, 500) # # 행을 추가할 때는 loc를 사용해서 행의 이름과 데이터를 튜플 혹은 리스트로 넘겨줌
# print(df)

# upper = df['open'] * 1.3 # DataFrame에서 open 이름의 열을 Series로 가져옵니다. open 열에 저장된 Series에 1.3을 모두 곱하고 upper 변수에 바인딩함
# df['upper'] = upper  # DataFrame에 upper 이름의 열을 추가

# print(df) # 인덱싱의 결과가 Series였음을 기억해야함 / Series 타입이기 때문에 곱하기 연산이 모든 데이터에 적용되고 그 결과 역시 Series임

# A칼럼에 100, 200, 300이 있는데 이를 한 줄 내려서 B칼럼에 저장하는 경우
# 이를 Pandas에서는 Series 객체에 있는 값을 시프트 하기 위해 shift 메서드를 사용
# ch04/04_25.py
# from pandas import Series

# s = Series([100, 200, 300])
# s2 = s.shift(1) # Series 객체의 값이 하나씩 밑으로 내려가 있음 / 값을 올릴려면 shift(-1)을 해주면 됨
# print(s)
# print(s2)

# from pandas import DataFrame
# data = {'open': [737, 750, 770], 'high': [755, 780, 770], 'low': [700, 710, 750], 'close': [750, 770, 730]}
# df = DataFrame(data, index=['2018-01-01', '2018-01-02', '2018-01-03'])
# print(df)

# from pandas import *
# data = {'open': [737, 750, 770], 'high': [755, 780, 770], 'low': [700, 710, 750], 'close': [750, 770, 730]}
# df = DataFrame(data, index=['2018-01-01', '2018-01-02', '2018-01-03']) # index 때문에 NaN으로 표시됨
# s = Series([55, 70, 20])
# df['volatility'] = s
# print(df)

#ch05/95_01.py
# import pykorbit
# import time
# tickers = pykorbit.get_tickers() # 티커 목록을 파이썬 리스트로 얻어옴
# print(tickers)
# print(len(tickers))
# price = pykorbit.get_current_price('BTC')

# while True:
#     print(price)
#     time.sleep(1)

# for ticker in tickers:  # 파이썬 for 루프 티커 리스트에서 티커를 하나씩 가져온 후 이를 ticker 변수가 바인딩함 
#     price = pykorbit.get_current_price(ticker) # get_current_price() 함수를 호출해 ticker 변수가 바인딩하는 가상화폐에 대한 현재가를 가져옴
#     print(ticker, price) # 티커와 현재가를 화면에 출력
#     time.sleep(0.1)

# 시가/고가/저가/현재가는 가상화폐의 방향성을 살펴볼 수 있는 대표적인 지표 거래서 모듈은 24시간 동안의 저가/고가/거래금액/거래량을 가져오는
# get_market_detail() 함수를 제공함 / get_market_detail() 함수의 파라미터로 조회할 티커를 넘겨주면 됨
# ch05/05_05.py
# import pykorbit

# detail = pykorbit.get_market_detail('BTC') # 순서대로 저가, 고가, 평균 거래 금액, 거래량임
# print(detail) # 저가, 고가, 평균 거래 금액, 거래량 / 튜플이기 때문에 인덱싱으로 각각의 데이터를 가져올 수 있음

# 매도 호가를 ask 매수 호가를 bid
# ch05/05_06.py
# import pykorbit

# orderbook = pykorbit.get_orderbook('BTC') # pykorbit 모듈로 호가 정보를 얻으려면 get_orderbook() 함수를 사용하면 됨
# print(orderbook)

# orderbook 딕셔너리에 저장된 키
# for k in orderbook:
#     print(k)

# timestamp = 1070/01/01 부터 지나간 시간 ms(milli second)를 의미함 ms = 1/1,000
# ch05/05/07.py
# import pykorbit
# import datetime

# orderbook = pykorbit.get_orderbook('BTC')
# ms = int(orderbook['timestamp']) # timestamp 메서드로 호가를 조회한 시간을 가져옴
# dt = datetime.datetime.fromtimestamp(ms/1000)
# print(dt)
# t = dt.strftime('%y/%m/%d %H:%M:%S')
# print(t)

# ch05/05_08
# import pykorbit

# orderbook = pykorbit.get_orderbook('BTC')
# bids = orderbook['bids']
# asks = orderbook['asks']
# print(bids)
# print(asks)

# for bid in bids:
#     price = bids[0]
#     quant = bids[1]
#     print('매수호가: ', price, '매수잔량: ', quant )
# 코빗에는 해당 메서드가 없나봄...

# ch05/05_09.py
# import pykorbit
# from item import *
# all = pykorbit.get_current_price('ALL')
# for k, v in all.items(): # Key와 Value값을 모두 가져오기
#     print(k, v)

# ch05/05_10.py
# import pykorbit

# all = pykorbit.get_current_price("ALL")
# for ticker, data in all.items() :
#     print(ticker, data(['closing_price']))

# 예외 처리
# ch05/05_12.py
# price = {'open': 100, 'high': 150, 'low': 90, 'close': 130}
# print('point-1')
# open = price['open1'] # keyError가 발생
# print('point-2') # 따라서 위의 라인에서 실행을 종료

# try:
#     open = price['open1']
# except:
#     pass # 서버가 불안정한 경우 일부 작업이 정상적으로 수행되지 않을 수 있으므로 특수한 상황(중요한 상황)에서의 에러처리를 해야함

# ch05/05_13.py
# import pykorbit
# import time
# 비트코인 현재가를 '0.2'초마다 조회한 후 현재가의 1/10을 출력하는 코드
# while True:
#     price = pykorbit.get_current_price('BTC')
#     print(price/10)
#     time.sleep(0.2)

# while True: # if 로 오류 대처
#     price = pykorbit.get_current_price('BTC')
#     if price is not None:
#         print(price/10)
#     time.sleep(0.2)

# while True: # try~except 로 오류 대처
#     price = pykorbit.get_current_price('BTC')
#     try:
#         print(price/10)
#     except:
#         print('에러발생', price)
#     time.sleep(0.2)

# ch05/05_14.py
# import pykorbit

# btc = pykorbit.get_ohlc('BTC') # 거래소 과거 시세
# print(btc)
# close = btc['close'] # DataFrame에서 'close'이름의 열을 close 변수에 바인딩
# print(close)
# close = btc['close']
# print((close[0] + close[1] + close[3] + close[4]) / 5) # 5일 이평선 구하기
# print((close[1] + close[3] + close[4] + close[5]) / 5)
# print((close[3] + close[4] + close[5] + close[6]) / 5)

# ch05/05_16.py
# import pykorbit
# Series는 rolling() 메서드와 mean() 메서드를 제공 / 해당 메서드를 사용하면 반복문을 사용할 필요 없이 모든 데이터의 이동평균을 자동으로 계산
# btc = pykorbit.get_ohlc('BTC')
# close = btc['close']
# window = close.rolling(5) # close의 rolling(5) 메서드를 호출해서 5일 윈도우를 설정 / 5일씩 모든 데이터를 그룹화
# ma5 = window.mean() # mean() 메서드는 그룹화된 값의 평균을 구함 / 계산된 결과는 Series로 ma5 변수에 저장
# print(ma5) # 데이터가 충분하지 않은 4일차까지의 앞부분에는 값없음(NaN)이 표시되지만 그 이후에는 정상적으로 출력됨
# ma5 = close.rolling(5).mean() # 이렇게 축약해서 사용 가능

# 상승장/하락장 구분하는 함수 구현
# 이평선은 5일 평균을 구한 것 = 마지막 5일자에 표시됨(따라서 지난 5일간의 기록이라 볼 수 있음)

# ch05/05_17.py
# import pykorbit
# df = pykorbit.get_ohlc('BTC')
# ma5 = df['close'].rolling(5).mean()
# last_ma5 = ma5[-2] # 끝에서 두 번째 위치한 전일 이동 평균을 last_ma5 변수에 바인딩
# price = pykorbit.get_current_price('BTC') # 비트코인의 현재가를 price 변수에 바인딩

# if price > last_ma5: # 현재가(price)와 5일 이동평균(last_ma5)를 비교
#     print('상승장')
# else:
#     print('하락장')

# 가상화폐별 상승장/하락장 판단하기
# import pykorbit

# def bull_market(ticker):
#     df = pykorbit.get_ohlc(ticker) # 티커별 오하로클을 df(데이터프레임) 변수로 바인딩
#     ma5 = df['close'].rolling(5).mean() # 티커별 5일 이평선을 ma5 변수로 바인딩
#     price = pykorbit.get_current_price(ticker) # 티커별 price를 price 변수로 바인딩
#     last_ma5 = ma5[-2] # 오늘 기준 전일 5일 이평선(ma5[-2])를 last_ma5 변수로 바인딩

#     if price > last_ma5:
#         return True
#     else:
#         return False

# is_bull = bull_market('BTC')
# if is_bull :
#     print('상승장')
# else:
#     print('하락장')

# tickers = pykorbit.get_tickers() # korbit에서 거래되는 모든 가상화폐의 티커 목록을 얻어옴
# for ticker in tickers: # 반복문을 사용해서 ticker 변수에 get_ticker() 함수로 얻은 티커를 하나씩 차례로 바인딩
#     is_bull = bull_market(ticker) # is_bull 변수가 True이면 '상승장' 문자열을 출력 그렇지 않으면 '하락장' 문자열을 출력
#     if is_bull:
#         print(ticker, ' 상승장')
#     else:
#         print(ticker, ' 하락장')

# ch05/05_20.py
# import sys
# import pykorbit
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from PyQt5.QtCore import * # QTimer 클래스를 사용하기 위해 PyQt5.QtCore를 임포트

# tickers = ['BTC', 'ETH', 'BCH', 'ETC']
# form_class = uic.loadUiType('bull.ui')[0] # loadUiType() 함수를 호출해서 Qt Designer로 생성한 bull.ui 파일을 로드함

# class MyWindow(QMainWindow, form_class): #QMainWindow와 form_class를 상속받아 MyWindow 클래스를 정의
#     def __init__(self): 
#         super().__init__()
#         self.setupUi(self)

#         timer = QTimer(self) # QTimer 클래스의 인스턴스를 생성
#         timer.start(5000) # start() 메서드를 호출하여 5초에 한 번씩 timeout 이벤트가 발생하도록 설정
#         timer.timeout.connect(self.timeout) # QTimer 객체에서 timeout 이벤트가 발생하면 MyWindow 클래스의 timeout() 메서드가 호출되도록 설정
    
#     def get_market_infos(self, ticker): # MyWindow 클래스에 get_market_infos() 메서드를 추가
#         df = pykorbit.get_ohlc(ticker) # 데이터프레임을 설정
#         ma5 = df['close'].rolling(window=5).mean() # df 변수중 close를 5일 이평선으로
#         last_ma5 = ma5[-2] # 5일 이평선 중 현재(-1)보다 하루 전의 이평선을 last_ma5로
#         price = pykorbit.get_current_price(ticker) # 각 티커별 가격을 변수로

#         state = None
#         if price > last_ma5: # 어제의 5일 이평선보다 현재의 가격이 높다면
#             state = '상승장' # state 칸에 상승장으로 표기
#         else:
#             state = '하락장' # 아니면 하락장

#         return price, last_ma5, state # 각 숫자 불러오기

#     def timeout(self): # 구현한 get_market_infos() 메서드를 timeout() 메서드에서 호출하여 5초마다 현재가, 5일 이동평균, 상승장/하락장 여부를 가져오도록 변경
#         for i, ticker in enumerate(tickers):
#             item = QTableWidgetItem(ticker) # timeout() 메서드에서 코인의 이름을 QTableWidgetItem 객체로
#             self.tableWidget.setItem(i, 0, item)

#             price, last_ma5, state = self.get_market_infos(ticker) # 얻어온 데이터는 QTableWidgetItem객체로 만든 후 이를 QTableWidget에 추가
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price))) # 주의할 점은 얻어온 데이터 중 문자열이 아닌 값은 먼저 문자열로 변환 후에 ㅃTableWidgetItem의 생성자로 전달
#             self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
#             self.tableWidget.setItem(i, 3, QTableWidgetItem(str(state)))

    

# app = QApplication(sys.argv)
# win = MyWindow() # MyWindow 객체를 생성
# win.show() # MyWindow 클래스의 show() 메서드로 윈도우를 화면에 그림
# app.exec_() 
# 이 GUI는 버벅댐 이유는 파이썬 인터프리터가 현재가를 조회하고 화면에 GUI를 그리는 과정이 복잡하거나 네트워크 지연이 발생하기 때문
# 이를 보완한 PyQt5의 QThread 클래스를 사용해보자

# ch05/05_24.py
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import * # QtCore 모듈 내의 모든 내용을 import

# class Worker(QThread): # QThread 를 상속받아 Worker 클래스를 정의 / QThread 클래스는 PyQt5.QtCore 모듈에 정의되어 있음
#     def run(self):  # 스레드가 실행될 때 수행할 코드를 run() 메서드에 작성 / # self는 클래스의 인스턴스임 까먹지 말자
#         while True:
#             print('안녕하세요')
#             self.sleep(1)

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.worker = Worker() # worker 클래스의 객체를 생성
#         self.worker.start() # start() 메서드를 호출하면 Worker 클래스의 run() 메서드를 호출함 즉 start() 메서드를 호출하는 것만으로 Worker 클래스의 run() 메서드가 실행됨

# app = QApplication(sys.argv)
# mywindow = MyWindow()
# mywindow.show() 
# app.exec_()
# 코드를 실행하면 MyWindow 클래스의 객체가 생성되는데 이때 Worker 클래스의 객체가 생성되면서 run() 메서드의 코드가 실행됨

# ch05/05_26.py
import sys
import pykorbit
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

tickers = ['BTC', 'ETH', 'BHC', 'ETC']
form_class = uic.loadUiType('bull.ui')[0]

class Worker(QThread): # QThread를 상속받아 Worker 클래스를 정의
    finished = pyqtSignal(dict) # Worker 스레드는 지금까지 사용했던 PyQt의 기본 위젯과 달리 사용자가 정의한 클래스이므로 이벤트 역시 사용자가 직접 정의 가능
# finished 라는 이름으로 이벤트(시그널) 객체를 생성 / 시그널이 발생할 때 슬롯으로 딕셔너리 객체가 전달됨
    def run(self): # run() 메서드를 정의함 run()메서드는 이름을 변경하지 않아야함
        while True:
            data = {}

            for ticker in tickers: # 각 티커에 대해서 get_market_infos() 메서드를 호출해서 현재 티커에 대한 현재가, 5일 이평, 상승장/하락장 튜플 객체를 딕셔너리에 저장함
                data[ticker] = self.get_market_infos(ticker) # 이때 티커가 딕셔너리의 key가 됨

            self.finished.emit(data) # finished라는 시그널이 발생하면 self.update_table_widget() 메서드가 호출되도록 설정       
            self.msleep(500) # 사용자 정의 시그널을 발생시킴 이때 data 변수가 바인딩하고 있는 딕셔너리 객체를 전달함
            # 스레드를 0.5초 슬립

    def get_market_infos(self, ticker): # MyWindow 크래스에 있던 get_market_infos() 메서드를 Worker 클래스로 옮겨줌 
        try: # get_market_infos() 메서드를 호출하여 현재 티커에 대한 (현재가, 5일 이평, 상승장/하락장) 데이터로 구성된 튜플 객체를 딕셔너리에 저장
            df = pykorbit.get_ohlc(ticker) 
            ma5 = df['close'].rolling(window=5).mean()
            
            price = pykorbit.get_current_price(ticker)
            last_ma5 = ma5[-2]

            state = None
            if price > last_ma5:
                state = '상승장'
            else:
                state = '하락장'

            return (price, last_ma5, state)
        except:
            return (None, None, None) # 이때 예외 처리를 위한 코드를 추가

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setRowCount(len(tickers))
        self.worker = Worker() # MyWindow 클래스의 객체가 생성될 때 Worker 클래스의 객체를 생성하고  start() 메서드를 호출
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    @pyqtSlot(dict) # 딕셔너리 객체가 받을 수 있는 슬롯임을 지정
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.item(): # data에는 딕셔너리가 바인딩돼 있는데, key와 value를 가져온 후 for 문을 돌림
                index = tickers.index(ticker) # 티커 리스트에서 티커가 위치하는 인덱스를 얻어옴 / 얻어온 인덱스는 QTableWidgetItem 객체를 QTableWidget 객체에 추가할 때 행(row) 인덱스로 사용됨

                self.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))

        except:
            pass
               


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()






