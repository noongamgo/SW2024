'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 정수를 입력받아 팩토리얼을 출력하시오.
            팩토리얼 계산하는 부분은 함수로 작성하고 결과는 돌려줍니다.
    [문제분석]
        n! = n * (n-1) * (n-2) * ... * 1
        n = 정수
    [알고리즘]
        1. 함수
            1) 정수를 전달 받는다.
            3) 전달받은 정수로 팩토리얼을 계산한다.
            4) 결과를 리턴한다.
        2. 메인
            2) 정수를 입력한다.
            5) 함수를 호출한다.
            6) 결과를 출력한다.

'''
# 함수 선언
result = 0
def result(factor) :
    for i in range(1, factor) :
        factor = factor * i
    return factor
        
                

# 함수 호출
factor = int(input("정수를 입력하시오. : "))
print(result(factor))
