def solution(phone_number):
    l=(len(phone_number)-4)
    answer = (l*"*")+phone_number[l:]
    return answer