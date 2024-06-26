'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 두 개의 정수를 입력받아 큰 수를 출력하시오.
            큰 수를 찾는 부분을 함수로 작성합니다.

    [문제분석]
        큰 수 찾는 부분은 함수로 작성한다.
        결과는 함수를 호출한 메인으로 돌려준다.
        메인은 두 수를 입력 받는다.
    [알고리즘]
        1.함수
            1) 두 수를 메인으로 부터 전달 받는다.
            3) 전달 받은 두 수 의 크기를 비교한다
            4) 만약 num1이 크다면
                4-1) num1의 값을 리턴한다.
            5) 아니면
                5-1) num2의 값을 리턴한다.
        2.메인
            2) 두 수 를 입력받는다.
            6) 함수를 호출한다.
            7) 결과를 출력한다.
            


'''
# 함수 선언
def num(num1,num2) :
    if num1 > num2 :
        return(num1)
    else :
        return(num2)
# 메인 
num1 = int(input("첫 번째 수 를 입력하시오 :"))
num2 = int(input("두 번째 수 를 입력하시오 :"))

print(f"{num1}과 {num2}중 큰수는 {num(num1, num2)}입니다.")