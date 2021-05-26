'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력하기


-----------------------------------------------------------
입력예시
f

출력예시
a b c d e f

'''

# 방법 1
txt = ord(input('영문 소문자 1개를 입력해주세요\n->'))
alpha = [chr(i) for i in range(97, txt+1)]
print(*alpha)


# 방법 2
txt = ord(input('영문 소문자 1개를 입력해주세요\n->'))
alpha = ord('a')

while(alpha <= txt):
    print(chr(alpha), end=' ')
    alpha += 1

