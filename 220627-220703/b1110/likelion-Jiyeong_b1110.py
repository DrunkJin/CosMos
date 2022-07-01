def main():
    _input = int(input())
    num = _input
    cnt = 0
    
    while(True):
        cnt += 1
        sum = num//10 + num%10
        num = (num%10)*10 + sum%10
        
        if num == _input:
            break
    print(cnt)

main()