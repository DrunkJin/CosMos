def solution(new_id):
    special = list('~!@#$%^&*()=+[{]}:?,<>/')
    
    # 1단계: 알파벳 소문자 치환
    tmp = list(new_id.lower())
    result = []

    # 2단계: 특수문자 제거
    for char in tmp:
        if char not in special: 
            result.append(char)
    result = ''.join(result)

    # 3단계: 연속된 마침표를 하나의 마침표로 치환
    for _ in range(len(result)//2):     # 여러개의 점이 연속될 경우 반복 제거 필요 (다른방법이 생각나지 않았습니다. ㅜㅜ)
        result = result.replace('..','.')

    # 4단계: 처음과 끝의 마침표 제거
    result = result.strip('.')

    # 5단계: result가 빈 문자열이라면 a 대입
    if result == '': result = 'a'

    # 6단계: 앞부터 문자열 15개 슬라이싱
    if len(result) > 15: result = result[:15]   

    result = result.strip('.')  # 4단계 실행

    # 7단계: 마지막 글자를 글자수 3이 될때까지 붙여넣기
    if len(result) <= 2:
        last = len(result)-1
        while (len(result) != 3):
            result += result[last]
    return result
