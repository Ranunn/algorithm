'''
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 출력하기
단, 0 <= a, b <= 214783647 이고 b는 0이 아니다.

-----------------------------------------------------------

입력예시
10.0 3.0

출력예시
13
7
30
3
1
3.33

'''

while(True):
    nums = input('정수 2개를 입력해주세요. (예) 10 3\n->')

    try:
        a, b = nums.split()
        a = int(a)
        b = int(b)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(a + b)  # 합
print(a - b)  # 차
print(a * b)  # 곱
print(a // b) # 몫
print(a % b)  # 나머지
print(format(a / b, ".2f"))  # 나눈 값(소숫점 이하 둘째자리까지)

