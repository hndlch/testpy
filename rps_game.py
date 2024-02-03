import random
import time
print('게임이 시작됩니다 ... ')
time.sleep(1)

while True:
    man=input('가위 바위 보 중 하나 선택(엔터는 종료): ')
    com=random.choice(['가위','바위','보'])
    if man == '': break
    if man not in ['가위','바위','보']:
        print('다시 입력하세요')
        continue
    if com==man:
        print('무승부')
    elif (com=='가위' and man=='바위')or(com=='바위' and man=='보')or(com=='보' and man=='가위'):
        print('승')
    else:
        print('패')

    print('-'*40)
    print(f'컴퓨터:{com}, 사람:{man}')
    print('-'*40)