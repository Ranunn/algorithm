'''
정수(integer)는
양의 정수(1, 2, 3, 4, 5, ...), 음의 정수(-1, -2, -3, -4, -5, ...), 0 과 같이
소숫점 아래에 수가 없는 수라고 할 수 있다.

변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.
'''

# 방법1
data = input('숫자를 입력하세요\n->')
print(int(data))
print(type(data))
print(type(int(data)))

# 방법2
data = input('숫자를 입력하세요\n->')
int_data = int(data)
print(int_data)
print(type(int_data))
