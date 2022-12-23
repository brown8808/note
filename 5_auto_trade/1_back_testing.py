# 백테스팅이란 '과거 데이터를 사용해서 투자 전략이 어느 정도의 수익률이 나는지를 화인하는 과정'
# 주식과 가상화폐에 관련된 검증되지 않은 수많은 투자 전략이 존재 / 이런 투자 전략들을 곧이곧대로 믿기 보다는 백테스팅을 통해 검증한 후 실제 투자에 적용해야함

# ch07/07_01.py
# import pykorbit

# df = pykorbit.get_ohlc('BTC') # pykorbit 모듈의 get_ohlc() 함수를 사용하면 암호화폐의 일봉 차트 데이터를 DataFrame으로 얻어올 수 있음
# print(df.tail()) # 얻어온 DtaFrame 객체의 tail() 메서드를 호출해서 마지막 5 줄(row)을 출력 / 인자를 지정하지 않으면 기본 5줄 데이터를 리턴해줌

# DataFrame 객체를 액셀로 저장하기
# 백테스팅을 위한 프로그램을 작성할 예정 / 이때 주의할 점은 백테스팅을 위해 작성한 코드에 버그가 있으면 안됨
# 전략을 검증하기 위해 백테스팅을 하는 것인데 백테스팅 과정에 오류가 있다면 제대로 전략을 평가할 수 없음
# 따라서 백테스팅 코드를 작성할 때는 반드시 여러 번 크로스체크를 하는 것이 필요
# 이를 위해 액셀을 사용 / DataFrame 클래스의 to_excel() 메서드를 사용하면 DataFrame 객체를 엑셀로 저장할 수 있음

 # ch07/07_02.py
# import pykorbit

# df = pykorbit.get_ohlc('BTC') # 'BTC'의 오하로클 데이터를 df로 바인딩해서
# df.to_excel('btc.xlsx') # 엑셀 생성 후 해당 파일명으로 저장
# 오.. 이렇게 간단할 일인가..
# df['range'] = (df['high'] - df['low']) * 0.5 # 'range'라는 컬럼(column)을 추가 후 (고가(high) - 저가(low)) * 0.5
# df.to_excel('BTC.xlsx')
# DataFrame은 for문을 사용하지 않고도 여러 행(row)에 동일한 연산을 적용할 수 있음 / 위 코드를 실행하면 range 컬럼이 추가된 엑셀 파일을 확인할 수 있음

# ch07/07_04.py
# import pykorbit

# df = pykorbit.get_ohlc('BTC')
# df['range'] = (df['high'] - df['low']) * 0.5
# df['range_shift1'] = df['range'].shift(1) # shift(1) 메서드의 결과 확인
# df['target'] = df['open'] + df['range'].shift(1) # shift(1) 메서드로 'range'의 컬럼 값을 1행 내려준 후 df['open']컬럼과 더하고 그 결과값을 'target'이라는 컬럼으로 저장
# 목표가 계산은 각 거래일을 기준으로 전날의 레인지를 사용하기 때문에 'range' 컬럼을 1행씩 내려줌
# df.to_excel('BTC.xlsx')
# DataFrame 객체에서 각 컬럼은 Series 객체임 / Series 객체에 대해 shift() 메서드를 사용하면 데이터를 위/아래로 시프트 시킬 수 있음
# 결과는 각 거래의 고가(high)가 목표가(target) 이상이면 수행된 것

# numpy.where(조건, 조건이 참 일 때의 값, 조건이 거짓일 때의 값)

# ch07/07.06.py
# import numpy as np # numpy 모듈을 np라는 이름으로 임포트
# from pandas import DataFrame

# data = {'빗썸': [100, 100, 100], # 딕셔너리를 data로 바인딩
#         '코빗': [90, 110, 120]}

# df = DataFrame(data)
# df['최저가'] = np.where(df['빗썸'] < df['코빗'], '빗썸', '코빗') # 빗썸보다 코빗이 크면 빗썸을 반환 아니면 코빗을 반환
# df.to_excel('거래소.xlsx')

