'''
문자 1개를 입력받아 그 다음 문자를 출력하기

-----------------------------------------------------------

입력예시
A

출력예시
B

'''

data = input('문자 또는 숫자를 1개 입력해주세요.\n->')

try:    # 문자를 입력했을 경우 ord()를 사용하여 정수로 변환 후 1 더하기
    n = ord(data) + 1
except: # 숫자를 입력했을 경우 정수형으로 변환 후 1 더하기
    n = int(data) + 1
    print(n)
else:   # try를 통과했을 경우
    print(chr(n))


