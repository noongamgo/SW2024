'''
    작성일 : 2024년 3월 29일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 2개의 정수를 입력받아
            두 수의 크기를 비교하는 프로그램

    [문제분석]
        필요한 변수는 무엇? 2개 num1 num2
        입력받는 두 수는 모두 정수로 변환해야 한다.
        두 수가 같은가?         num1 == num2
        첫번째 수가 두번째 수보다 큰가? num1>num2
        두번째 수가 첫번쨰 수보다 큰가? num1<num2

    [알고리즘]
    1. 두 개의 정수를 입력 받는다.
    2. 만약에 num1과 num2가 같다면
        2-1. 'num1'과 'num2'는 같다. num1 == num2
    3. 아니면 만약에 num1 < num2 라면
        3-1. 'num2'가 'num1'보다 크다.
    4. 아니면
        4-1. 'num1'이 'num2'보다 크다.

'''
num1 = '정수a'
num2 = '정수b'

num1 = int(input(f"{num1}를 입력하시오"))
num2 = int(input(f"{num2}를 입력하시오."))

if num1 == num2 :
    print(f"{num1}와 {num2}는 같다.")
elif num1 > num2 :
    print(f"{num1}가 {num2}보다 크다.")
else :
    print(f"{num1}는 {num2}보다 작다.")