# 각 거래일 기준으로 고가(high)가 목표가(target)보다 크면 매수 조건에 해당하고 그때의 수익률은 '매도가/매수가'임
# ex) 10,000원에 매수 / 12,000원에 매도했다면 수익률은 1.2가됨 / 매수 조건을 만족하지 못한 경우의 수익률은 1이됨

# ch07/07_07.py
# import pykorbit
# import numpy as np

# df = pykorbit.get_ohlc('BTC')
# df['range'] = (df['high'] - df['low']) * 0.5
# df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032 # 수수료를 고려할 시

# df['ror'] = np.where(df['high'] > df['target'], # 넘파이 where()메서드를 사용해서 고가와 목표가를 비교, 조건 만족시 수식 적용, 만족하지 않은 경우는 1로 표현
#                 df['close'] / df['target'] - fee, # 여기에 fee만 빼주면됨
#                 1) # 기간수익률(HPR: Holding Period Return)을 계산할때 백테스팅의 경우 수익률을 퍼센트(%)로 계산하기보다 몇 배(ratio)로 표현하는 것이 더 좋음

# df.to_excel('trade.xlsx')
# ror = df['ror'].cumprod()[-2] # Series 객체에서 모든 값을 곱해주는 메서드로 cumprod()가 있음 / ror 컬럼의 값을 모두 곱해서 누적 수익률을 계산함
# print(ror)
# 수수료를 고려하기 전과 비교해보면 투자수익률이 큰 차이가 나는 것을 확인할 수 있음

# 가장 좋은 k(변동폭)를 구하는 방법 / 백테스팅으로 과거 기록중 가장 좋은 k 값을 찾기 가능 = 수익률이 더 높은 것
# 07/07_11.py
# import pykorbit
# import numpy as np

# def get_ror(k=0.5): # ror(rate of returns)를 계산하는 코드를 함수로 만들어줌. 이때 함수는 k값을 함수의 인자(parameter)로 입력받음 / 0.5 없어도됨
#     df = pykorbit.get_ohlc('BTC')
#     df['range'] = (df['high'] - df['low']) * k
#     df['target'] = df['open'] + df['range'].shift(1)

#     fee = 0.0032
#     df['ror'] = np.where(df['high'] > df['target'],
#                 df['close'] / df['target'] - fee,
#                 1)
#     ror = df['ror'].cumprod()[-2]
#     return ror

# for k in np.arange(0.1, 1.0, 0.1): # 0.1 부터 1.0까지 증가한 값으로 for loop을 만들기 위해 noupy 모듈의 arange() 함수를 사용 / range()는 정수값만 사용 가능
#     ror = get_ror(k) # get_ror()함수를 호출하여 입력된 k값에 따른 수익률을 계산
#     print('%.1f %f' % (k, ror)) # k값과 수익률을 화면에 출력

# MDD(Maximum Draw Down) 계산하기 / MDD는 투자 기간 중에 포트폴리오의 전 고점에서 저점까지의 최대 누적 손실을 의미
# MDD 수식 = high - low / high * 100

# import pykorbit
# import numpy as np

# df = pykorbit.get_ohlc('BTC')
# df['range'] = (df['high'] - df['low']) * 0.5
# df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032 # 수수료를 고려할 시

# df['ror'] = np.where(df['high'] > df['target'], # 넘파이 where()메서드를 사용해서 고가와 목표가를 비교, 조건 만족시 수식 적용, 만족하지 않은 경우는 1로 표현
#                 df['close'] / df['target'] - fee, # 여기에 fee만 빼주면됨
#                 1) # 기간수익률(HPR: Holding Period Return)을 계산할때 백테스팅의 경우 수익률을 퍼센트(%)로 계산하기보다 몇 배(ratio)로 표현하는 것이 더 좋음



# ror = df['ror'].cumprod()[-2] # Series 객체에서 모든 값을 곱해주는 메서드로 cumprod()가 있음 / ror 컬럼의 값을 모두 곱해서 누적 수익률을 계산함
# df['hpr'] = df['ror'].cumprod()
# df.to_excel('btc.xlsx')
# print(ror)

#07/07_13.py
# import pykorbit
# import numpy as np

