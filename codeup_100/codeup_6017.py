'''
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 공백을 두고 한 줄로 3번 출력해보자.
'''

data = input('출력하고자 하는 데이터를 입력해주세요\n->')

# 방법1
print(data, data, data)

# 방법2
print('{0} {0} {0}'.format(data))
