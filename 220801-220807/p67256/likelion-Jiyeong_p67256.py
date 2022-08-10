# 거리 구하는 함수
def get_dist(num,left_now, right_now, pos, hand):
    dist_left = abs(pos[left_now][0] - pos[num][0]) + abs(pos[left_now][1] - pos[num][1])
    dist_right = abs(pos[right_now][0] - pos[num][0]) + abs(pos[right_now][1] - pos[num][1])
    if dist_left == dist_right:
        return 'L' if hand == 'left' else 'R'
    return 'L' if dist_left < dist_right else 'R'
         
def solution(numbers, hand):
    pos = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)
    }
    
    left = [1,4,7]
    right = [3,6,9]
    left_now = '*'
    right_now = '#'
    answer = []
    
    for i in numbers:
        if i in left:
            answer.append('L')
            left_now = i
        elif i in right:
            answer.append('R')
            right_now = i
        else:           # 가운데 배열일 경우
            result = get_dist(i,left_now,right_now,pos,hand)
            answer.append(result)
            if answer[-1] == 'L':
                left_now = i
            else:
                right_now = i

    answer = ''.join(answer)
    return answer

