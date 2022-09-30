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
