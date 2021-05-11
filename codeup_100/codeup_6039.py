'''
실수 2개(f1, f2)를 입력받아 f1를 f2번 곱한 거듭제곱을 출력하기

-----------------------------------------------------------

입력예시
4.0 2.0

출력예시
16.0

'''

multiple = 1

while(True):
    data = input('거듭제곱할 수를 입력해주세요. (예) 4.0 2.0\n->')

    try:
        f1, f2 = data.split()
        f1 = float(f1)
        f2 = float(f2)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(f1 ** f2)


