'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 2단부터 9단까지 구구단을 계산하는 코드를 작성하시오


    [문제분석]
        단 하나에 1 ~ 9까지 반복
        2단을 반복하고 3단을 반복하며 9단까지 반복 한다.(반복-반복 이중 사용)
        9단의 9까지 곱하고 나면 프로그램을 종료

    [알고리즘]
        1.단은 2단부터 9단까지 반복
            1-1.곱하는 수는 1부터 9까지 반복한다.
                1-1-1. 단 * 수 = 결과출력


'''
for dan in range(2, 10) :
    for su in range(1, 10) :
        print(f"{dan} * {su} = {dan * su}")