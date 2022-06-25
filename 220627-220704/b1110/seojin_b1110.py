# 26, 4  55, 3


number = int(input())

target = number
count = 0

while True:
    if number == target and count != 0:
        print(count)
        break

    else:
        if number > 9:
            ten_digit = number // 10
            one_digit = number % 10
            number = (one_digit*10) + (ten_digit + one_digit)%10
            count += 1
        else:
            number = int(str(number)+str(number))
            count += 1
