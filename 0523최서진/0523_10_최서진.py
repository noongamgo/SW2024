'''
    작성일 : 2024년 5월 23일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 학생 정보 입력된 파일의 내용을 출력하시오.

    [알고리즘]
        1.학생 이름과 성적을 읽어올 객체 생성
        2.반복하면서 내용 읽어오기
            2-1. 출력하기
    읽기 => readline() => while true
'''

with open("text3.txt","r") as f:
    while True :
        student = f.readline

        if student == '' :
            break