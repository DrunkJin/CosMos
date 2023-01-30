"""
1칸, 2칸, 3칸 ... 확인해보면 피보나치 수열이라는 것을 알 수 있음
cnt를 통해서 n칸만큼의 횟수를 체크함
 pre_result : 이전 스텝에서 가능한 방법 수
 result : 현재 칸에서 가능한 방법 수

 ++++ else문으로 뺄 필요가 없어서 수정함
"""
def solution(n):
    cnt = 0
    pre_result = 0
    result = 1
    while True:
        if n == cnt:
            return result % 1234567
        cnt += 1
        tmp = result
        result += pre_result
        pre_result = tmp