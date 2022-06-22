wood = list(map(int, input().split()))

for i in range(len(wood)-1):
    if wood[i] > wood[i+1]:
        temp = wood[i]
        wood[i] = wood[i+1]
        wood[i+1] = temp
        print(" ".join(map(str, wood)))
    else:
        continue
