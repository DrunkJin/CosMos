'''
걍 arr에 있는 걸로 다 나눠지는 값 찾으면 됨
'''
def solution(arr):
    answer = 2
    while True:
        cnt = 0
        for idx in arr:
            if answer % idx == 0:
                cnt += 1
        if cnt == len(arr):
            break
        answer += 1

    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.67ms, 10MB)
테스트 2 〉	통과 (0.09ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 9.96MB)
테스트 4 〉	통과 (0.48ms, 10MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (6212.81ms, 9.96MB)
테스트 7 〉	통과 (230.91ms, 10.2MB)
테스트 8 〉	통과 (22.22ms, 9.95MB)
테스트 9 〉	통과 (295.85ms, 10.1MB)
테스트 10 〉	통과 (2673.78ms, 10.1MB)
'''