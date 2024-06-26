'''
    작성일 : 2024년 4월 18일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 1~10 까지 합을 출력하시오.
            합계를 계산하되 , 합이 30이상이면 프로그램을 종료하고,
            그때의 합을 출력하시오
    [문제분석]    
    반복 하면서 합계를 계산한다.
    합계가 30이상이면 프로그램을 종료한다.
    반복조건:10까지
    선택조건:30이상인가?    종료
    
    break => 반복을 멈춘다. (나를 포함하고 있는 반복을 멈춘다.)

    [알고리즘]
        0. sum = 0
        1. 1부터 10까지 반복하면서 합계를 계산한다.
            1-1. 합계가 30 이상이면
                1-1-1. 반복을 멈춘다.()
        2. 합계를 출력한다.
    
'''
sum = 0
for num in range(1,11,1) :
    sum = sum + num
    if sum >= 30 :
        break
print("sum =", sum)

sum = 0
num = 1
while num < 11 :
    sum = sum + num
    if sum > 30 :
        break
    num = num + 1
print(f'{sum}입니다.')
