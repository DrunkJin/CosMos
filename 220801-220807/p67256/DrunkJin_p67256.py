# 가운데 위치한 숫자가 입력된 경우 현재 손가락의 위치와 주 손잡이에 따라 다른 결과 도출
def position(num, left, right, hand):
    # 엄지손가락의 현재 위치를 파악하기 위해 딕셔너리로 키패드 생성
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    # (x1, y2), (x2, y2)의 좌표간 거리는 |x1 - x2| + |y1 - y2|
    dist_left = abs(keypad[num][0] - keypad[left][0]) + abs(keypad[num][1] - keypad[left][1])
    dist_right = abs(keypad[num][0] - keypad[right][0]) + abs(keypad[num][1] - keypad[right][1])

    #  가까운 손가락의 결과 리턴
    if dist_left < dist_right:
        return 'L'
    elif dist_left > dist_right:
        return 'R'
    # 입력된 키와 왼손, 오른손의 거리가 같은 경우 오른손잡이면 R, 왼손잡이면 L 출력
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'

def solution(numbers, hand):
    answer = ''
    left_position = "*"
    right_position = "#"
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left_position = number
        elif number in [3,6,9]:
            answer += 'R'
            right_position = number
        # 가운데 (0,2,5,8) 인 경우 position 함수를 태워서 적용
        else:                                                           
            middle = position(number, left_position, right_position, hand)
            answer += middle
            if middle == 'R':
                right_position = number
            else:
                left_position = number
    return answer

    """
    정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.4MB)
테스트 14 〉	통과 (0.11ms, 10.4MB)
테스트 15 〉	통과 (0.28ms, 10.3MB)
테스트 16 〉	통과 (0.27ms, 10.2MB)
테스트 17 〉	통과 (0.73ms, 10.3MB)
테스트 18 〉	통과 (0.48ms, 10.4MB)
테스트 19 〉	통과 (0.52ms, 10.4MB)
테스트 20 〉	통과 (0.58ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
    """