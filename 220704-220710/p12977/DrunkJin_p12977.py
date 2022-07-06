# 급하게 짜서 완성도가 떨어짐 추후에 보완하겠음. 정답이긴함

from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3)) # 모든 조합의 경우의 수를 만들어주는 combinations사용. 단점으로는 오래 걸림
    sum_list = []
    for i in combi:
        sum_list.append(sum(i)) # 조합을 더한 값을 모아줌
    for i in sum_list:
        cnt = 0
        for j in range(1,i+1):  # 나누어떨어지는 수가 1부터 자기자신까지 했을 때 2개가 되면 소수니까 cnt==2면 답을 1늘림
            if i%j==0:  
                cnt+=1
        if cnt == 2:
            answer +=1
    return answer

    """
    소수를 구하는 경우에 range(2, i//2 + 1):
        if  i%j == 0:
            여기에 들어오면 소수 아님
        if문 안타면 소수임
    """