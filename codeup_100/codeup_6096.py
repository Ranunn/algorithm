
'''
부모님을 기다리던 영일인는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아놓고 놀다가...
"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 십자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19*19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여 있을 때,
n개의 좌료를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

참고)
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고,
더 확장한 n차원의 리스트도 만들 수 있다.

- 20개의 0이 들어간 리스트 만들기 1
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

- 20개의 0개 들어간 리스트 만들기 2 : List Comprehensions
d = [ [0 for j in range(20)] for i in range(20)]

...
입력)
바둑알이 깔려 있는 상황이 19*19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n)만큼 입력된다.
단, n은 10 이하의 자연수이다.

출력)
십자 뒤집기 결과를 출력한다.

...
입력 예시
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2
10 10
12 12

출력 예시
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0

'''

# 바둑판 역할을 할 2차원 리스트를 생성한다.
pan = [ [0 for j in range(20)] for i in range(20)]
pan[10][10] = 1
pan[10][12] = 1
pan[12][10] = 1
pan[12][12] = 1

# 개수를 입력받아 n에 정수로 저장
n = int(input('십자 뒤집기를 할 횟수를 입력해주세요.\n->'))
# n개의 좌표를 입력받아 2차원 리스트에 담는다.
for i in range(n):
    print(i, '번째 좌표 : ', end='')
    x,y = input('십자 뒤집기를 할 기준 좌표를 입력해주세요\n->').split()

    # 해당 좌표에서 십자 뒤집기 실행
    for j in range(1,20):
        if pan[j][int(y)] == 0:
            pan[j][int(y)] = 1
        else:
            pan[j][int(y)] = 0

        if pan[int(x)][j] == 0:
            pan[int(x)][j] = 1
        else:
            pan[int(x)][j] = 0

# 결과 출력
for i in range(1,20):
    for j in range(1,20):
        print(pan[i][j], end=' ')
    print()



