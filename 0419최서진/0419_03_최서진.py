'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 1부터 100사이의 수 중에서 2의 배수이면서
            3의 배수가 아닌수를 출력하시오
    
    [문제분석]
        2의 배수 = 2 * n
        3의 배수 = 3 * n
        (반복-선택)
            2의 배수를 100까지 출력 하면서
            3의 배수와 겹친다면 출력 x
    
    [알고리즘]
        1. 2의 배수를 2부터 100까지 반복한다.
            1-1. 반복한 수가 만약 3의 배수라면
                1-1-1. 결과를 출력 하지 않는다.
            1-2. 아니면
                1-2-1. 결과를 출력한다. 
'''
for dan in range(2,101,2) :
    if dan % 3 != 0 :
        print(dan, end = ', ')