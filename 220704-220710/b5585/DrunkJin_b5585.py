money = int(input())
count = 0

money = 1000 - money

coin_type = [500, 100, 50, 10, 5, 1]

for coin in coin_type:
    count += money // coin  # money에서 coin으로 나눈 몫만큼 더함
    money %= coin # coin로 나눈 나머지를 money에 저장

print(count)