'''
10진수를 입력받아 16진수(hexadecimal)로 출력하기
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
0 1 2 3 4 5 6 7 8 9 A  B  C  D  E  F  10 11
입력예시
255

출력예시
ff

'''

data = input('10진수를 입력해주세요.\n->')
decimal = int(data)
print('%x' %decimal)