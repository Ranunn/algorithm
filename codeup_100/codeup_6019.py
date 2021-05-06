'''
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
'''

while(True):
    data = input('오늘 날짜를 입력해주세요. (예) 2020.3.4\n->')
    try:
        year, month, day = data.split('.')
    except:
        print('잘못 입력하였습니다.')
        continue
    else:
        break

# 방법1 (.format() 사용)
print('{}-{}-{}'.format(day,month,year))

# 방법2 (sep='' 사용)
print(day,month,year,sep='-')
