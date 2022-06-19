n, m = map(int, input().split())

# n * m ÀÇ »ç°¢Çü n-1¹ø ÂÉ°³¸é n°³°¡ »ı±è. n(m-1)¹ø ÂÉ°³¸é m°³°¡ ´õ ÂÉ°³Áü

print(n*m - 1)

'''
# ¿Ö Æ²·ÈÀ»±î?
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