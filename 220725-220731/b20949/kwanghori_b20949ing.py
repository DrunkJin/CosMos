def ppi(w, h):
    return (w**2 + h**2)**0.5

def results(n):
    results = []
    for _ in range(n):
        w, h = [int(i) for i in input().split()]
        results.append(ppi(w,h))
    return results

def rank(arr):
    for v in arr:
        print(sorted(arr, reverse=True).index(v)+1)

if __name__ == '__main__':
    arr = results(int(input()))
    rank(arr)
    
    
    # 10%에서 
