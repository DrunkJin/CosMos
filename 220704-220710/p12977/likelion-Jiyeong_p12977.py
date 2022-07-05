from itertools import combinations

def find_primary(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

def solution(nums):
    list_ = list(combinations(nums,3))
    cnt = 0
    for i in list_:
        sum = i[0]+i[1]+i[2]
        if find_primary(sum):
            cnt+=1
    answer  = cnt

    return answer