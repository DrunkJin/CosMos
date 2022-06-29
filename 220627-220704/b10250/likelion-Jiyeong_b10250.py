def get_room_number(h,w,n): 
    c = n//h + 1
    d = n % h
    if d == 0:
        c = n//h
        d = h
    return d*100+c


def main():
    _input = int(input())
    for case in range(_input):
        h,w,n = map(int, input().split())
        result = get_room_number(h,w,n)
        print(result)    

main()
