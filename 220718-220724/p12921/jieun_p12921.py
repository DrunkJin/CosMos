def solution(n) :
    # (n+1)개의 0으로 채워진 리스트 생성
    # 여기에 소수는 1로 , 어떤 수의 배수는 -1로 체크 할 예정
    lst =  [0] * (n+1)
    # lst[0] 과 lst[1]은 0
    # lst[2] 부터 배수를 -1로 체크해서 제외하기
    for i in range(2,n+1) :
        # 만약 0인 상태라면 1로 체크 (i가 어떤 수의 배수라서 -1로 체크되어 있다면 변경하지 않음)
        if lst[i] == 0 :
            lst[i] = 1
        j = 2
        while i*j < (n+1) : # i 의 배수 -1로 체크
            lst[i*j] = -1
            j += 1

    return lst.count(1)