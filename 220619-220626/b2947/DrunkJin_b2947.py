# 5개를 리스트로 받아옴
wood = list(map(int, input().split()))

while True: # 예제를 보니 순차적으로 돌고 다시 반복하는 것을 확인함
    if sorted(wood) == wood: # 오름차순 정렬과 같아질 때까지 반복
        break
    else:
        for i in range(len(wood)-1): # 0,1,2,3 으로 나와있기 때문에 길이 4에서 1개 빼줌
            if wood[i] > wood[i+1]: # 다음 것보다 크면
                temp = wood[i] # 현재꺼 저장
                wood[i] = wood[i+1] # 현재 원소값을 바꿔줌
                wood[i+1] = temp  # 다음 원소값을 바꿔줌
                print(" ".join(map(str, wood))) # 바꿔준 내용 출력
            else:
                continue

