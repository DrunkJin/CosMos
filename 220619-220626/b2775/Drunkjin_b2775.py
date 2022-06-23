# 26, 4  55, 3

from re import A


number = int(input())

target = number
count = 0

while True:
    print(number)
    if number == target & count != 0:
        print(count)
        break

    else:
        if number > 9:
            ten_digit = number // 10
            one_digit = number % 10
            number = ten_digit + one_digit
            count += 1
        else:
            number *= 10