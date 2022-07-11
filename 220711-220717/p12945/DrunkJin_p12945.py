def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    pp = 0
    p = 1
    answer = 0
    
    for _ in range(2, n+1): # 2부터 n까지 반복하며 피보나치 수열 수행
        answer = pp + p
        pp = p
        p = answer

    answer %= 1234567     # answer를 1234567로 나눈 나머지를 answer에 저장
    return answer


    """
    
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.20ms, 10.1MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.12ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (83.55ms, 10.3MB)
테스트 14 〉	통과 (80.77ms, 10.3MB)
    
    """