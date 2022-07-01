"""
1,2,3일경우
1,1+2,1+2+3 이 다음 층 값이다.
"""

times = int(input())

for _ in range(times):
    k = int(input())
    n = int(input())
    under = []
    for i in range(1, n+1):
        under.append(i)

    def up(under, k):   # 0층에는 목표로하는 n호수까지 1부터 순차적으로 들어있다. 그 값으로 시작해서 천천히 올라간다.
        if k == 1 : # 함수가 돌때마다 k값을 줄일텐데 1층이 궁금하면 0층까지의 합이 나와야하므로 k-1에서 스탑하고 아랫층의 인원을 모두 더한값을 본다
            return sum(under)
        else:
            down = under.copy() # 들어온 리스트값을 복사한다. 재귀함수를 쓸 때 좀더 직관적으로 보려고..그리고 합과 빈리스트가 필요하니까
            under = []
            for i in range(len(down)):  # 103호가 목표라면 3번 돌린다.
                under.append(sum(down[:i+1]))   # 이전에 있던 리스트에서 돌아갈 때마다 하나씩 더해서 새로운 under에 넣는다.
        return up(under, k-1) # 다시 up함수를 탄다.

    print(up(under, k))