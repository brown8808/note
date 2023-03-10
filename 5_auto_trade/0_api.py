# API 클래스 객체
# ch06/06_01.py

# import pybithumb
# import time
# con_key = "###" # API 신청 페이지에서 발급받은 본인의 Conect Key를 입력
# sec_key = "###" # API 신청 페이지에서 발급받은 본인의 Secret Key를 입력
# bithumb = pybithumb.Bithumb(con_key, sec_key) # Buthumb 클래스 객체를 생성하는데 초기화자(__init___)로 두 키값을 전달
# balance = bithumb.get_balance('BTC') # 잔고 조회
# get_balance() 메서드는 하나의 튜플을 반환함/튜플 안에는 네 개의 값이 저장되어 있는데 앞에서부터 순서대로 비트코인의 총 잔고, 거래 중인 비트코인의 수량, 보유 중인 총 원화, 주문에 사용된 원화를 의미
# print(format(balance[0], 'f')) # 읽기 좋은 실수로 값을 출력
# for ticker in pybithumb.get_tickers() : # public API인 get_tickers() 함수는 모든 가상화폐의 티커를 리스트로 반환 / 반복문의 ticker 변수에는 티커가 차례로 바인딩
#    balance = bithumb.get_balance(ticker) # ticker에 바인딩된 가상화폐를 private API인 get_balance() 메서드로 조회 결과 값은 balance 변수에 바인딩
#    print(ticker, ':', balance) # balance 변수에 저장된 잔고를 화면에 출력
#    time.sleep(0.1)
# order = bithumb.buy_limit_order('BTC', 3900000, 0.001)
# print(order) # ('bid', 'BTC', '1544373733978958') / 순서대로 매수, 종목, 주문 번호가 튜플로 반환됨 / 해당 주문 번호로 조회/취소/정정에 사용됨
# 지정가 매수를 하는 경우 다음 세 가지에 유의해서 주문을 넣어야함 = 최소 주문 수량 / 유효 자릿수 / 호가단위
# KeyError {'status': '5600', 'message': '1000원 단위로 거래 가능합니다.'} None / 이런식의 에러 메시지가 출력될 수 있음
# order = bithumb.buy_market_order('btc', 1) # 시장가 매수

# krw = bithumb.get_balance('BTC')[2] # get_balance() 메서드는 튜플을 리턴하는데 그중 2번 인덱스에 '원화 잔고'가 저장됨
# orderbook = pybithumb.get_orderbook('BTC') # get_orderbook() 함수는 딕셔너리를 리턴하는데 'asks"라는 키를 통해 매수 호가 내역을 리스트로 얻어올 수 있음
# asks = orderbook['asks'] 
# sell_price = asks[0]['price'] # 매도 호가 리스트에서 인덱싱을 통해 호가 정보 하나를 얻어오면 딕셔너리 타입임. 따라서 다시 'price'라는 키값을 사용해서 매도 금액을 얻을 수 있음
# unit = krw/sell_price # 원화 잔고를 최우선 매도 호가 금액으로 나누면 매수 수량을 구할 수 있음 / 잔고가 만원인데 가격은 천원이다 = 10개 살 수 있음
# print(unit)
# 호가창을 조회해서 예상 체결 가격에 매수 가능한 비트코인의 수량을 계산했더라도 예상 가겨보다 높게 매수될 수 있음 / 호가창에 매도 수량이 매수 수량보다 적거나 주문간 매도 호가가 상승할 수 있음
# unit = krw/float(sell_price) # 주문할 비트코인의 개수를 계산
# order = bithumb.buy_market_order('BTC', unit) # 계산한 개수만큼 시장가 주문을 발행함
# print(order) # 정상적으로 주문이 체결됐다면 buy_market_order() 메서드는 주문 ID를 리턴함
# 매도 또한 지정가와 시장가가 존재함
# order = bithumb.sell_limit_order('BTC', 4000000, 1)
# KeyError {'status': '5600', 'message': '주문량이 사용가능 BTC을 초과하였습니다.'} 주문 수량을 초과하면 이런 에러 로그가 출력됨
# unit = bithumb.get_balance('BTC')[0] # get_balance() 메서드는 튜플로 값을 리턴 / 0번 인덱스에는 보유 중인 비트코인의 잔고가 저장돼 있음
# order = bithumb.sell_limit_order('BTC', 400000, unit) # sell_limit_order() 메서드로 보유 중인 비트코인의 수만큼 지정가 매수 주문을 발행
# ('ask', 'BTC', '1529880463137270') / 매도, 종목, 주문 번호
# KeyError {'status': '5600', 'message': '1000원 단위로 거래 가능합니다.'} / 거래 단위 오류
# order = bithumb.sell_market_order('BTC', unit) # 보유 중인 비트코인을 모두 시장가에 매도
# cancle = bithumb.cancel_order(order) # buy_limit_order() 함수의 리턴 값(튜플)을 cancel_order 메서드의 입력으로 넣어 주문 취소 메서드를 호출
# 가격 변동폭 계산 : 타겟의 전일 고가(high)에서 전일 저가(low)를 빼서 가격 변동 폭을 구함
# 매수 기준 : 당일 시간에서 (변동폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수
# 매도 기준 : 당일 종가에 매도
# 래리 윌리엄스의 변동성 돌파 전략 ex) 전일 high 460, 전일 low 300 = 변동폭 160 / 현재 시가(open) 400 + 변동폭 160 * 0.5 = 480을 넘어 서면 바로 매수
# 매도는 일봉이 마감될때 시장가로 전량 매도

