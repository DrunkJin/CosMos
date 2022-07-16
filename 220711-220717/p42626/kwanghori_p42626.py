'''최소 정렬 힙을 직접 구현하여 정답을 제출해보고, 파이썬 내장 모듈을 이용해서도 제출해보았습니다.'''

# 1. 최소 힙 정렬을 직접 구현한 정답

def heap_sort(array) -> None:
    '''
    최소 힙 정렬
    '''

    def down_heap(array, l: int, r: int) -> None:
        """array[l] ~ array[r]를 힙으로 만들기"""
        tmp = array[l]      # 루트

        parent = l
        while parent < (r+1) // 2:
            cl  = parent*2 + 1      # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= r and array[cr] > array[cl] else cl     # 자식 중 큰 값을 선택

            if tmp >= array[child]:
                break
            array[parent] = array[child]
            parent = child
        array[parent] = tmp
    
    n = len(array)

    for i in range((n-1) // 2, -1, -1):     # array[i] ~ array[n-1]을 힙으로 만들기
        down_heap(array, i, n-1)

    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]     # 최댓값인 array[0]와 마지막 원소를 교환
        down_heap(array, 0, i-1)                        # array[0] ~ array[n-1]을 힙으로 만들기


        
def solution(scoville, K):
    answer = 0
    heap_sort(scoville)
    
    while scoville[0] < K:
        # print(scoville)
        answer += 1
        least, less = scoville[0], scoville[1]
        
        scoville.remove(least)
        scoville.remove(less)

        val = least + less*2
        scoville.append(val)
        heap_sort(scoville)
        
        if len(scoville) == 1 and scoville[0] < K:    # 원소의 갯수가 1이면서 K값 이상일 경우는 제외됨 ex) [1,2,3], 11의 경우 5, 11로 원소의 갯수가 1개가 되며 조건을 만족
            return -1
            
    
    return answer
  
  
# 2. 파이썬 heapq모듈 활용

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        answer += 1
        values = [0,0]  # least와 less 값을 저장할 리스트
        
        
        for idx in range(len(values)):    # heapq를 사용한 것 외에는 로직은 모두 같다.
            values[idx] = scoville[0]
            heapq.heappop(scoville)
        
        val = values[0] + values[1]*2
        heapq.heappush(scoville, val)
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
            
    
    return answer
  
  
# 테스트 결과 비교
'1. 직접 구현한 정답'

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.08ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (440.09ms, 10.3MB)
# 테스트 7 〉	통과 (258.92ms, 10.4MB)
# 테스트 8 〉	통과 (4.17ms, 10.2MB)
# 테스트 9 〉	통과 (4.88ms, 10.2MB)
# 테스트 10 〉	통과 (207.62ms, 10.4MB)
# 테스트 11 〉	통과 (85.01ms, 10.3MB)
# 테스트 12 〉	통과 (1033.16ms, 10.2MB)
# 테스트 13 〉	통과 (339.08ms, 10.2MB)
# 테스트 14 〉	통과 (0.15ms, 10.4MB)
# 테스트 15 〉	통과 (701.09ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)

# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)

'2. 파이썬 내장모듈을 이용한 정답'

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.05ms, 10.2MB)
# 테스트 6 〉	통과 (0.65ms, 10.3MB)
# 테스트 7 〉	통과 (0.55ms, 10.4MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (0.11ms, 10.1MB)
# 테스트 10 〉	통과 (0.46ms, 10.2MB)
# 테스트 11 〉	통과 (0.29ms, 10.2MB)
# 테스트 12 〉	통과 (1.05ms, 10.1MB)
# 테스트 13 〉	통과 (0.54ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.73ms, 10.1MB)
# 테스트 16 〉	통과 (0.00ms, 10.3MB)

# 효율성  테스트
# 테스트 1 〉	통과 (242.26ms, 16.2MB)
# 테스트 2 〉	통과 (518.26ms, 22MB)
# 테스트 3 〉	통과 (1953.70ms, 49.8MB)
# 테스트 4 〉	통과 (186.69ms, 14.9MB)
# 테스트 5 〉	통과 (2315.73ms, 51.8MB)
