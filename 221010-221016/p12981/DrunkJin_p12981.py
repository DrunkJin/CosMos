"""
2가지 경우의 수가 존재함. 동일한 단어가 들어오거나 끝말잇기가 안된다거나
"""
def solution(n, words):
    past, answer = [], [0,0]   # 이미 나온 단어들을 모으는 past, 정답으로 넣을 answer
    rounds, cnt, relay = 1, 1, words[0][0]
    for i in words:
        if i in past:          # 이전에 나온 단어가 들어오면 현재 차례와 라운드 넣고 종료
            answer = []
            answer.append(cnt)
            answer.append(rounds)
            break
        if relay != i[0]:     # 앞단어의 끝단어와 현재 첫단어가 일치하지 않으면 현재 차례와 라운드 넣고 종료
            answer = []
            answer.append(cnt)
            answer.append(rounds)
            break
        past.append(i)        # 위에 해당되지 않으면 현재 단어를 나왔던 list에 저장
        relay = i[-1]         # 넣은 단어의 마지막 글자를 저장
        cnt += 1              # 차례 더하기
        if cnt > n:           # 인원보다 커질 경우 차례 초기화, rounds 더하기
            rounds += 1
            cnt = 1

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 9.89MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.00ms, 10.1MB)
테스트 20 〉	통과 (0.07ms, 10.3MB)
"""