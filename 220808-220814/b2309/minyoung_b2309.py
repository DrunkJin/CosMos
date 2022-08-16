from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))
    
re = list(combinations(arr, 7))

for r in re:
    if sum(r) == 100:
        de = r
        
de = sorted(de)

for i in de:
    print(i)