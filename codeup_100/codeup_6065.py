'''
입력된 정수 3개 중 짝수만 출력하기

-----------------------------------------------------------
입력예시
1 2 4

출력예시
2
4

'''

while(True):
    nums = input('정수 3개를 입력해주세요. (예) 123 456 32\n->')

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

print(a if a%2 == 0 else '', end='')    # 홀수일 경우 줄바꿈 없이 출력되게 하기 위함
print(b if b%2 == 0 else '', end='')
print(c if c%2 == 0 else '', end='')

