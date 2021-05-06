'''
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.
'''

# 숫자가 아닌 문자를 입력했을 경우엔 다시 입력하도록 작성함
while(True):
    a = input('숫자를 입력하세요\n->')
    if(a.isalpha()):    # 결과가 True, False로 나옴
        print('숫자만 입력해주세요.')
    else:
        # 실수타입으로 형 변환 후 while 문 빠져나가기
        a = float(a)
        break

# 3회 줄 바꿔 출력
for num in range(3):
    print(a)
