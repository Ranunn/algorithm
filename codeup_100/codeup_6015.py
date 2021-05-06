'''
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
'''

# 숫자가 아닌 문자를 입력했을 경우엔 다시 입력하도록 반복문 시작
while(True):
    nums = input('숫자를 2개 입력하세요. (예) 3 5\n->')

    # 2개의 숫자를 입력하지 않았을 때 에러 방지하기 위함
    try:
        a, b = nums.split()
    except:
        print('숫자 갯수를 잘못 입력하였습니다. 다시 입력해주세요.')
        continue

    # 모두 숫자가 맞는지 확인
    if(a.isalpha() | b.isalpha()):
        print('잘못 입력하였습니다. 다시 입력해주세요.')
    else:
        # 실수타입으로 형 변환 후 while 문 종료
        a = int(a)
        b = int(b)
        break

print(a)
print(b)
