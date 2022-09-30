def solution(s):
    cvt = 0     # 이진 변환 횟수
    zero_cnt = 0    # 제거된 0 갯수
    
    while s != '1':   # 입력값이 '1'이 되는 순간 loof 종료
        zero_cnt += s.count('0')    # 제거전 0 갯수 카운트
        cnt = s.count('1')    # 1 갯수 카운트
        s = '1' * cnt     # 갯수만큼 '1' 생성
        l = len(s)
        s = bin(l)[2:]
        cvt += 1
        
    return cvt, zero_cnt



테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.40ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.32ms, 10.4MB)
테스트 10 〉	통과 (1.02ms, 10.2MB)
테스트 11 〉	통과 (0.49ms, 10.2MB)
