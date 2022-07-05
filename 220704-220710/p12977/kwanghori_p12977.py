def solution(nums):
    # 라이브러리 사용x, 3중첩 for문,,,,
    array = []
    cnt = 0
    primes = []
    
    for i in range(len(nums)-2):    # index를 지정한 for문을 이용하게 되면 중복값이 없고, 계산속도 또한 줄일 수 있음
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                array.append(nums[i]+nums[j]+nums[k])
    
    for value in array:     # 2 ~ value 까지 나눗셈 중간에 한번이라도 나머지가 없을경우 break 모두 다 마치고 나오면 cnt += 1 (else 중요!!!)
        for n in range(2,value):
            if value % n == 0:
                break
        else: cnt += 1
    
    
    return cnt
                
    