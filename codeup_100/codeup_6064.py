'''
입력된 정수 3개 중 가장 작은 값을 3항 연산을 사용하여 출력하기

-----------------------------------------------------------
3개의 요소로 이루어지는 3항 연산은 x if C else Y 의 형태로 작성된다.
C : True 또는 False를 평가할 조건식(conditional exporession) 또는 값
x : C의 평가 결과가 True일 때 사용할 값
y : C의 평가 결과가 False일 때 사용할 값

-----------------------------------------------------------
입력예시
3 -1 5

출력예시
-1

'''

while(True):
    nums = input('정수 3개를 입력해주세요. (예) 123 456 32\n->')

    try:
        a, b, c = nums.split()
        a = int(a)
        b = int(b)
        c = int(c)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)

