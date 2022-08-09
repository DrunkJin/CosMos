def solution(n):
    n = str(n)  # int로 진행하면 map함수에서 따로 분리가 안됨
    answer = list(reversed(list(map(int, n))))  # map으로 int형으로 변환하고 reversed해줌
    return answer