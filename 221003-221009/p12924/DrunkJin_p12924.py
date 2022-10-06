'''
굉장히 단순하게 짰음.
1부터 n까지 계속 더하다가 본인 숫자면 answer +1 
넘어가면 바로 브레이크
'''
def solution(n):
    answer = 0
    start = 1

    while start != n+1:
        hap = 0
        for i in range(start, n+1):
            hap += i
            if hap == n:
                answer += 1
                break
            elif hap > n:
                break

        start +=1

    return answer









# 아래는 pycharm디버그 테스트용 코드
# n = 15
# 
# cnt = 0
# start = 1
# 
# while start != n+1:
#     hap = 0
#     for i in range(start, n+1):
#         hap += i
#         if hap == n:
#             cnt += 1
#             break
#         elif hap > n:
#             break
# 
#     start +=1
# 
# 
# print(cnt)
