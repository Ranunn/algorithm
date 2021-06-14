'''
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다르색 빛을 만들어 내려고 한다.
빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 떄,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓수를 구하자.

빨녹파(r, g, b) 각 빛의 가짓수가 공백을 두고 입력된다.
예를 들어, 3 3 3은 빨녹파 빛에 대하여 각각 0~2까지 3가지 색이 있음을 의미한다.
0 <= r,g,b <= 127

만들 수 있는 rgb 색의 정보를 오름차순으로 줄을 바꿔 모두 출력하고,
마지막에 그 갯수를 출력한다.

-----------------------------------------------------------
입력예시
2 2 2

출력예시
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8

'''

flag = True
while(flag):
    txt = input('숫자를 입력해주세요\n->')
    try:
        r,g,b = txt.split()
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        print('잘못된 입력입니다.')
    else:
        flag = False

cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            cnt += 1
print(cnt)


