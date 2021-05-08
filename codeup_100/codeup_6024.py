'''
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하기

입력예시
hello world

출력예시
helloworld

'''

while(True):
    data = input('단어를 2개 입력해주세요. (예) hello world\n->')

    try:
        d1, d2 = data.split()
    except:
        continue
    else:
        break
        
d = d1+ d2
print(d)
