def solution(left, right):
    answer = 0
    
    for number in range(left, right+1):
        if number == int(number**0.5)**2:   # 제곱의 경우 약수의 갯수가 홀수
            answer -= number
        else: answer += number  # 어떤 수의 제곱이 아닌 경우 약수의 갯수 짝수
    return answer