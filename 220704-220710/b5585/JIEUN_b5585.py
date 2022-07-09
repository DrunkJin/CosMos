def solution() :
    pay = int(input())
    budget = 1000
    change = (budget-pay)
    changes = [500, 100, 50, 10, 5, 1]
    answer = 0

    if change > 500  :
        changes = changes
    elif change > 100 :
        changes = changes[1:]
    elif change > 50 :
        changes = changes[2:]
    elif change > 10 :
        changes = changes[3:]
    elif change > 5:
        changes = changes[4:]
    elif change > 1 :
        changes = changes[5:]

    for i in changes :
        if change == 0 : break
        n = change//i
        change -= i*n
        answer += n

    print(answer)

solution()