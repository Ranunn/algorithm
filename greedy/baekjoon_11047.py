
'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이 때 필요한 동전 갯수의 최솟값을 구하는 프로그램을 작성하시오.


...
입력)
첫째 줄에 N과 K가 주어진다. (1≤N≤10, 1≤K≤100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력)
첫째 줄에 K원을 만드는데 필요한 동전 갯수의 최솟값을 출력한다.

...
입력 예시 1
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

출력 예시 1
6

입력 예시 2
10 4790
1
5
10
50
100
500
1000
5000
10000
50000

출력 예시 2
12

'''


###### 시간조건을 충족한 방법
n, k = input().split()
n = int(n)
k = int(k)

gachi = []
for i in range(n):
    gachi.append(int(input()))
    
su = 0
for i in range(n-1, -1, -1):
    su += k // gachi[i]
    k %= gachi[i]

print(su)


###### 예외처리를 적용한 방법
# 동전의 종류와 합계에 해당하는 금액을 입력한다.
flag = True
while(flag):
    try:
        n, k = input('동전의 종류와 최종합계금액을 입력해주세요.(ex. 10 4200)\n->').split()
    except:
        print('잘못된 입력입니다.')
        continue
    else:
        n = int(n)
        k = int(k)
        if n>=1 and n<=10 and k>=1 and k<=100000000:
            flag = False
        else:
            print('1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000만 가능합니다.')
            continue

# 동전의 가치를 입력받아 리스트에 담는다.
gachi = []
for i in range(n):
    print(i+1, '번째 동전의 가치 : ', end='')
    flag = True
    while(flag):
        try:
            txt = int(input())
        except:
            print('동전 1개의 가치만 입력해주세요.\n->')
            continue
        else:
            gachi.append(txt)
            flag = False

# 리스트에 있는 동전을 금액이 작은 순서대로 정렬한다.
gachi.sort()

# 가치가 큰 동전부터 사용하여 최종합계금액을 나누어 동전갯수를 별도의 리스트에 담는다.
su = []
while(k!=0):
    for i in range(n-1, 0, -1):
        moc = k / gachi[i]
        if moc >= 1:
            try:
                moc = int(moc)
            except:
                su.append(0)
            else:
                su.append(moc)
                k -= moc*gachi[i]
        else:
            su.append(0)

# 동전의 갯수를 합산하여 출력한다. 
print(sum(su))



