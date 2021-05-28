'''
정수 (0~100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 출력하기


-----------------------------------------------------------
입력예시
5

출력예시
6

'''

hap = 0
num = int(input('정수 (0~100) 1개를 입력해주세요.\n->'))

# 방법 1
for i in range(num+1):
    if (i%2 ==0):
        hap += i
print(hap)

# 방법 2
hap = 0
inc = 0
num = int(input('정수 (0~100) 1개를 입력해주세요.\n->'))
while(inc<=num):
    if (inc%2 ==0):
        hap += inc
    inc += 1
print(hap)
