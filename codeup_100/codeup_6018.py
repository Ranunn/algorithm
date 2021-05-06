'''
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
'''

data = input('현재 시각을 입력해주세요. (예) 3:16\n->')
hour, minute = data.split(':')

# 방법1 (.format() 사용)
print('{}:{}'.format(hour,minute))

# 방법2 (sep='' 사용)
print(hour,minute,sep=':')
