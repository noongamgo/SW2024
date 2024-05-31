'''
1.함수
    2)전달받은 값 함수 선언
    3) 두수의 합을 변수에 저장
    4) 변수 리턴
2.메인
    1) 두 수를 입력
    5) 함수 출력    
    
    
'''
#함수 선언
def result(num1,num2) :
    result = num1 + num2
    return(result)
#메인
num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))
print(result(num1,num2))

print("======== 2번 문제 =============")
'''
[알고리즘]
1.함수
    2) 전달받은 값 함수선언
    3) 만약 짝수라면
        3-1) 짝수 리턴
    4) 아니면
        4-1) 홀수리턴
2. 메인
    1) 정수입력
    5) 함수 출력
'''
#함수 선언
def su(num) :
    if num % 2 ==0 :
        return("짝수")
    else :
        return("홀수")
#메인
num = int(input("정수입력 : "))
print(su(num))