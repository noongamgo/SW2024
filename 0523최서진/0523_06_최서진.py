'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : readline() 메소드 사용법
'''
print("== reline()메소드 이용하여 읽기 ==")

# readline() 메소드는 주로 while문과 사용
# with open 을 이용하여 쓰기 모드로 파일 객체 생성
with open("text2.txt","r") as f :
    #while문을 사용하여 무한반복
    while True :
        line = f.readline() #한줄씩 읽어와서 변수에 저장
        print(line) # 내용 출력

        if line == '' : # 읽어온 값이 없는경우 반복을 브레이크.
            break
    
# with open 을 사용하면 f.close()사용 x