'''
CCC 2014 Junior Division 4번
CCC 2014 Senior Division 1번


You are hosting a party and do not have room to invite all of your friends.

You use the following unemotional mathematical method
to determine which friends to invite.

Number your friends 1, 2, . . . , K and place them in a list in this order.
Then perform m rounds.
In each round, use a number to determine
which friends to remove from the ordered list.

The rounds will use numbers r1, r2, . . . , rm.
In round i remove all the remaining people
in positions that are multiples of ri (that is, ri, 2ri, 3ri, . . .)
The beginning of the list is position 1.

Output the numbers of the friends that remain after this removal process.

....
입력)
The first line of input contains the integer K (1 ≤ K ≤ 100).
The second line of input contains the integer m (1 ≤ m ≤ 10),
which is the number of rounds of removal.
The next m lines each contain one integer.
The ith of these lines (1 ≤ i ≤ m) contains ri (2 ≤ ri ≤ 100)
indicating that every person at a position
which is multiple of ri should be removed.

....
출력)
The output is the integers assigned to friends who were not removed.
One integer is printed per line in increasing sorted order.

....
예제 입력 1)
10
2
2
3

....
예제 출력 1)
1
3
7
9
'''

import sys
from collections import deque

# 친구들이 총 몇 명인지 입력받는다.
k = int(sys.stdin.readline())
friends = []
for i in range(k):
    friends.append(i+1)

# 제거 프로세스를 수행할 횟수를 입력받는다.
m = int(sys.stdin.readline())

# 제거 위치로 사용할 정수를 프로세스 횟수만큼 입력받아 수행한다.
for i in range(m):
    r = int(input())
    # 배열에서 정수의 배수 위치에 따라 제거할 친구와 남길 친구들을 구분한다.
    throw = []
    remain = []
    while(len(friends)>0):
        # r번째 배수에 해당하면 제거 리스트로 이동
        if (len(friends) % r == 0):
            throw.append(friends.pop())
        # 배수에 해당하지 않을 경우 유지 리스트로 이동
        else:
            remain.append(friends.pop())
    # 남겨진 친구 목록을 업데이트하여 다음 프로세스로 들어간다. 
    friends = remain
    friends.sort()

# 최종 초대할 친구들의 순번을 출력한다. 
friends.sort()
for i in friends:
    print(i)
