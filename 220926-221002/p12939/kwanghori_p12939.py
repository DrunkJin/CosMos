def solution(s):
    answer = ''
    tmp = [int(i) for i in s.split()]   # 입력값 숫자로 분리
    answer = f'{min(tmp)} {max(tmp)}'   # f-string 이용
    return answer
