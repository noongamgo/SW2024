'''
    작성일 : 2024년 5월 10일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 1부터 100사이의 정수형 난수를 10개 생성하여 리스트에 저장하고,
        리스트에서 가장 큰 값과 작은 값을 출력한뒤,
        리스트 값의 합계와 오름차순으로 정련된 리스트를 출력하시오.

    [문제분석]
        랜덤수는 import random을 포함 시켜야 한다.
        랜덤 수 생성하기 위해서는 메소드 random.radint(1,100)을 사용한다.

    [알고리즘]
        1. 빈 리스트 생성
        2. 10번 반복하면서
            2-1. 랜덤수 생성하여 리스트에 추가한다
        3. 가장 큰값과 작은 값, 합계, 오름차순 정령 출력    
'''
# 랜덤 모듈 사용선언
import random
num = []

for i in range(10) :
    num.append(random.randint(1,100))
print('생성된 리스트(num) : ', num)
print('가장 큰값은 : ',max(num))
print('가장 작은값은 : ',min(num))
print('전체요소의 합 : ', sum(num))
num.sort()
print('오름차순 정렬 : ', num)
num.sort(reverse=True)
print('내림차순 정렬 : ', num)

