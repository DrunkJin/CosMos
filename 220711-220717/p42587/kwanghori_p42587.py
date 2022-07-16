def solution(wait_arr, loc):
    '''
    1. 맨 앞에 있는 문서를 대기목록에서 꺼냄
    2. 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한개라도 있을 때 J를 대기목록 마지막에 넣음
    3. 그렇지 않으면 J를 인쇄
    '''
    
    answer = 0      # 출력 횟수 체크
    change = loc    # 리스트 내 값 변동에 대한 인덱스 업데이트
    target = wait_arr[loc]    # 목표값, 우선순위와 변경된 인덱스를 교차검증하여 확인할 예정

    # if max(wait_arr) == target:   해당 코드는 속도에 큰 영향이 없어 주석 처리함
    #     if wait_arr.count(target) == 1:
    #         return 1

    while len(wait_arr) != 0:    # 모든 문서가 출력될 때 까지 반복
        head = wait_arr[0]       
        wait_arr.remove(head)    # 맨 앞의 문서를 head로 지정하고, 목록에서 꺼냄

        if len(wait_arr) == 0:   # 꺼냈을 때 대기목록에 아무것도 남지 않으면 1개만 있는 것으로 1을 더한 뒤 결과 출력
            answer += 1
            return answer

        if change == 0 and target == head:  # 목표값이 head에 왔을 때 
            if max(wait_arr) <= head:       # head가 남은 대기목록의 우선순위보다 크거나 같으면 결과 출력
                answer += 1
                return answer
            else:
                wait_arr.append(head)       # 그렇지 않다면 목록의 맨 뒤로 이동
                change = len(wait_arr) - 1
             
        else:                               # 목표값이 head가 아닐 때
            if max(wait_arr) <= head:       # 중요도가 가장 높은 문서라면 출력
                answer += 1
            else:                           # 그게 아니면 맨 뒤에서 대기
                wait_arr.append(head)
            change -= 1                     # 두 경우 모두 대기목록의 인덱스 앞으로 한 칸씩 이동함
            
        

    return answer
  
  
  
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.66ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.09ms, 10.2MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.45ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.15ms, 10.3MB)
테스트 11 〉	통과 (0.34ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.30ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
테스트 17 〉	통과 (0.54ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.36ms, 10.2MB)
테스트 20 〉	통과 (0.06ms, 10.3MB)
