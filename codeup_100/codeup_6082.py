'''
친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 3 6 9 마스터 프로그램을 작성해보자.

1부터 특정 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함되어 있는 수인 경우, 그 수 대신 영문 대문자 X를 출력한다.

-----------------------------------------------------------
입력예시
9

출력예시
1 2 X 4 5 X 7 8 X

'''

flag = True
while(flag):
    txt = input('숫자를 입력해주세요\n->')
    try:
        num = int(txt)
    except:
        print('잘못된 입력입니다.')
    else:
        flag = False


for i in range(1, num+1):
    i = str(i)
    if '3' in i:
        print('X', end=' ')
    elif '6' in i:
        print('X', end=' ')
    elif '9' in i:
        print('X', end=' ')
    else:
        print(i, end=' ')
