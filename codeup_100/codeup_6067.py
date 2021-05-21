'''
0이 아닌 정수 1개가 입력되었을 때,
음(-) 양(+)과 짝(even), 홀(odd)을 구분해 분류하여 출력하기

음수이면서 짝수 : A
음수이면서 홀수 : B
양수이면서 짝수 : C
양수이면서 홀수 : D

-----------------------------------------------------------
입력예시
-214

출력예시
A

'''

while(True):
    a = input('0이 아닌 정수 1개를 입력해주세요. (예) 123 456 -32\n->')

    try:
        a = int(a)
        if (a != 0):
            pass
        else:
            print('잘못 입력하였습니다. 0은 입력할 수 없습니다.')
            continue
    except:
        print('잘못 입력하였습니다. 1개만 입력주세요.')
        continue
    else:
        break

if ((a<0) and (a %2 ==0)):
    print('A')
elif ((a<0) and (a %2 !=0)):
    print('B')
elif ((a>0) and (a %2 ==0)):
    print('C')
elif ((a>0) and (a %2 !=0)):
    print('D')
else:
    print('잘못된 입력입니다.')
