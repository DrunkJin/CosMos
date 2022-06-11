# 내가 짜본 코드
n = 5
m = 8
k = 3
data = [2,4,5,4,6]
data.sort(reverse = True)
answer = 0
while(m >= 0):
    if m == 0:
        break
    elif (m - k) < 1: # k번만큼 빼고 2번째 큰수까지 한번 뺄 경우를 else로 넣을 것이기 때문에
        for i in range(m):  # k번 더하기
                answer += data[0]  # data[0]은 가장 큰 수
                m -= 1  # 더할 때마다 더할 수 있는 횟수 차감
    else:
        for i in range(k): # k번 더하기
            if m != 0:
                answer += data[0] # data[0]은 가장 큰 수
                m -= 1 # 더할 때마다 더할 수 있는 횟수 차감

        answer += data[1] # 2번째로 큰 수 한번 더해주기
        m -= 1  # 더할 때마다 더할 수 있는 횟수 차감
    print(f"현재 총합 : {answer}")
print(f"최종 정답 : {answer}")