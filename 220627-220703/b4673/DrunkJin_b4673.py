# 10000보다 작은 셀프넘버


numList = []
for i in range(1, 10000): # 10000까지 셀프넘버 계산해서 싹 다 numList에 넣음
    for j in list(str(i)):
        i += int(j)
    numList.append(i)

for num in range(1, 10000): # numList에 없는 번호 출력
    if num not in numList:
        print(num)

