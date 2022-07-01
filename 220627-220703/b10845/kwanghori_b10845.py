from collections import deque
import sys

queue = deque()

# 파이썬 모듈을 이용하여 큐를 구현하였습니다.

class example:

    def __init__(self, times) -> None:
        self.times = times

    def sol(self):

        for _ in range(self.times):
            order = sys.stdin.readline().strip()    # 개행문자 제거 (\n)

            # empty 구현
            if order == 'empty':
                if len(queue) == 0:
                    sys.stdout.write(str(1)+'\n')
                else:
                    sys.stdout.write(str(0)+'\n')
            
            # front 구현
            elif order == 'front':
                if len(queue) == 0:
                    sys.stdout.write(str(-1)+'\n')
                else:
                    sys.stdout.write(str(queue[-1])+'\n')

            # back 구현
            elif order == 'back':
                if len(queue) == 0:
                    sys.stdout.write(str(-1)+'\n')
                else:
                    sys.stdout.write(str(queue[0])+'\n')

            # size 구현
            elif order == 'size':
                sys.stdout.write(str(len(queue))+'\n')

            # pop 구현
            elif order == 'pop':
                if len(queue) == 0:
                    sys.stdout.write(str(-1)+'\n')
                else:
                    sys.stdout.write(str(queue.pop())+'\n')
            
            # push 구현
            else:
                num = int(order.split()[-1])
                queue.appendleft(num)

if __name__ == '__main__':
    b10845 = example(int(input()))
    b10845.sol()
