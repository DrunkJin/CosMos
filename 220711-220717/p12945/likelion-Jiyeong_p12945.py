def solution(n):
    a,b = 0,1  # 피보나치의 1,2번째는 항상 0,1임
    answer = 1 
    
    for i in range(n-2): # 3번째 값부터 for문 돌림
        a = b
        b = answer
        answer = a+b
    return answer%1234567
