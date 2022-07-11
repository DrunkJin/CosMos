def solution(phone_number):
    answer = ''
    for _ in phone_number[:-4]: # 끝의 4자리 빼고 나머지 자리를 차지하는 만큼 반복하며 * 넣기
        answer += "*"
    answer += phone_number[-4:] # 끝 4자리 붙이기
    return answer