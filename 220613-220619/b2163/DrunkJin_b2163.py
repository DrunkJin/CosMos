n, m = map(int, input().split())

# n * m �� �簢�� n-1�� �ɰ��� n���� ����. n(m-1)�� �ɰ��� m���� �� �ɰ���

print(n*m - 1)

'''
# �� Ʋ������?
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