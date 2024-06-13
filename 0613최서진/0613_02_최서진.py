
'''
    학번을 입력받아 어느 학과 학생인지 알려주세요.
    학번은 학과 코드 영문자와 숫자로 구성되어 있습니다.

    예) C202095001
    [학과 코드]
    C : 컴퓨터공학과  A : 인공지능공학과   F : 식품영양학과

    입력받는 학과코드는 대소문자를 구분하지 않습니다.
    학과를 알려주는 부분은 함수로 작성하세요.

    [출력 결과]
        [학과 코드]
         C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과
        학번을 입력하세요 : c202095001 
        c202095001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : A202045001
        A202045001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : s202036001
        해당 학과는 없습니다.
'''
# 함수 선언
def hamsu() :

    A=["컴퓨터 공학과"]
    C=["인공지능 학과"]
    F=["식품 영양학과"]

    if "A"or"a" in name :
        print(f"{name}의 학과는 {A}입니다")
    elif "C"or"c" in name :
        print(f"{name}의 학과는 {C}입니다")
    elif "F"or"f" in name :
        print(f"{name}의 학과는 {F}입니다")
    else :
        print("없습니다")
        return(hamsu)
    
#메인
name = str((input("학번을 입력하세요 : ")))
hamsu()

# 시작하는 글자가 c이면
# starswitch(시작하는문자)
# endswitch(끝나는 문자)
if name.startswith("c") == True or name.startswith("c" == False) :
    print("컴공부")