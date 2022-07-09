def solution(n):
    # DFS 문제
    fib = [0,1] # f(0)과 f(1) 결과를 먼저 저장한 list
    if n == 0:
        return fib[n]
    elif n == 1:
        return fib[n]
    
    for i in range(2, n+1):   # fibonacci 수열 저장
        fib.append(fib[i-2]+fib[i-1])
    
    return fib[n] % 1234567   # 1234567로 나눈 나머지 출력
