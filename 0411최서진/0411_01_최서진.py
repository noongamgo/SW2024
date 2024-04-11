'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 반복문 while
'''

# 1~10까지 출력하기
print("=== 반복문 while로 1부터 10까지 출력하기 1 ===")

num1 = 1    #초기값. 숫자는 1부터
while num1 <= 10 :      # 조건식. 숫자를 10까지
    print(num1, end= ' ')     # 반복하면서 할 일.
    num1 = num1 + 1 # 증감식.숫자를 1씩 증가하면서

print()     # 한 줄 바꿈
print("=== 반복문 while로 1부터 10까지 출력하기 2 ===")
num1 = 1    # 초기 값
num2 = 10   # 종료 값
while num1 <= num2 :
    print(num1, end =' ')
    num1 = num1 + 1


print('=== 반복문으로 자기 이름 10개 출력하기 ===')
i = 1
while i <= 10 :
    print(i, end= '. ')
    print("최서진")
    i = i + 1    
i = 1 # i, j, k ,l
# i, j 반복 회수를 저장하는 변수
