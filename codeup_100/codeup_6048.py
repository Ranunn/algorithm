'''
정수 2개(a, n)를 입력받아 a가 b보다 작으면 True,
a가 b보다 크거나 같으면 False를 출력하기 (불리언으로 출력하기)

비교 연산자 less than sign <
-----------------------------------------------------------

입력예시
1 9

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

print(a<b)
