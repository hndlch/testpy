# animals='원숭이 닭 개 돼지 쥐 소 호랑이 토끼 용 뱀 말 양'
# animals=animals.split()
# print(animals)
# year=int(input('연도를 입력하세요:'))
# print(f'{year}년은 {animals[year%12]}띠의 해입니다.')
# if 문을 안 써도 된다

# 동전교환프로그램내가볼땐이게베스트
# money=int(input('금액을 입력하세요:'))
# for unit in [500,100,50,10,1]:
#     print(f'{unit}원짜리: {money//unit}개')
#     money%=unit

import random

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

