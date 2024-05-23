'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : for문을 이용하여 읽어오기
'''
print("== for문을 이용하여 읽기 ==")
# with open 을 이용하여 쓰기 모드로 파일 객체 생성
with open("text2.txt","r") as f :
    for line in f : #for문에 파일 객체를 지정하여 한 줄씩 반복하여 읽어온다
        print(line)
#with open 을 사용하면 f.close()사용 x