# df = pykorbit.get_ohlc('BTC')
# df['range'] = (df['high'] - df['low']) * 0.5
# df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032
# df['ror'] = np.where(df['high'] > df['target'],
#             df['close'] / df['target'] - fee,
#             1)

# df['hpr'] = df['ror'].cumprod()
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# print('MDD(%) : ', df['dd'].max())
# df.to_excel('btc.xlsx')

# ch07/07_14.py
# import pykorbit
# import numpy as np

# df = pykorbit.get_ohlc('BTC')

# df['ma5'] = df['close'].rolling(window=5).mean().shift(1) # 'close'컬럼을 사용해서 각 거래일에 대해 5일 이동평균을 계산, shift(1)을 호출해서 계산된 5일 이평값을 한 행 밑으로 내려 저장
# df['range'] = (df['high'] - df['low']) * 0.5 # 변동폭 설정
# df['target'] = df['open'] + df['range'].shift(1) # 매수 타겟가 설정
# df['bull'] = df['open'] > df['ma5'] # 거래일의 시가가 전일 종가까지 계산된 5일 이동편균보다 크면 'bull' 컬럼에 True를 저장하고 그렇지 않으면 False를 저장함

# fee = 0.0032
# df['ror'] = np.where((df['high'] > df['target']) & df['bull'], # 매수 조건에 '상승장' 여부를 저장하고 있는 'bull' 컬럼을 추가로 확인, 조건을 추가할 때 and가 아니라 '&(앰퍼샌드)'를 사용해야함
#             df['close'] / df['target'],
#             1)

# df['hpr'] = df['ror'].cumprod() # 컴프로드로 ror series를 모두 곱해줌
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100 # 최고가 - 최저가 / 최고가 * 100 (Maximum Draw Down)  MDD 계산
# print('MDD : ', df['dd'].max())
# print('HPR : ', df['hpr'][-2])
# df.to_excel('larry_ma.xlsx')

# ch07/07_15.py
# import pykorbit
# import numpy as np

# def get_hpr(ticker):
#     try:
#         df = pykorbit.get_ohlc(ticker)
#         df = df.loc['2021'] # DataFrame의 loc라는 메서드 / 해당하는 행 가져오기

#         df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
#         df['range'] = (df['high'] - df['low']) * 0.5
#         df['target'] = df['open'] + df['range'].shift(1)
#         df['bull'] = df['open'] > df['ma5']

#         df['ror'] = np.where((df['open'] > df['target']) & df['bull'],
#                               df['close'] / df['target'],
#                               1)

#         df['hpr'] = df['ror'].cumprod() # Cumulative Product 누적곱! 외우자..
#         df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#         return df['hpr'][-2]

#     except:
#         return 1

# tickers = pykorbit.get_tickers() # 코빗에서 거래되는 모든 티커 목록을 얻어옴

# hprs = [] # for 루프를 실행하기 전에 리스트를 만들어줌
# for ticker in tickers:
#     hpr = get_hpr(ticker)
#     hprs.append((ticker, hpr)) # 리스트에 코인의 티커와 코인의 기간 수익률을 저장

# sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True) # 기간수익률을 기준으로 오름차순 정렬
# print(sorted_hprs[:5]) # 기간수익률이 높은 5개의 코인 정보를 화면에 출력

# ch07/07/15.py 복습 / 왜 작동 안되지..
# import pykorbit
# import numpy as np

# def get_hpr(ticker):
#     try:
#         df = pykorbit.get_ohlc(ticker)
#         df = df.loc('2018')

#         df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
#         df['range'] = (df['high'] - df['low']) * 0.5
#         df['target'] = df['open'] + df['range'].shift(1)
#         df['bull'] = df['open'] > df['ma5']

#         df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
#                     df['close'] / df['target'],
#                     1)

#         df['hpr'] = df['ror'].cumprod()
#         df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#         return df['hpr'][-2]
#     except:
#         return 1
        
# tickers = pykorbit.get_tickers()

# hprs = []
# for ticker in tickers:
#     hpr = get_hpr(ticker)
#     hprs.append((ticker, hpr))

# sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True)
# print(sorted_hprs[:5])



