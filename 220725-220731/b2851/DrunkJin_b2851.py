total = 0                                           # 마리오가 먹은 점수의 합
for _ in range(10):                                 # 10개의 버섯이 주어짐
    mushroom = int(input())                         # 순서대로 먹어야하므로 매번 버섯의 점수를 받아옴
    if total + mushroom <= 100:                     # 총합 + 버섯의 점수가 100점과 같거나 작다면 더해줌
        total += mushroom
    else:
        if (100-total) < (total+mushroom-100):      # 총합 + 버섯점수 가 그 이전보다 100과의 차이가 크다면 멈춤
            break
        else:                                       # 그 외엔 더해주고 반복중지
            total += mushroom
        break

print(total)


"""
메모리 30840KB
시간 72ms
"""