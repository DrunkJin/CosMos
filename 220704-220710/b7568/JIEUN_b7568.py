def big(x,y,x1,y1) :
    if (x < x1) & (y < y1) : return 1
    else : return 0

def solution() :
    N = int(input())
    temp={}

    for i in range(N) :
        body = list(map(int,input().split()))
        temp[i] = body

    result = ''
    for i in range(N) :
        x = temp[i][0]
        y = temp[i][1]
        answer = 0
        for j in range(N) :
            answer += big(x,y,temp[j][0],temp[j][1])
        result += str(answer+1)+' '

    print(result)

solution()