'''
    작성일 : 2024년 5월 10일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 튜플 => 한번 생성되면 그 값을 고칠수 없는 자료형
    
'''
# 튜플 생성.
colors1 = ('red','bule','green','orange')

print('corols1 = ' , colors1)

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.

print('색상 중 2,3,4번은?', colors1[1:4])
print('색상 거꾸러 출력 : ' , colors1[::-1])

# + 연산자, * 연산자 사용 가능
colors1 = colors1 + colors1
print('colors1 = ',colors1)
print('colors1 * 10 = ', colors1 * 10)

# colors1에 black 추가 => 튜플은 그값을 고칠수 없다.
colors2 = ('red','green','bule','orange','pink','white','white')
print('화이트 갯수 : ' , colors2.count('white'))
print('그린의 위치:' , colors2.index('green'))
# 튜플에서는 find 사용이 불가능

# 튜플은 생성된 후에 변경될수 없는 자료형이어서
# 제공되는 메소드가 두개뿐임 count,index 갑자기 코딩 개어려움
