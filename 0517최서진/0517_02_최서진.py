'''
    작성일 : 2024년 5월 17일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 다섯명의 학생 정보를 입력 받는다.
            이름과 전화번호를 입력 받는다.

    


'''
# 빈 딕셔너리 생성
phone = {}

# 6번 반복하면서
for i in range(5) : 
    # 이름을 입력하시오.
    name = input(str(i+1) + '반학생의 이름을 입력하시오 :')
    # 전화번호를 입력사이오
    phone_num = input(str(i+1) + '반학생의 전화번호를 입력하시오 :')

    #딕셔너리에 이름과 전화번호 저장.
    phone[name] = phone_num
print('학생 전화번호 부가 완성 되었습니다.')
print()

for key in phone.keys() :
    print(key,":",phone[key])
# 학생 검색
# 학생 이름을 입력하면 해당 학생의 전화번호를 출력하시오.
# 만약 학생이름이 없으면'입력한 학생의 전화번호가 없습니다' 를 출력
# 무한반복 단 0을 입력시 종료
while True :
    name = input('검색을 원하는 합생이름 입력 (종료 : 0)')
    if name == '0' :
        print('종료')
        break
    else :
        # 이름이 전화번호부에 있으면
        if name in phone :
            print(phone[name])

        else : 
            print('입력한 학생의 전화번호 없음')