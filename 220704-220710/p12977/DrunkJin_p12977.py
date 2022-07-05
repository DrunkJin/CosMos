# 급하게 짜서 완성도가 떨어짐 추후에 보완하겠음. 정답이긴함

from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    sum_list = []
    for i in combi:
        sum_list.append(sum(i))
    for i in sum_list:
        cnt = 0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt == 2:
            answer +=1
    return answer