# 6 12 10 -> 402, 30 50 72 -> 1203

t = int(input()) # 몇번 반복해서 볼 것인지


for _ in range(t):
    h, w, n = map(int, input().split())  # 높이, 길이, 손님선착순번호 받음
    if n % h == 0:  # 손님순서를 높이로 나눈 것의 나머지가 0이면 높이 층의 몫호실
        floor = str(h)
        number = n // h

    else:
        floor = str(n % h)  # 나머지가 있으면 몫이 층이 되고 몫+1 이 방번호가 됨
        number = (n // h) + 1
        
    if number < 10: # 12층 11호실의 경우 이 작업을 안해추면 12011호가 되어버림
        room = floor + '0' + str(number)
    else:
        room = floor + str(number)
    
    print(room)