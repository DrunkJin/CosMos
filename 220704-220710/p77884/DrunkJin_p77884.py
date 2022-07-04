def solution(left, right):
    answer = 0
    for number in range(left, right+1):    # left ~ right까지의 수를 넣어서 확인
        count = 0
        for check in range(1, number+1): # 1 ~ 본인 수까지 나누어떨어지면 약수이므로 그때 count + 1
            if number % check == 0:
                count += 1
        if count % 2 == 0:  # count가 짝수면 더하고 아니면 빼고
            answer += number
        else:
            answer -= number
    return answer