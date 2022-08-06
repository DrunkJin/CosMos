
n, score, show = map(int, input().split())

# n이 0인 경우 받아올 rank가 없는데 입력을 받으려고 하는 상태 때문에 EOFError가 떴기 때문에 이 부분 수정
if n == 0:
    rank = []
else:
    rank = list(map(int, input().split()))
    
rank.append(score)
rank = sorted(rank, reverse=True)                           # 순서대로 정렬
score_rank = rank.index(score)                              # 점수의 등수 판별
score_rank_index = rank.index(score) + rank.count(score)    # 중복된 경우에는 그만큼 인덱스값이 늘어남

if score_rank > 50:                                         # P는 최대 50이니까 50이상인 경우 볼 필요도 없음
    print(-1)
else:
    if show >= score_rank_index:
        print(rank.index(score)+1)
    else:
        print(-1)
        
        
    """
    메모리 : 30840 KB
    시간 : 72 ms
    """