dice = list(map(int, input().split()))

result = 0
if len(set(dice)) == 1:
    result = (dice[0] * 1000) + 10000
    
elif len(set(dice)) == 2:
    if dice.count(list(set(dice))[0]) == 2:
        result = 1000 + list(set(dice))[0]*100
    else:
        result = 1000 + list(set(dice))[1]*100
else:
    result = max(dice) * 100
    
print(result)