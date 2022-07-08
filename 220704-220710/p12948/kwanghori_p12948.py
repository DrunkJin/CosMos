def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]  # 번호 자릿수 - 4 == 뒷 네자리를 제외한 번호 자릿수 갯수만큼 '*'으로 채우기
    return answer
