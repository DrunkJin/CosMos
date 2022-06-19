# 이것이 취업을 위한 코딩테스트다 p.92
# 2019 국가 교육기관 코딩 테스트

# 책에서 나온 답안 첫번째 : 단순하게 푸는 답안 예시 (백준처럼 짠듯)

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 위의 코드는 M의 크기가 100억이상으로 커진다면 시간 초과 판정을 받게 됨. 
# 효율성을 높이려면 반복되는 수열에 대해서 파악하고 수학적으로 해결하는 것이 좋음


## 효율성을 높인 답안
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k+1)

result =0
result += (count) * first
result += (m-count) * second

print(result)