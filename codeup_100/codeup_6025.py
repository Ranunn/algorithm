'''
정수 2개를 입력받아
합을 출력하기

입력예시
123 -123

출력예시
0

'''

while(True):
    data = input('숫자를 2개 입력해주세요. (예) 24 813\n->')

    try:
        d1, d2 = data.split()
    except:
        continue
    else:
        break
d = int(d1) + int(d2)
print(d)
