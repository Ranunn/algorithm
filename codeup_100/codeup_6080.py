'''
1부터 n까지, 1부터 m까지 숫자가 적인 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력하기


-----------------------------------------------------------
입력예시
2 3

출력예시
1 1
1 2
1 3
2 1
2 2
2 3

'''

flag = True
while(flag):
    txt = input('정수 2개를 입력해주세요\n->')
    try:
        num1, num2 = txt.split()
        num1 = int(num1)
        num2 = int(num2)
    except:
        print('잘못된 입력입니다.')
    else:
        flag = False

for i in range(1, num1+1, 1):
    for j in range(1, num2+1, 1):
        print(i, j)
