# 1번

import time
n = int(input())

hour, min, sec = n//3600, (n//3600)//60,  ((n%3600)%60)
print(f"시:{hour}")
print(f"분:{min}")
print(f"초:{sec}")
while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)


# 2번
import random

random_list = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
sort_random_list = sorted(random_list)

random_list = list(map(str, random_list))
sort_random_list = list(map(str, sort_random_list))

random_list = " ".join(random_list)
sort_random_list = " ".join(sort_random_list)
print("랜덤 수 :",random_list)
print("정렬 후 :",sort_random_list)


# 3번
updown_answer = random.randint(1, 100)
cnt = 0
while True:
    updown = int(input("입력 : "))
    cnt +=1
    if updown_answer < updown :
        print("DOWN--")
    elif updown_answer > updown:
        print("----UP")
    else:
        print("정답입니다.")
        print("입력횟수 : ", cnt)
        break

# 4번
import random

comp = []

numbers = list(range(10))
for _ in range(4):
    num = random.choice(numbers)
    numbers.remove(num)
    comp.append(num)

print("정답:", comp)

roof1 = True
roof2 = True

while (roof1):
    user = input("예상하는 숫자 4개를 입력해주세요.")
    l_user = list(map(int, list(user)))

    print(l_user)
    while (roof2):
        strike = 0
        ball = 0
        for idx in l_user:
            if idx in comp:
                if l_user.index(idx) == comp.index(idx):
                    strike += 1

                else:
                    ball += 1

        if strike == 4:
            roof1 = False
            roof2 = False
            print("정답 4stike!!")

        else:
            print("당신의 입력은", strike, "strike,", ball, "ball입니다.")
        break

    if len(l_user) != 4:
        print("숫자는 4개만 입력해주세요.")
        continue
    for joong in l_user:
        if l_user.count(joong) > 1:
            print("숫자가 중복되어선 안됩니다.")
            break