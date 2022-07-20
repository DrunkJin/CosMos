# 그냥 했는데 효율성이 너무너무 안되서 찾아보니 뭐시기 체를 이용하는 문제라함..그래서 그 부분 참고함ㅠㅠ

import math 
def solution(n):
    answer = 1 # n은 2이상이므로 무조건 2 1개는 있음
    for i in range(3, n+1):
        tmp = 0
        if i//2 > 2:
            for j in range(2, int(math.sqrt(i))+1):
                if tmp != 0:
                    break
                if i%j == 0:
                    tmp += 1
            if tmp == 0:
                answer += 1

        else:
            for j in range(2, i):
                if tmp != 0:
                    break
                if i%j == 0:
                    tmp += 1
            if tmp == 0:
                answer += 1

    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.29ms, 10.1MB)
테스트 4 〉	통과 (0.63ms, 10MB)
테스트 5 〉	통과 (0.43ms, 10.2MB)
테스트 6 〉	통과 (7.99ms, 10.2MB)
테스트 7 〉	통과 (1.88ms, 10.1MB)
테스트 8 〉	통과 (5.42ms, 10.2MB)
테스트 9 〉	통과 (10.05ms, 10.3MB)
테스트 10 〉	통과 (716.10ms, 10.1MB)
테스트 11 〉	통과 (3620.57ms, 10.2MB)
테스트 12 〉	통과 (839.07ms, 9.96MB)

효율성  테스트
테스트 1 〉	통과 (4208.64ms, 10.3MB)
테스트 2 〉	통과 (3755.95ms, 10.2MB)
테스트 3 〉	통과 (4182.77ms, 10.1MB)
테스트 4 〉	통과 (4084.41ms, 10.1MB)

채점 결과
정확성: 75.0
효율성: 25.0
합계: 100.0 / 100.0
"""

