'''
실수 2개를 입력받아
합을 출력하기

입력예시
0.1 0.9

출력예시
1.0

'''

while(True):
    data = input('실수를 2개 입력해주세요. (예) 0.9 0.1\n->')

    try:
        d1, d2 = data.split()
    except:
        continue
    else:
        break
d = float(d1) + float(d2)
print(d)
