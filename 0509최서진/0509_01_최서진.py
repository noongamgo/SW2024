'''
    작성일 : 2024년 5월 9일
    작성자 : 202495021 최서진 컴공
    설명 : 시퀀스 자료형 - 문자열
'''
# 문자열 생성
text1 = '안녕하세요.'

#빈 문자열 생성.
text2 = ''
text3 = str() # str()함수를 사용하여 빈 문자열 생성

text4 = '오늘은 "목요일" 입니다.'
print(text4)
'''
    str()함수를 사용하여 다른 자료형(숫자, 리스트, 튜플)을
    문자열로 변환하여 새로운 문자열 생성.
'''
text5 = str(12345)
print(f"text5 = {text5}")
print(f"text5의 자료형 : {type(text5)}")

# 리스트[]를 문자열로 생성.
text6 = str([1,2,3])
print(f"text6 = {type(text6)}")

print(f'text6[1] = {text6[1]}') #결과 [
    
# 튜플()을 문자열로 생ㅇ.
text7 = str((1,2,3))
print(f'text7 = {text7}')

print(f'text7[2] = {text7[2]}')

'''
    대소문자 변환
'''
text8 = 'i like python language'
print(text8)

#첫문자만 대문자로 변환
print(text8.capitalize())
print(f'모든 단어의 첫 문자를 대문자로 변환{text8.title()}')
text9 = text8.upper()
print(f'모두 대문자로 변환{text9}')
text10 = text9.lower()
print(f'모두 소문자로 변환{text10}')
'''
    문자열 찾기
'''
print(text10)
print(f'문자열에 a가 몇개 있습니까{text10.count("a")}')
print(f'문자열 인덱스 0번지 부터 12번지 사이에 "a" 가 몇개{text10.count("a",1 ,12)}')
print(text10.index("l"))
print(text10.find("l"))
print(text10.rfind("l"))
print(text8.index("python"))
print(text8.find('Python'))

# 문자열 리스트 생성
list1 = ['1','2','3','4']
print(f'list1 = {list1}')

#리스트에 있는 문자열을 '-'와 결합
join1 = '-'.join(list1)
print(join1)


#join은 문자열만 가능하다

'''
문자열 분리
'''
text10 = 'i like python languge'
print(text10)

#문자열을 스페이스로 구분하여 리스트로 변환
list3 = text10.split()
print(list3)
text11= 'i-like-python-languge'
print(text11)
list4 = text11.split("-")

'''
    문자열 변환.
'''
# 'python'을 기준으로 문자열을 나누어 튜플로 변환.
tuple1 = text10.partition("python")
print(tuple1)
print('like를 love로 대체',text10.replace('like','love'))

text12 = 'I Like Python Language'
print("모든 단어읏 문자가 대문자인가? ", text12.istitle())
text13 = 'abc123'
print('문자열이 순자와 문자로 구성되어 있나?', text13.isalnum())
text14 = '1234567890'
print('문자열이 숫자로만 구성되어 있나?', text14.isdigit())
print('문자열이 문자로만 구성되어 있나?', text14.isalpha())

print('모든 문자가 대문자인가?', text12.isupper())
print('모든 문자가 소문자인가?', text12.islower())