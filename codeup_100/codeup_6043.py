'''
실수 2개(f1, f2)를 입력받아 f1을 f2로 나눈 값을 출력하되,
소숫점 넷째자리에서 반올림하여 소숫점 셋째자리까지 출력하기

-----------------------------------------------------------

입력예시
10.0 3.0

출력예시
3.333

'''

while(True):
    nums = input('실수 2개를 입력해주세요. (예) 10.0 3.0\n->')

    try:
        a, b = nums.split()
        f1 = float(a)
        f2 = float(b)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

result = f1 / f2
print(format(result, ".3f")) # 원하는 자릿수만큼 지정

