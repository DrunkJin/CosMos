def solution(n):
    answer = n
    for i in range(1, n):
        if n%i ==0:
            answer += i
    return answer