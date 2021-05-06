'''
줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
'''

# 숫자가 아닌 문자를 입력했을 경우엔 다시 입력하도록 작성함
while(True):
    a = input('첫 번째 숫자를 입력하세요\n->')
    b = input('두 번째 숫자를 입력하세요\n->')
    if(a.isdigit() & b.isdigit()):    # 결과가 True, False로 나옴
        break
    else:
        print('숫자만 입력해주세요.')

print(int(a))
print(int(b))