# ch06/06_12.py
# import pykorbit
# import time

# 목표가는 프로그램이 시작될 때 한 번 그리고 매일 자정마다 재계산되어야함 / 코드의 재사용을 위해 목표가를 계산하는 부분을 함수로 정리
# def get_target_price(ticker):
#     df = pykorbit.get_ohlc('BTC') # get_ohlc() 함수를 호출해서 비트코인의 일봉 정보를 DataFrame 객체로 얻어옴
#     # print(df.tail()) # tail() 메서드를 사용해서 DataFrame 객체에 저장된 일봉 데이터 중 끝의 5개 값만을 출력
#     yesterday = df.iloc[-2] # iloc[-2]로 끝에서 두 번째 행(전일 데이터)을 가져옴 yesterday에는 전일 데이터가 Series 객체로 바인딩

#     today_open = yesterday['close'] # 전일 종가
#     yesterday_high = yesterday['high'] # 전일 고가
#     yesterday_low = yesterday['low'] # 전일 저가
#     target = today_open + (yesterday_high - yesterday_low) * 0.5 # 래리 윌리엄스 변동성 돌파 전략의 목표가를 계산
#     return target
# import datetime # datetime 모듈을 임포트
# dt = datetime.datetime(2018, 12, 1) # datetime 클래스의 초기화자로부터 년/월/일 세 개의 값을 전달
# print(dt) # 객체가 바인딩된 dt 변수를 출력
# print(dt.year, dt.month, dt.day) # datetime 객체에 저장된 인스턴스 변수를 출력
# now = datetime.datetime.now()
# print(now)
# print(now == dt) # 비교 연산이 거짓이므로 Falese를 반환
# print(now > dt) # 비교 연산이 참이므로 True를 반환

# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 00:00:00 초의 datetime 객체를 생성하고, 1일의 시간을 더해 다음 날 자정으로 만듦
# print(now) # datetime.timedelta(1)이 1일의 시간을 의미
# print(mid)
# 변동성 돌파 전략은 24시간 동안 실행되며, 자정마다 목표가를 갱신해야함 / while문 안에서 now() 메서드와 datetime 클래스를 활용해서 자정을 판별


# import datetime
# import time

# now = datetime.datetime.now() # 프로그램이 시작할 때 실행되는 코드로 다음날 자정 시각을 계산하기 위해 현재 시각을 얻어옴
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 다음날 자정의 시간을 계산해서 dattime 객체로 저장

# while True:
#     now = datetime.datetime.now() # while문 안에서 반복해서 현재 시각을 얻어옴
#     if mid < now < mid + datetime.timedelta(seconds=10): # (seconds=10)은 10초를 더한다는 의미 / 현재 시각(now)이 자정(mid)과 자정에서 10초 뒤의 구간 사이에 있는가를 비교
#         print('정각입니다')
#         now = datetime.datetime.now() # 자정이라면 다음날의 자정 시각을 계산
#         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

#     print(now, 'vs', mid) # 현재 시각과 다음날 자정 시각을 출력
#     time.sleep(1)
# 자 이제 목표가 계산까지 포함된 전체 코드
# ch06/06_16.py
# import time
# import pykorbit
# import datetime

# def get_target_price(ticker): # 타겟프라이스 출력을 위한 함수
#     df = pykorbit.get_ohlc(ticker)
#     yesterday = df.iloc[-2]

#     todayopen = yesterday['close']
#     yesterday_high = yesterday['high']
#     yesterday_low = yesterday['low']
#     target = todayopen + (yesterday_high - yesterday_low) * 0.5
#     return target # return은 외부로 출력

# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
# target_price = get_target_price('BTC') # 위에 만든 목표가 인자에 BTC를 넣음

# while True:
#     now = datetime.datetime.now()
#     if mid < now < mid + datetime.timedelta(seconds=10):
#         target_price = target_price('BTC')
#         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

