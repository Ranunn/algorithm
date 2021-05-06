'''
공백을 두고 문자(character) 2개를 입력받아 줄을 바꿔 출력해보자.
'''

# 잘못 입력했을 경우 다시 시작하기 위한 반복문
while(True):
    data = input('문자를 2개 입력하세요. (예) a b\n->')

    # 문자의 갯수가 2개가 아닐 때 발생하는 에러를 방지하기 위함
    try:
        a, b = data.split()
    except:
        print('문자 갯수를 잘못 입력하였습니다. 다시 입력해주세요.')
        continue

    # 모두 문자가 맞는지 확인
    if(a.isalpha() & b.isalpha()):
        break
    else:
        print('잘못 입력하였습니다. 다시 입력해주세요.')

print(b)
print(a)
