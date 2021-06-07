'''
1부터 n까지 정수를 계속 더해 나갈 때,
입력한 수보다 같거나 커지는 지점을 출력하기


-----------------------------------------------------------
입력예시
55

출력예시
10

'''

flag = True
while(flag):
    txt = input('정수 1개를 입력해주세요\n->')
    try:
        num = int(txt)
    except:
        print('잘못된 입력입니다.')
    else:
        flag = False

sum = 0
cnt = 0
while(sum < num):
    cnt += 1
    sum += cnt
print('마지막에 더한 정수 : ', cnt)
