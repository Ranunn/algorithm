'''
정수 2개(a, b)를 입력받아 a와 b의 값이 크거나 같으면  True,
같지 않으면 False를 출력하기 (불로 출력하기)

-----------------------------------------------------------

입력예시
0 0

출력예시
True

'''

while(True):
    num = input('정수 2개를 입력해주세요. (예) 123 456 \n->')

    try:
        a, b = num.split()
        a = int(a)
        b = int(b)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(a>=b)
