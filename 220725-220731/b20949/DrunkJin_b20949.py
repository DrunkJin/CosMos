

repeat = int(input())

def ppi(w, h):
    return ((w**2)+(h**2))**0.5
ppi_dict, ppi_list = {}, []
for i in range(1, repeat+1):
    w, h = map(int, input().split())
    ppi_dict[ppi(w, h)] = i
    ppi_list.append(ppi(w, h))

ppi_list = sorted(ppi_list, reverse=True)
for i in ppi_list:
    print(ppi_dict[i])

# 아직 해결 못함

# 수정 필요. dictionary는 동일값에서 처리를 하지 못함
# sorted key를 사용해봐야할듯?