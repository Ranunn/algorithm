'''
정수 3개를 입력받아 합과 평균을 출력하기

-----------------------------------------------------------

입력예시
1 2 3

출력예시
6 2.00
'''

while(True):
    nums = input('정수 3개를 입력해주세요. (예) 1 2 3\n->')

    try:
        a, b, c = nums.split()
        a = int(a)
        b = int(b)
        c = int(c)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

sum = a + b + c
print(sum, format(sum / 3, ".2f"))
