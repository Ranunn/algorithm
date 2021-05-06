'''
줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.
'''

# 문자가 아닌 숫자를 입력했을 경우엔 다시 입력하도록 작성함
while(True):
    a = input('첫 번째 문자를 입력하세요\n->')
    b = input('두 번째 문자를 입력하세요\n->')
    if(a.isalpha() & b.isalpha()):    # 결과가 True, False로 나옴
        break
    else:
        print('문자만 입력해주세요.')

print(b)
print(a)
