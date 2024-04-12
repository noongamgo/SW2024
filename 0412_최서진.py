'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 단을 입력받아 해당 단을 출력하는 프로그램
    [문제분석]
        초기값은 곱하는수 1로한다.(su)
        단을 입력받는다.
        su는 9이하로 한다.
        초기값 su는 1씩 증가한다.

    [알고리즘]
        1.단을 입력 받는다. num
        2.곱하는 수는 1부터(초기값)
        3.곱하는 수는 9까지 반복하면서 (조건식)
            3-1. 구구단을 출력한다. 3 * 1 = 3
            3-2 곱하는 수는 1씩 증가한다. (증감식)

'''

dan = int(input('단을 입력하시오. : '))
su = 1

while su <= 9 :
    result = su * dan
    print(f'{dan} * {su}는 {result} 입니다.')
    print()
    su = su + 1
