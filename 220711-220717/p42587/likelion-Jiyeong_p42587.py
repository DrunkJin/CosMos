from collections import deque
def solution(prior,loc):
    answer = 0
    temp = deque(enumerate(prior)) 
    while temp:
        ord, prio = temp.popleft()
        if any(prio < temp_prio[1] for temp_prio in temp): # any 유용함
            temp.append((ord, prio))
        else:
            answer += 1
            if ord == loc:  # popleft하면서 append시킨 데이터가 돌아옴 
                break
    return answer