import re

def solution(new_id):
    answer = new_id.lower() # 1단계 소문자로 만듬
    answer = re.sub(r"[^a-z0-9-_.]","", answer) # 2단계 영어, 숫자, -, _, . 빼고 다 제거
    answer = re.sub(r'[.]{2,}', '.', answer) # 3단계 마침표가 2개이상 연속으로 나오는 경우 하나로 통합
    answer = answer.strip(".") # 4단계 양옆의 점 제거

    # 5단계 아무것도없으면 a추가
    if answer== "":
        answer += 'a'
        return solution(answer)
    # 16개 이상이면 15개까지만 출력
    # 혹시나 제거 후에 남아있을 마침표를 제거하기 위해 이 함수를 다시 한번 탐
    elif len(answer) > 15:
        answer = answer[:15]
        return solution(answer)
    # 2글자 이하면 마지막 글자 반복 (마지막에 마침표가 올리 없으니 바로 리턴)
    elif len(answer) < 3:
        while (len(answer)!=3):
            answer += answer[-1]  
        return answer
    # 이상없으면 출력
    else:
        return answer