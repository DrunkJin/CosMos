import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 힙으로 변환해줌
    
    while scoville[0] < K: # min heap이라 최상단 노드값이 항상 최소값이 됨
        if len(scoville) == 1: # len이 1일 때는 더이상 조합을 하지 못함
            return -1
        first = heapq.heappop(scoville) # heap에서 가장 작은 값을 가진 노트를 뽑아냄
        second = heapq.heappop(scoville) # first에서 가장 작은 값을 뽑아내고 남은 것에서 가장 작은 것 뽑아냄
        heapq.heappush(scoville, first + (second * 2)) # scoville 힙에 계산한 값을 넣어줌
        answer += 1
    
    return answer

"""
자료구조 힙에 대해서 공부한 유익한 시간이었음

정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.42ms, 10.1MB)
테스트 7 〉	통과 (0.55ms, 10.1MB)
테스트 8 〉	통과 (0.07ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.30ms, 10.1MB)
테스트 11 〉	통과 (0.19ms, 10.1MB)
테스트 12 〉	통과 (0.70ms, 10.2MB)
테스트 13 〉	통과 (0.36ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.50ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (183.82ms, 16.2MB)
테스트 2 〉	통과 (390.05ms, 21.8MB)
테스트 3 〉	통과 (1596.38ms, 49.7MB)
테스트 4 〉	통과 (135.19ms, 14.8MB)
테스트 5 〉	통과 (1916.73ms, 51.7MB)
채점 결과
정확성: 76.2
효율성: 23.8
합계: 100.0 / 100.0
"""