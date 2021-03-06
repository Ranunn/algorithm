'''
2개의 정수값이 입력될 때,
그 bool 값이 모두 True일 때에만 True 출력하기

-----------------------------------------------------------
bool()을 이용하면 입력된 식이나 값을 평가해볼 형의 값(True, False)를 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다.
-----------------------------------------------------------
bool 값이나 변수에 not True, not False, not a와 같은 계산이 가능하다.
참 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word)를 사용할 수 있다.
-----------------------------------------------------------
입력예시
1 0

출력예시
True

'''

while(True):
    nums = input('정수 2개를 입력해주세요. (예) 1 3 \n->')

    try:
        a, b = nums.split()
        a = int(a)
        b = int(b)
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

# 방법 1
print(a!=0 - b!=0)

# 방법 2
print(bool(a) or bool(b))
