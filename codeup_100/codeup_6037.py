'''
줄을 바꿔 입력된 문장과 반복 횟수대로 여러 번 출력하기

-----------------------------------------------------------

입력예시
3
I love CS

출력예시
I love CSI love CSI love CS

'''

while(True):
    repeat = input('반복할 횟수를 입력해주세요. (예) 3\n->')
    sentence = input('반복할 문장을 입력해주세요. (예) I love CS\n->')

    try:
        c = str(sentence) * int(repeat) # 조건대로 입력된 것인지 확인
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print(c)


