# 가상화폐 거래소에서 거래가 체결되면 가상화폐의 가격이 변함. 이때 사용자는 가상화폐가 언제 체결될지 알 수 없음
# 따라서 REST API와 같은 요청(request)-응답(response) 방식으로는 체결 시점의 데이터를 지연 없이 얻기란 사실상 불가능함
# 최선의 방법은 0.1초와 같이 정해진 시간마다 주기적으로 시세를 요청함으로써 가장 최근 체결가를 얻는 것
# 물론 이 경우에도 최대 0.1초의 지연이 발생하게됨

# 요청 - 응답 방식으로도 기본적인 자동매매 프로그램을 개발 할 수 있음
# ! 재정거래(Arbitrage) 프로그램의 경우에는 되도록 지연이 없이 체결 시점의 현재가를 얻는 것이 매우 중요
# 사용자는 거래소에서 가상화폐가 체결되는 시점을 알 수 없으므로 가상화폐가 체결될 때 서버가 나에게 알려줘야함

# ch09/09_01.py
def sync_func1():
    print('Hello')

def sync_func2():
    print('Bye')

# sync_func1()
# sync_func2()
# 함수의 정의는 def라는 키워드를 사용 / 위와 같이 sync_func1, sync_func2 함수를 정의한 후 이를 순차적으로 호출하면 1, 2가 호출됨
# 이러한 전통적인 함수 호출 방식을 동기(synchronous) 호출 방식이라고함

# 코루틴 / 파이썬에서 어떤 함수가 비동기 방식으로 처리되도록 설정하려면 async라는 키워드를 붙여주면됨 이를 코루틴(coroutine)이라고 부름
# 코루틴 함수는 정의하는 방법도 다르지만, 호출 역시 일반 함수와 다른 방식으로 호출해야함 / 일반 함수처럼 호출하면 에러가 발생함

# ch09/09_02.py
# import asyncio

# async def async_func1(): # async_func1이라는 코루틴을 정의
#     print('Hello')

# loop = asyncio.get_event_loop() # 이벤트 루프를 가져옴
# loop.run_until_complete(async_func1()) # 코루틴 객체가 완료될 때까지 실행
# loop.close() # 이벤트 루프를 닫음

# ch09/09_04.py
# import asyncio

# async def make_americano(): 
#     print('Americano Start')
#     await asyncio.sleep(3) # 3초를 기다리기 위해 acyncio.sleep 함수를 호출 / timesleep과 비슷하게 정해진 시간(secs)동안 대기
#     print('Americano End')
#     return 'Americano'

# async def make_latter():
#     print('Latter Start')
#     await asyncio.sleep(5) # timesleep 함수가 CPU를 점유하면서 기다리는 것과 달리 asyncio.sleep 함수는 CPU가 다른 코루틴을 처리할 수 있도록 CPU점유를 해제한 상태로 기다림
#                            # asyncio.sleep 함수 역시 코루틴인데 코루틴 내에서 다른 코루틴을 호출할 때 await 구문을 사용
#     print('Latter End')
#     return 'Latter'
#     # 코루틴에서도 값을 리턴 가능
# async def main():
#     coro1 = make_americano() # 아메리카노를 만드는 코루틴 객체를 생성
#     coro2 = make_latter() # 커피 라테를 만드는 코루틴 객체를 생성
#     result = await asyncio.gather( # 두 코루틴을 동시에 실행
#         coro1,
#         coro2
#     )
#     print(result)
# asyncio.gather 함수가 리턴하는 값을 result 변수로 바인딩 / 해당 리턴값이 파이썬 리스트에 담겨서 전달됨

# print('Main Start')
# asyncio.run(main()) # 이벤트 루프를 생성하여 main 코루틴을 처리하고 이벤트 루프를 닫음
# print('Main End')
# 아메리카노를 만드는 코루틴과 커피 라테를 만드는 코루틴을 정의 후 코드 실행 시 스레드를 사용하지 않았음에도 동시에 수행되는 것을 볼 수 있음

# multiprocessing 모듈
# 파이썬 코드를 작성한 후 이를 실행시키면 파이썬 인터프리터가 코드를 해석한 후 실행해줌. 프로세스 관점에서 보면 이를 메인 프로세스(Main Process)라고 부를 수 있음
# multiprocessing 모듈의 current_process 함수를 호출하면 현재 실행 되는 프로세스에 대한 정보를 담고 있는 객체를 얻을 수 있음
# 해당 객체의 name과 pid 속성에 접근하면 프로세스의 이름과 PID(Process ID)를 얻을 수 있음. 
# 여기서 PID란 운영체제가 각 프로세스에 부여한 고유 번호로써 프로세스의 우선순위를 조정하거나 종료하는 등 다양한 용도로 사용

# ch09/09_06.py
import multiprocessing as mp

if __name__ == "__main__":
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)