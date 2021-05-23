'''
점수 (정수, 0 ~ 100)를 입력받아 평가를 출력하기

점수 범위 : 평가
90 ~ 100 : A
70 ~ 89  : B
40 ~ 69  : C
 0 ~ 39  : D

-----------------------------------------------------------
입력예시
73

출력예시
B

'''

while(True):
    a = input('점수를 입력해주세요. (예) 0 ~ 100 사이의 정수\n->')

    try:
        a = int(a)
        if (a <= 100 and a >=0 ):
            pass
        else:
            print('잘못 입력하였습니다.')
            continue
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

# 방법 1
if ( a>= 90 ):
    print('A')
else:
    if ( a>= 70):
        print('B')
    else:
        if ( a >= 40):
            print('C')
        else:
            print('D')

# 방법 2
if (a>=90):
    print('A')
elif (a>=70 and a<90):
    print('B')
elif (a>=40 and a<70):
    print('C')
else:
    print('D')
