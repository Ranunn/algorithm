'''
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력하기

평가 : 내용
 A  : Bese!!!
 B  : Good!!
 C  : Run!
 D  : Slowly~
 etc: what?

-----------------------------------------------------------
입력예시
A

출력예시
Best!!!

'''

# while(True):
#     a = input('평가를 입력해주세요. (예) A, B, C , D \n->')
#
#     try:
#         a = str(a)
#     except:
#         print('잘못 입력하였습니다.')
#         continue
#     else:
#         break


a = input('평가를 입력해주세요. (예) A, B, C , D \n->')

# 방법 1
if ( a == 'A'):
    print('Best!!!')
else:
    if ( a == 'B'):
        print('Good!!')
    else:
        if ( a == 'C'):
            print('Run!')
        else:
            if ( a == 'D'):
                print('Slowly~')
            else:
                print('what?')

# 방법 2
if ( a == 'A'):
    print('Best!!!')
elif ( a == 'B'):
    print('Good!!')
elif ( a == 'C'):
    print('Run!')
elif ( a == 'D'):
    print('Slowly~')
else:
    print('what?')
