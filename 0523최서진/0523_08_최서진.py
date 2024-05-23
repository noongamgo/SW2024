'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : readlines() 메소드 사용법 반복문으로 출력하기.
'''
print("== relines()메소드 이용하여 읽기 ==")

with open("text2.txt","r") as f :
    textlist = f.readlines() #파일에 있는 모든줄을 하나의 리스트로 만든다.

    for line in textlist :
        print(line)

# with open 을 사용하면 f.close()사용 x