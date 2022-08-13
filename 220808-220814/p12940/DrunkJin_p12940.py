def gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:
        return n

def solution(n,m):
    return [gcd(n,m),int(m*n/gcd(n,m))]

# 유클리드호제법 공부