# mCn  수학문제인듯

def factorial(n):
    factorial_number = 1
    for i in range(1, n+1):
        factorial_number *= i
    return factorial_number

repeat = int(input())

for _ in range(repeat):
    n, m = map(int, input().split())
    upper = factorial(m)
    down = factorial(n)*factorial(m-n)
    answer = upper//down                   # 숫자가 커져서 실수로 나눌경우 23.99999999이런식으로 인식하는 경우가 있다고해서 // 이걸로 해줘야 답이 나온다고함 
    print(answer)

"""
논외로 다양한 팩토리얼 관련해서 자료구조적으로 공부했는데 reduce라는 것을 알아두면 좋을 듯
내용은 어려우니 개인적으로 추가 공부해야할 듯


from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
"""