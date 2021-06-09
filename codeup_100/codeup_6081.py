'''
A,B,C,D,E,F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력하기
(단, A~f 까지만 입력된다.)

-----------------------------------------------------------
입력예시
B

출력예시
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5

'''

flag = True
while(flag):
    txt = input('A~F 중 하나를 입력해주세요\n->')
    try:
        test = ord(txt)
        if (test > 64 and test < 71):
            num = int(txt, 16)
            pass
        else:
            continue
    except:
        print('잘못된 입력입니다.')
    else:
        flag = False


# print('%X' %num)
hexadecimal = int('F', 16)
# print('%X' %hexadecimal)

for i in range(1, hexadecimal+1, 1):
    print('{0}*{1}={2}'.format('%X'%num, '%X'%i, '%X'%(num*i)))

