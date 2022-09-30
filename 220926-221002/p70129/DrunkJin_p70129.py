def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while True:
        if s == '1': # 1로 되면 로직정지
            break
        cnt += 1   # 사이클 횟수 추가
        n = ''
        for i in range(s.count('1')):   # 1의 갯수만큼 추가해서 만들어버림
            n += '1'
        zero += s.count('0') # 0의 개수를 저장`
        s = str(bin(len(n))[2:]) # bin(숫자) -> 0b이진법 으로 변환되서 나옴

    # 반복횟수랑 0제거갯수 저장
    answer.append(cnt)
    answer.append(zero)

    return answer


'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.18ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (5.49ms, 10.4MB)
테스트 10 〉	통과 (5.18ms, 10.4MB)
테스트 11 〉	통과 (1.20ms, 10.3MB)
'''