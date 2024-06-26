'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 숫자 맞추기 게임
            컴푸터에 1 ~ 10 사이의 숫자를 정해두고
            사용자에게 5번의 기회를 줍니다.
            사용자는 컴퓨터가 가지고 있는 숫자를 맞추고
            몇번만에 맞췄는지 알려줌

            
    [문제분석]
        컴퓨터가 임의로 1~10 중의 숫자를 정한다 (랜덤수)
        기회는 5번 주어지고 만약 n번째로 맞추었다면 n번째 맞추었다고 말해주고 게임의 종료.
        기회를 모두 소진시 프로그램 종료. break
        반복 - 선택

                    
    [알고리즘]
        1. 1~10까지 랜덤수를 저장한다.
        2. 5번 반복하면서
            2-1. 1~10까지 중 하나의 숫자를 입력한다.
                2-1-1. 만약 저장한 랜덤 수 와 같다면
                    2-1-1-1. (게임승리,n번만에 맞췄습니다.) 를 출력하고 종료한다. break
                2-1-2. 만약 저장한 랜덤 수 와 다르다면
                    2-1-2-1. (틀렸습니다. 기회가 n번남았습니다.) 를 출력한다.


'''
import random #랜덤 수 사용하기 위한 함수 불러오기

# 1~10 사이 랜덤 수 발생하기 => 변수에 저장
comnum = random.randint(1,10)

for count in range(1,6) :
    usernum = int(input('숫자 입력 : '))
    if usernum == comnum :
        print(f"승리{count}번째로 맞췄습니다.")
        break
    elif usernum != comnum :
        print(f'틀렸습니다{5 - count}번 남았습니다')
        
