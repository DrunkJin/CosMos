l, p = map(int, input().split())
news = list(map(int, input().split()))

people = l*p

news = list(map(lambda x : x - people, news))

result = " ".join(map(str, news))


# for i in news:
#     result += str(i)+" "
    
print(result)