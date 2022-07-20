'''
글자 토큰을 리스트에 저장 후 하나씩 꺼내면서 비교하는 로직 구현
'''

def solution(s):
    answer = len(s)   # answer값 초기 글자 갯수로 

    for k in range(1, len(s)//2+1):  # 1부터 글자수까지 한개씩 tokenized
        arr = []
        
        for i in range(0, len(s), k):
            try:
                arr.append(s[i:i+k])
            except:   # indexError 발생할 경우 길이가 짧아 발생하는 것이므로 마지막 글자까지 범위 설정
                arr.append(s[i:-1])

                
        unit = 1      # 연속된 글자를 확인하는 변수
        zipped = ''
        for idx in range(len(arr)):
            try:
                if arr[idx] == arr[idx+1]:  # 글자가 같은 경우
                    unit += 1
                else:   # 뒷글자와 앞글자가 같지 않을 때
                    if unit > 1:
                        zipped += f'{unit}{arr[idx]}'
                        unit = 1    # unit을 1로 되돌림 (중요)
                    else: # unit이 1인 경우는 글자 앞에 숫자를 넣지 않음
                        zipped += arr[idx]
            except: # 맨 마지막 인덱스 처리
                if unit > 1:  # 이미 unit을 더해주었기 때문에 zipped에 글자토큰을 붙이기만 하면 된다.
                    zipped += f'{unit}{arr[idx]}'
                    unit = 1
                else:
                    zipped += arr[idx]
                    
        if answer > len(zipped):  # 압축문자열이 기존 문자열 보다 짧을 경우 answer값 업데이트
            answer = len(zipped)
        
    return answer



정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.40ms, 10.3MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.48ms, 10.3MB)
테스트 8 〉	통과 (0.44ms, 10.3MB)
테스트 9 〉	통과 (0.64ms, 10.3MB)
테스트 10 〉	통과 (2.32ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.2MB)
테스트 12 〉	통과 (0.10ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.66ms, 10.4MB)
테스트 15 〉	통과 (0.11ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (1.12ms, 10.2MB)
테스트 18 〉	통과 (1.10ms, 10.3MB)
테스트 19 〉	통과 (1.12ms, 10.2MB)
테스트 20 〉	통과 (2.55ms, 10.3MB)
테스트 21 〉	통과 (2.48ms, 10.3MB)
테스트 22 〉	통과 (3.38ms, 10.4MB)
테스트 23 〉	통과 (2.47ms, 10.2MB)
테스트 24 〉	통과 (2.28ms, 10.4MB)
테스트 25 〉	통과 (2.52ms, 10.4MB)
테스트 26 〉	통과 (2.59ms, 10.2MB)
테스트 27 〉	통과 (2.49ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.4MB)
