# -*- coding: utf-8 -*-
n, m = map(int, input().split())

# n * m 의 사각형 n-1번 쪼개면 n개가 생김. n(m-1)번 쪼개면 m개가 더 쪼개짐

print(n*m - 1)

'''
# 왜 틀렸을까?
count = 0
def split_choco(N, count):
    while (N != 1):
        N //= 2
        count += 1
    return count

if n == m == 1:
    pass
else:
    count += 1
    count = split_choco(n, count)
    count = split_choco(m, count)
    
print(count)
'''