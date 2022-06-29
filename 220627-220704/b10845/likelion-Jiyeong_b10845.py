import sys
def get_result(quest, queue):
    if quest == 'front':
        if queue: print(queue[0])
        else: print(-1)

    elif quest == 'back':
        if queue: print(queue[-1])
        else: print(-1)

    elif quest =='size':
        print(len(queue))

    elif quest == 'empty':
        if queue: print(0)
        else: print(1)

    elif quest == 'pop':
        if queue: print(queue.pop(0))
        else: print(-1)

def main():
    # _input = int(input())   # 시간초과됨
    _input = int(sys.stdin.readline())
    queue = []
    for case in range(_input):
        quest = sys.stdin.readline().split()
        if quest[0] == 'push':
            num = quest[1]
            queue.append(num)
        else:
            get_result(quest[0], queue)
            
main()