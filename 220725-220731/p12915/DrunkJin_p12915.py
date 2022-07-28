def solution(strings, n):
    strings = sorted(strings)                   # 1차 정렬 : (abce, abcd) => (abcd, abce)
    answer = sorted(strings, key=lambda x:x[n]) # 2차 정렬 : 정렬되어있던 strings에서 x[n] 인덱스를 기준으로 재정렬 -> 동일한 경우 1차 정렬 순서대로 들어가게됨
    return answer

    """
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 9.98MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 9.98MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
    """