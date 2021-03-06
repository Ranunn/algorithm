
'''
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다.
미르코는 30이란 수를 존경하기 때문에,
그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

...
입력)
N을 입력받는다.
N은 최대 10^5개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

출력)
미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라.
그 수가 존재하지 않는다면 -1을 출력하라.

...
입력 예시 1
30

출력 예시 1
30

입력 예시 2
102

출력 예시 2
210

입력 예시 3
2931

출력 예시 3
-1

입력 예시 4
80875542

출력 예시 4
88755420

'''

#길거리에서 발견한 양수 N을 입력받는다.
n = input()
sum = 0

# N을 내림차순 정렬한다.
n = sorted(n, reverse=True)

# 30의 배수이려면 1의 자리에 항상 0이 올 수 있어야 한다.
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))




