
s = int(input()) 

calculation = 0 # 1부터 계속 더한 값의 합
number = 0 # 1부터 증가하는 값

while True:
    if calculation > s: # calculation이 s보다 크다면 그 차이만큼의 숫자를 제외해야하므로 number-1
        print(number-1)
        break
    elif calculation == s: # calculation이 s와 동일하다면 number까지의 합이므로 number 출력
        print(number)
        break
    else: # calculation이 s보다 작다면 계속해서 number 값을 증가시키면서 더함
        number += 1
        calculation += number
