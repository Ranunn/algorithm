'''
숫자(0~9)와 소수점(.)을 사용해 표현한 수를 실수(real number)라고 한다.

변수에 실수값을 저장한 후
변수에 저장되어 있는 값을 그대로 출력해보자.
'''

# 방법1
data = input('숫자를 입력하세요\n->')
print(float(data))
print(type(data))
print(type(float(data)))

# 방법2
data = input('숫자를 입력하세요\n->')
float_data = float(data)
print(float_data)
print(type(float_data))
