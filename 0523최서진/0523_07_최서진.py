'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : readlines() 메소드 사용법
'''
print("== relines()메소드 이용하여 읽기 ==")

# readlines() 메소드는 파일로부터 읽어들인 한 줄을 리스트의 한 항목으로 만든다.

# readline() 메소드와 다른점은 각각줄을 읽어 리스트로 반환한다.

# with open 을 이용하여 쓰기 모드로 파일 객체 생성


with open("text2.txt","r") as f :
    textlist = f.readlines() #파일에 있는 모든줄을 하나의 리스트로 만든다.
    print(textlist)
    print('textlist 의 자료형 출력 : ',type(textlist))
# with open 을 사용하면 f.close()사용 x