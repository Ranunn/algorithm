'''
정수값이 입력될 떄,
그 bool값을 반대로 출력하기

-----------------------------------------------------------
bool()을 이용하면 입력된 식이나 값을 평가해볼 형의 값(True, False)를 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다.
-----------------------------------------------------------
bool 값이나 변수에 not True, not False, not a와 같은 계산이 가능하다. 
참 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word)를 사용할 수 있다. 
-----------------------------------------------------------
입력예시
0

출력예시
True

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
print(not(a!=0))

# 방법 2
print(not(bool(a)))
