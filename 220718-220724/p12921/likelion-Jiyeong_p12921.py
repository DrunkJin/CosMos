# 소수개수찾기 찾기
"""
함수로 소수를 판별하는 방법은 시간초과가 뜬다. 
다른 방법 필요함
"""
# def find_primary(n):
#     for i in range(2, n//2+1):
#         if n%i == 0:
#             return False
#     return True

# def solution(n):
#     answer = 0
#     for i in range(2,n+1): #1은 소수가 아니므로 2부터
#         if find_primary(i):
#             answer+=1
    
#     print(f"answer >> {answer}")
#     return answer
# solution(5)

# 에라토스테너스의 체를 이용
# 직접 구현하기 헷갈려서 그냥 코드를 외울 계획
def solution(n):
    nums = set(range(2,n))
    for i in range(2,n+1):
        if i in nums:
            nums -= set(range(i*2, n+1, i))
    return len(nums)