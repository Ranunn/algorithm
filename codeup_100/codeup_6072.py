'''
정수 (1~100) 1개가 입력되었을 때 카운트다운을 출력하기


-----------------------------------------------------------
입력예시
5

출력예시
5
4
3
2
1

'''

# 방법 1
while(True):
    num = input('1. 카운트다운을 시작할 정수(1~100)를 입력해주세요\n->')

    try:
        num = int(num)
        if(num<1):
            print('너무 작은 숫자입니다.')
            continue
        elif(num>100):
            print('너무 큰 숫자입니다.')
            continue
        else:
            pass
        for i in range(num, 0, -1):
            print(i)
        break
    except:
        print('숫자를 입력해주세요!')
    else:
        pass


# 방법 2
while(True):
    n = (input('2. 카운트다운을 시작할 정수(1~100)를 입력해주세요\n->'))
    try:
        n = int(n)
        if(n<0):
            print('너무 작은 숫자입니다.')
            continue
        elif(n>100):
            print('너무 큰 숫자입니다.')
            continue
        else:
            pass
    except:
        print('잘못된 입력입니다.')
    else:
        while(n!=0):
            print(n)
            n = n-1
        break

