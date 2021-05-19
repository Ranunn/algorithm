'''
입력된 정수 3개에 대해 짝(even), 홀(odd) 출력하기

-----------------------------------------------------------
입력예시
1 2 4

출력예시
odd
even
even

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

# 방법 1 ::: 정수별로 inline print문으로 출력
print('even' if a%2 == 0 else 'odd')
print('even' if b%2 == 0 else 'odd')
print('even' if c%2 == 0 else 'odd')

# 방법 2 ::: 정수를 모두 list에 담아 반복문으로 출력
lists = []
lists.append(a)
lists.append(b)
lists.append(c)

for i in lists:
    if (i%2 == 0) :
        print('even')
    else:
        print('odd')
