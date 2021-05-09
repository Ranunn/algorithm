'''
단어와 반복 횟수를 입력받아 여러 번 출력하기

-----------------------------------------------------------

입력예시
love 3

출력예시
lovelovelove

'''

while(True):
    data = input('단어 1개와 반복할 횟수를 입력해주세요. (예) love 3\n->')

    try:
        a, b = data.split() # 2개의 데이터를 입력했는지 확인
        c = str(a) * int(b) # 조건대로 입력된 것인지 확인
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(c)


