import pyupbit # pip install -U pyupbit
# print(pyupbit.Upbit) # 에러가 없다면 정상 설치 완료

tickers = pyupbit.get_tickers()
# print(tickers) # 항목별 KRW, BTC 등의 접두사가 붙어있음 / 해당 통화로 매매 가능
tickers = pyupbit.get_tickers(fiat='KRW') # pyupbit 모듈은 시장별로 티커를 얻어올 수도 있음 / 기준 통화(fiat)값을 입력하면 특정 시장의 티커만 가져옴
# print(tickers)
price = pyupbit.get_current_price('BTC-XRP') # 반환하는 값의 단위가 BTC이기 때문에 소수점 단위로 출력됨
# print(price)
price = pyupbit.get_current_price(['KRW-XRP', 'KRW-DOGE']) # 여러 가상화폐의 현재가를 한 번에 조회할 때는 리스트 형태로 넘겨주면 됨
# print(price) # 여러 가상화폐의 현재가를 한 번에 조회했기 때문에 결괏값이 딕셔너리로 리턴됨 / 티커를 key로 해서 현재가가 value로 저장되어 있음
df = pyupbit.get_ohlcv('KRW-BTC') # 가격 조회
# print(df)
df = pyupbit.get_ohlcv('KRW-BTC', count=5) # 최근 5일간의 데이터만 조회
# print(df)
df = pyupbit.get_ohlcv('KRW-BTC', interval='minute1') # get_ohlcv() 함수의 interval 옵션으로 월/주/일/분봉 중 하나를 선택 가능 / 미입력시 기본 일봉으로 셋팅
# print(df)

orderbook = pyupbit.get_orderbook('KRW-BTC') # get_orderbook() 함수의 리턴되는 값은 리스트 객체인데 리스트 안에 딕셔너리 객체가 있음
bids_asks = orderbook['orderbook_units']

# for bid_ask in bids_asks: # 호가창 보기
#     print(bid_ask)

# ch08_07.py 매수 / 매도
import pyupbit

access_key = '1234'
secret_key = '1234'

upbit = pyupbit.Upbit(access_key, secret_key) 
ret = upbit.buy_limit_order('KRW-XRP', 100 ,20) # 순서대로 종목, 가격, 개수 / buy_limit_order() 함수가 정상적으로 동작했는지 확인 여부는 미체결 내역을 보면됨
ret = upbit.sell_limit_order('KRW-XRP', 100, 20) # 지정가 매도
ret = upbit.cancel_order('uuid입력') # 주문 취소
# print(ret) # 리턴값은 튜플 객체 / 주문 API 호출시 해당 주문 건에 대한 'uuid' 값이 리턴되는데 이 값을 통해 미체결된 주문을 취소할 수 있음

# ch08/08_21.py

import ccxt # 바이낸스가 지원하는 API는 공식 문서를 참조해서 이를 직접 구현 가능 / 하지만 기존에 개발된 파이썬 모듈을 사용하면 개발 시간을 크게 줄일 수 있음
# CCXT(CryptoCurrency eXchange Trading Library) 모듈은 자바스크립트, 파이썬, PHP와 같이 다양한 언어에서 범용적으로 사용할 수 있는 가상화폐 거래소 모듈임
# 바이낸스 뿐만 아니라 피트파이넥스, 비트렉스, 크라켄 등등 125개 거래소의 API를 지원

binance = ccxt.binance() # cctx 모듈에서 binance 객체를 생성
markets = binance.fetch_tickers() # binance 객체의 fetch_ticker() 메서드는 티커와 거래 가격 정보를 딕셔너리로 반환
# print(markets.keys()) # 딕셔너리의 키값을 출력
ticker = binance.fetch_ticker('ETH/BTC')
# print(ticker['open'], ticker['high'], ticker['low'], ticker['close']) # API를 호출한 시점에서의 종가('close')는 최근 거래된 가격인 현재가임
ohlcvs = binance.fetch_ohlcv('ETH/BTC')
# print(ohlcvs) # 출력 결과를 살펴보면 가격 정보(일자, 시가, 고가, 저가, 종가, 거래량)가 리스트로 저장되어 있음 / 일자는 timestamp 형태로 출력

import datetime # 타임스탬프를 문자열로 변환하기 위해 datetime 모듈을 import

# for ohlc in ohlcvs: 
#     print(datetime.datetime.fromtimestamp(ohlc[0]/1000).strftime('%y-%m-%d %H:%M'))

orderbook = binance.fetch_order_book('ETH/USDT')
# print(orderbook['bids'])
# print(orderbook['asks'])
# for ask in orderbook['asks']: # for 문을 사용해서 orderbook['ask']에 저장된 매도호가를 하나씩 출력
#     print(ask[0], ask[1]) # orderbook['ask']에는 (매도 가격, 매도 수량)이 리스트로 저장되어 있기 때문에 0, 1 인덱스로 그 값을 출력할 수 있음

binance = ccxt.binance({ # public API와 동일하게 binance 클래스의 인스턴스를 통해 메서드를 호출
    'apikey' : 'Your API KEY',
    'secret' : 'Your secret key',
})

balance = binance.fetch_balance() # 잔고 조회는 fetch_balance()로
# print(balance) # 리턴 값은 딕셔너리 객체
# 잔고 조회 메서드의 딕셔너리 안에는 거래 수수료 정보가 포함된 'info'와 가상화폐 이름들이 키값으로 저장되어 있음
# 이때 잔고 조회에 저장된 티커에는 시장 정보가 포함되어 있지 않음

# 가상화폐 이름의 키 값 안에는 보유 중인 코인('free'), 거래 진행 중인 코인('used'), 전체 코인('total')의 개수가 딕셔너리로 저장되어 있음 / 딕셔너리 안에 딕셔너리가 있는거
# print(balance['BTC']['free'], balance['BTC']['used'], balance['BTC']['total'])
order = binance.create_limit_buy_order('XRP/BNB', 50, 0.03) # create_limit_buy_order() 메서드에 티커, 주문 수량, 주문 가격을 차례로 전달
print(order)



