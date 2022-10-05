def solution(s):
    # ( 갯수와 ) 갯수가 일치해야 하고, 마지막이 )로 끝나야하며 시작은 (로 되어야 함.
    # 위 조건이 틀리면 바로 False반환
    if s.count("(") != s.count(")"):
        return False
    if s[0]==")":
        return False
    if s[-1]=="(":
        return False
    cnt = 0
    for i in s:
        if cnt < 0:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    return True


'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (6.75ms, 10.2MB)
테스트 2 〉	통과 (0.61ms, 10.2MB)
'''