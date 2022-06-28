class Example:

    def __init__(self, k, n):
        self.k = k
        self.n = n
    
    def sol(self):
        '''
        양의 정수 k,n에 대해 k층에 n호에는 몇 명이 살고 있는지 계산
        '''
        if n==1:
            return print(1)
        floor = 0
        array = [None] * self.n     # n개의 data를 받을 수 있는 리스트 생성
        ground_floor = [i for i in range(1,self.n+1)]   # 아래층 숫자, 초기엔 0층

        while floor != self.k:
            for idx in range(self.n): 
                if idx == 0:    # 1호의 거주자 수는 항상 1명
                    array[idx] = ground_floor[0]
                else:   # 아래층 1~n호 까지의 합은 다음 식과 같음
                    array[idx] = array[idx-1] + ground_floor[idx]
            
            floor += 1  # 층 올라가기
            ground_floor = array    # 아래층 숫자 업데이트
        return print(array[self.n-1])

if __name__ == "__main__":
    times = int(input())
    for _ in range(times):
        k = int(input())
        n = int(input())
        b2775 = Example(k, n)
        b2775.sol()
