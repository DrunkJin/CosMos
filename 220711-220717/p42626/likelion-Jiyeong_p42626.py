"""
    처음에는 deque로 해결하려고 했다가 일부 런타임에러와,
    효율성체크에서 점수가 안나와서 heapq로 변경    
"""

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 힙구조에 맞게 자동으로 정렬됨
    while True:
        if len(scoville) < 2: return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new_sco = a+(b*2)  
        heapq.heappush(scoville,new_sco)
        answer += 1        
        if scoville[0] >= K:
            return answer
        

# from collections import deque
# def solution(scoville, K):
#     answer = 0
#     temp_list = sorted(scoville)
#     while True:
#         if len(scoville) < 2: return -1
#         temp_deque = deque(temp_list)
#         a = temp_deque.popleft()
#         b = temp_deque.popleft()
#         new_sco = a+(b*2)  
#         temp_deque.appendleft(new_sco) 
#         temp_list = sorted(temp_deque)
#         answer += 1         
#         if all(k >= K for k in temp_list):
#             return answer
        

