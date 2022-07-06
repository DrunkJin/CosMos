import re
def solution(text):
    text = text.lower()                    # 1단계 소문자변환
    text = re.sub(r'[^a-z0-9-_.]','',text) # 2단계 특수문자제거
    while '..' in text:                    # 3단계 . 중복제거
        text = text.replace('..','.')
    text = text.strip('.')                 # 4단계 맨 앞뒤 . 제거
    if text == '':                         # 5단계 빈 문자열 확인   
        text = 'a'
    if len(text) >= 16:                    # 6단계 단어수 체크
        text = text[0:15]                  
        text = text.strip('.')             # .이 남아있는 케이스가 있어 제거
    if len(text) <= 2:
        while len(text) < 3:
            text+=text[-1]
    answer = text
    return answer