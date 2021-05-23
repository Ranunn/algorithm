'''
월이 입력될 때 계절 이름을 출력하기

 월 : 계절 이름
 12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9,10,11 : fall

-----------------------------------------------------------
입력예시
12

출력예시
winter

'''

while(True):
    a = input('월을 입력해주세요. (예) 1, 2, 3, ... 11, 12 \n->')

    try:
        a = int(a)
        if (a>0 and a<13):
            pass
        else:
            print('범위가 잘못되었습니다.')
            continue
    except:
        print('정수가 아닙니다.')
        continue
    else:
        break


# 방법 1
if (a // 3 == 1):
    print('spring')
else:
    if (a // 3 == 2):
        print('summer')
    else:
        if ( a // 3 == 3):
            print('fall')
        else:
            print('winter')

# 방법 2
if ( a >= 3 and a < 6):
    print('spring')
elif ( a >= 6 and a < 9):
    print('summer')
elif ( a >= 9 and a < 12):
    print('fall')
else:
    print('winter')
