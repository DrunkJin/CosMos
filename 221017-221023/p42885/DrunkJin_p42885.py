'''
효율성 통과를 아직 못함!
수정 필요!!
'''
def solution(people, limit):
    answer = 0
    people = sorted(people)
    while people:
        load = people.pop()
        if load > limit-40:
            answer += 1
            continue
        remain = limit - load
        if remain < 40:
            answer+=1
            continue
        ride_check = list(map(lambda x:x<=remain, people))
        if True in ride_check:
            plus = people.pop(ride_check.index(True))

        answer += 1
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (214.51ms, 10.3MB)
테스트 2 〉	통과 (0.91ms, 10.3MB)
테스트 3 〉	통과 (106.77ms, 10.3MB)
테스트 4 〉	통과 (121.18ms, 10.3MB)
테스트 5 〉	통과 (51.89ms, 10.1MB)
테스트 6 〉	통과 (7.10ms, 10.2MB)
테스트 7 〉	통과 (10.78ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.68ms, 10.2MB)
테스트 10 〉	통과 (82.96ms, 10.2MB)
테스트 11 〉	통과 (113.22ms, 10.1MB)
테스트 12 〉	통과 (46.19ms, 10.3MB)
테스트 13 〉	통과 (42.01ms, 10.4MB)
테스트 14 〉	통과 (0.66ms, 10.3MB)
테스트 15 〉	통과 (0.06ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (7.38ms, 10.8MB)
테스트 5 〉	통과 (6.87ms, 10.8MB)
채점 결과
정확성: 75.0
효율성: 10.0
합계: 85.0 / 100.0
'''