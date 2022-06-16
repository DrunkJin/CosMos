n, m = map(int, input().split())

# n * m 의 사각형 n-1번 쪼개면 n개가 생김. n(m-1)번 쪼개면 m개가 더 쪼개짐

print(n*m - 1)