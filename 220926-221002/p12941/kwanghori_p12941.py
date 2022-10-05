def solution(A,B):
    # 작은 수 * 큰 수를 더할 경우, 모든 경우를 비교하지 않고 최솟값을 구할 수 있음.
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i,j in zip(A, B):
        answer += i*j
            
    return answer
