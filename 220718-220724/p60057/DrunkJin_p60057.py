def solution(s):
    answer = 0
    all_len = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1): # aabbaccc -> 1~4
        word = ''
        cnt = 1
        temp = s[:i] # i개씩 잘라서 저장 (비교할 문자)

        for j in range(i, len(s), i): # i개씩 쪼개서 확인
            if temp == s[j:i+j]: # temp와 동일한게 존재하면 cnt+=1
                cnt += 1
            else: # 동일한게 없을때
                if cnt != 1: # 중복된게 있을 시
                    word += str(cnt) + temp # cnt값을 붙이고 temp연결해서 word에 붙여넣기
                else:
                    word += temp # 1개면 걍 넣기
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1: 
            word += str(cnt) + temp
        else:
            word += temp
            
        all_len.append(len(word))
        answer = min(all_len) # 최솟값이 정답
    return answer


    """채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.39ms, 10.3MB)
테스트 3 〉	통과 (0.31ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.45ms, 10.2MB)
테스트 8 〉	통과 (0.45ms, 10.2MB)
테스트 9 〉	통과 (0.75ms, 10.3MB)
테스트 10 〉	통과 (3.49ms, 10.3MB)
테스트 11 〉	통과 (0.16ms, 10.1MB)
테스트 12 〉	통과 (0.09ms, 10.2MB)
테스트 13 〉	통과 (0.11ms, 10.3MB)
테스트 14 〉	통과 (0.67ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (1.38ms, 10.2MB)
테스트 18 〉	통과 (1.74ms, 10.3MB)
테스트 19 〉	통과 (1.37ms, 10.2MB)
테스트 20 〉	통과 (3.89ms, 10.2MB)
테스트 21 〉	통과 (3.99ms, 10.2MB)
테스트 22 〉	통과 (4.72ms, 10.2MB)
테스트 23 〉	통과 (3.95ms, 10.3MB)
테스트 24 〉	통과 (3.43ms, 10.2MB)
테스트 25 〉	통과 (3.94ms, 10.4MB)
테스트 26 〉	통과 (3.86ms, 10.2MB)
테스트 27 〉	통과 (3.84ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
    """