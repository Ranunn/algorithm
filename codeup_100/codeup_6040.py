'''
정수 2개(a, b)를 입력받아 a를 b로 나눈 몫을 출력하기

-----------------------------------------------------------

입력예시
10 3

출력예시
3

'''

multiple = 1

while(True):
    ints = input('나누기할 정수를 입력해주세요. (예) 10 3\n->')
    floats = input('나누기할 실수를 입력해주세요. (예) 10.0 3.0\n->')

    try:
        a, b = ints.split()
        a = int(a)
        b = int(b)
        f1, f2 = floats.split()
        f1 = float(f1)
        f2 = float(f2)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(a // b)   # 정수로 떨어지는 몫만 출력
print(f1 // f2) # 실수로 떨어지는 몫만 출력

# 비고
print(a / b)    # 몫을 소수점까지 출력
print(f1 / f2)  # 몫을 소수점까지 출력

