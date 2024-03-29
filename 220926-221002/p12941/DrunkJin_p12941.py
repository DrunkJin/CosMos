def solution(A,B):
    # 이후 삭제를 빠르게 하기 위한 로직
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer = 0
    for _ in range(len(A)):
        # 최소값을 구하려면 각 리스트에서 최소, 최대 값을 서로 곱해주어야함
        temp = A[0] *B[0]
        answer += temp
        #  remove, A[1:] 등등 탐색이 필요한 로직은 효율성에서 걸렸다. 시간복잡도 문제 발생
        A.pop(0)
        B.pop(0)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.08ms, 10.1MB)
테스트 5 〉	통과 (0.09ms, 10MB)
테스트 6 〉	통과 (0.09ms, 9.97MB)
테스트 7 〉	통과 (0.09ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (0.09ms, 10.1MB)
테스트 11 〉	통과 (0.04ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.1MB)
테스트 13 〉	통과 (0.05ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.1MB)
테스트 15 〉	통과 (0.05ms, 9.97MB)
테스트 16 〉	통과 (0.05ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (0.71ms, 10.2MB)
테스트 2 〉	통과 (0.77ms, 10.2MB)
테스트 3 〉	통과 (0.47ms, 10.2MB)
테스트 4 〉	통과 (0.51ms, 10.3MB)
채점 결과
정확성: 69.6
효율성: 30.4
합계: 100.0 / 100.0
'''