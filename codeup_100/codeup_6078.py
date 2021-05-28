'''
영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하기


-----------------------------------------------------------
입력예시
x
b
k
d
l
q
g
a
c

출력예시
x
b
k
d
l
q

'''

# 방법 1 - 루프 안에서 q가 입력되면 flag가 바뀌면서 빠져나옴
flag = True
while(flag):
    txt = input('영문 소문자를 입력해주세요.\n->')
    if (txt != 'q'):
        print(txt)
    else:
        print(txt)
        flag = False

# 방법 2 - 루프 안에서 ascii 코드를 사용하여 영문 소문자인지 판별하는 과정을 추가
flag = True
while(flag):
    txt = input('영문 소문자를 입력해주세요.\n->')
    try:
        num = ord(txt)
        if (num>96 and num<123):
            pass
        else:
            print('영문 소문자가 아닙니다.')
            continue
    except:
        print('다시 입력해주세요.')
    else:
        if (num != 113):
            print(txt)
        else:
            print(txt)
            flag = False
