import heapq

def solution(scoville, K) :
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K :
        if len(scoville) == 1 : return -1
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        mix = num1 + (num2 *2)
        heapq.heappush(scoville,mix)
        answer += 1
    return answer