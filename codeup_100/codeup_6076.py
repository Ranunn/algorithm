'''
정수 (0~100) 1개를 입력받아 0부터 그 수까지 순서대로 출력하기


-----------------------------------------------------------
입력예시
4

출력예시
0
1
2
3
4

'''


num = int(input('정수 (0~100) 1개를 입력해주세요.\n->'))
for i in range(num+1):
    print(i)

