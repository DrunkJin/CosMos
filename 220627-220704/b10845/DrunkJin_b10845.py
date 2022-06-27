from collections import deque
import sys

times = int(input())
que = deque()

# queue 로직 함수화
def order_logic(order, number=None, data=que):
    if order == 'push':
        data.appendleft(int(number))
    elif order == 'pop':
        if len(data) == 0:
            return print(-1)
        else:
            print(data[-1])
            data.pop()
    elif order == 'size':
        return print(len(data))
    elif order == 'empty':
        if len(data) == 0:
            return print(1)
        else:
            return print(0)
    elif order == 'front':
        if len(data) == 0:
            return print(-1)
        else:
            return print(data[-1])
    else:
        if len(data) == 0:
            return print(-1)
        else:
            return print(data[0])
# times만큼 반복 실행..
for _ in range(times):
    order = sys.stdin.readline().split()
    if len(order) == 2:     # 숫자까지 들어오면 number에 변수 추가
        order_logic(order[0], order[1], que)
    else:
        order_logic(order[0], None, que)
