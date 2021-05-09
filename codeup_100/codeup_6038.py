'''
정수 2개(a,b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하기

-----------------------------------------------------------

입력예시
2 10

출력예시
1024

'''

multiple = 1
print(type(multiple))

while(True):
    data = input('거듭제곱할 수를 입력해주세요. (예) 2 10\n->')

    try:
        a,b = data.split()
        a = int(a)
        b = int(b)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(a ** b)