#     current_price = pykorbit.get_current_price('BTC')
#     if current_price > target_price: # 현재가가 목표가 보다 크다면 다음 코드를 실행함
#         krw = korbit.get_balance('BTC')[2] # 잔고 조회 API를 사용해서 보유 중인 원화를 얻어옴
#         orderbook = pykorbit.get_orderbook('BTC') # 호가창을 조회해서 최우선 매도 호가를 조회
#         sell_price = orderbook['asks'][0]['price'] 
#         unit = krw/float(sell_price) # 원화 잔고를 최우선 매도가로 나눠서 구매 가능한 수량을 계산
#         korbit.buy_market_order('BTC', unit) # 시장가 주문으로 비트코인을 매수

#     time.sleep(1)

# # 매수와 관련된 코드를 Buy_crypto_currency() 함수로 정리
# def buy_crypto_currency(ticker):
#     krw = pykorbit.get_balance(ticker)[2]
#     orderbook = pykorbit.get_orderbook(ticker)
#     sell_price = orderbook['asks'][0]['price']
#     unit = krw / float(sell_price) # float은 실수
#     korbit.buy_market_order('BTC', unit)

# # 매도 기능을 추가
# while True:
#     now = datetime.datetime.now()
#     if mid < now < mid + datetime.timedelta(seconds=10):
#         target_price = get_target_price('BTC')
#         now = datetime.datetime.now()
#         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#         sell_crypto_currency('BTC')

# # sell_crypto_currency() 라는 매도 함수를 구현 / 단순히 본인 계좌에서 비트코인이 있는지 잔고 조회한 후 조회된 수량의 비트코인을 시장가로 전량 매도
# def sell_crypoto_currency(ticker):
#     unit = korbit.get_balance(ticker)[0]
#     korbit.sell_market_order(ticker, unit)

# 정리해보면 매일 밤 자정에는 다음과 같은 순서로 작업이 진행됨
# 1) 보유한 비트코인이 있다면(당일 매수 조건에 따라 매수가 됐다면) 해당 비트코인을 시장가로 매매
# 2) 전일 시가, 고가, 저가, 종가 기준으로 래리 윌리엄스의 변동성 돌파 전략 기반 목표가 재계산
# 3) 해당 일 기준으로 다음 날의 00:00:00 초 시간 계산

# ch06/06_18.py 매수/매도 기능까지 함수로 정리한 코드
# while True:
#     now = datetime.datetime.now()
#     if mid < now < mid + datetime.timedelta(seconds=10):
#         target_price = get_target_price('BTC')
#         mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#         sell_crypto_currency('BTC')

#     current_price = pykorbit.get_current_price('BTC')
#     if current_price > target_price:
#         buy_crpto_currency('BTC')
#     time.sleep(1)

# 보안 예외 처리 / 아이디 or 비번을 코드 상에 문자열로 직접 입력했을때, 코드 공개시 정보가 유출됨
# 이를 방지하기 위해 vs code 경로에 메모장을 생성 후 개인 정보를 보관
# with open("hide.txt") as f: # 예외처리 기능이 포함된 파일 열기 코드
#     lines =f.readlines() # 파일에서 모든 줄(line)을 읽어서 파이썬 리스트로 저장
#     id = lines[0].strip() # line[0] 번(id)을 읽은 후 strip() 메서드를 호출하여 좌우 공백을 제거한 문자열을 id라는 변수로 바인딩
#     password = lines[1].strip() # line[1] 번(password)을 읽은 후 strip() 메서드를 호출하여 좌우 공백을 제거한 문자열을 id라는 변수로 바인딩

# print(id)
# print(password)

# 지금까지 구현한 변동성 돌파 전략은 이상적인 환경에서만 동작 가능 / 네트워크 상태가 일시적으로 좋지 않거나 해당 서버가 불안정한 경우 API 호출의 실패로 프로그램이 종료될 수 있음
# 프로그램이 종료되면 매수/매도를 해야 할 시점에 대응하지 못해 추가적인 손실을 입히거나 시장 참여 기회를 잃어버릴 수 있음

# 이동평균(Moving Average)
# 종가를 기준으로 5일 이동평균을 계산
# import pybithumb
# import pyupbit
# import pykorbit
# import datetime
# import time

# df = pykorbit.get_ohlc('BTC')
# close = df['close']
# ma5 = close.rolling(5).mean()
# print(ma5)

# 매수함수 업데이트
# def get_yesterday_ma5(ticker):
#     df = pykorbit.get_ohlc(ticker)
#     close = df['close']
#     ma5 = close.rolling(5).mean()
#     return ma5[-2]

# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
# ma5 = get_yesterday_ma5('BTC')
# target_price = get_traget_price('BTC')

# while True:
#     try:
#         now = datetime.datetime.now()
#         if mid < now < mid + datetime.timedelta(seconds=10):
#             target_price = get_target_price('BTC')
#             mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#             ma5 = get_yesterday_ma5('BTC')
#             sell_crypto_currency('BTC')

#         current_price = pykorbit.get_current_price('BTC')
#         if (current_price > target_price) and (current_price > ma5):
#             buy_crypto_currency('BTC')
#     except:
#         print('에러발생')
#     time.sleep(1)






