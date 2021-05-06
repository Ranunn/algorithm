'''
줄을 바꿔 출력하기

Hello
World 
'''

# 방법1 - print() 함수를 2번 호출
print('Hello')
print('World')

# 방법2 - \n으로 줄 바꿈
print('Hello \nWorld')

# 방법3 - \n을 사용하는 동시에 .format옵션 적용
print('{0} \n{1}'.format('Hello', 'World'))
