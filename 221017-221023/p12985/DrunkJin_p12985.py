
n, a, b = 8,4,7

answer = 0
while a != b:
    a, b = round(a/2), round(b/2)
    answer += 1
    print(a,b)
print(answer-1)