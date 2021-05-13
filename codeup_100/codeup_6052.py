'''
정수가 입력되었을 때, 입력한 값이 0이면 True,
아닐 경우 False를 출력하기

-----------------------------------------------------------
bool()을 이용하면 입력된 식이나 값을 평가해볼 형의 값(True, False)를 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다. 

python 언어에서 정수값 0은 False(거짓)로 평가되고,
그 외의 값들은 모두 True(참)로 평가된다. 
-----------------------------------------------------------
입력예시
0

출력예시
False

'''

while(True):
    a = input('정수 1개를 입력해주세요. (예) 123 \n->')

    try:
        a = int(a)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

# 방법 1
print(a!=0)

# 방법 2
print(bool(a))
