# 숫자는 upper(), lower() 영향X
def solution(s):
    answer = s[0].upper()          # 시작은 대문자
    for i in range(1, len(s)):     # index 1번부터 시작
        if s[i - 1] == " ":        # 앞이 비었으면 대문자로 변환
            answer += s[i].upper()
        else:                      # 그 외에는 소문자로 변환
            answer += s[i].lower()

    return answer