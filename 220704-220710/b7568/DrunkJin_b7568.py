from ast import And


repeat = int(input())

weight, height, rank = [], [], []
for _ in range(repeat):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for wgt, hgt in zip(weight, height):    # 튜플 생각못하고 zip으로 for문 돌렸음..ㅠㅠ
    temp = 1
    for i, j in zip(weight, height):    # 처음에는 인덱스를 활용할 수 없을까 고민하였으나 반례가 상당수 발견되어 모두 비교
        if i > wgt and j > hgt:
            temp += 1
        else:
            pass
    rank.append(str(temp))  # join을 쓰기 위해 str로 변경 후 append

print(" ".join(rank))

