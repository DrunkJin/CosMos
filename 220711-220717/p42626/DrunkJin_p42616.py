def solution(priorities, location):
    answer = 0
    while True:
        max_number = max(priorities)
        for i in range(len(priorities)):
            if max_number == priorities[i]:
                answer += 1 # 순서 +1
                priorities[i] = 0 # 출력된 max값은 0으로 치환 (중요도는 1~9)
                max_number = max(priorities) # 새로운 다음 출력물
                if i == location:
                    return answer
                
    """
[1, 1, 0, 1, 1, 1]
[1, 1, 0, 0, 1, 1]
[1, 1, 0, 0, 0, 1]
[1, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
    """