class Example:

    def __init__(self, data:int):
        self.S = data

    def sol(self):
        target = self.S
        answer = 0
        n = 0
        while(target > answer):   # 자연수 1부터 덧셈 연산, answer가 target보다 커질 경우 루프문 종료
            n += 1
            answer += n
        
        if target == answer:    # n(n+1)/2 = S 식을 따라 n 출력
            print(n)
        else:                   # n(n+1)/2 > S 이므로 n-1 출력
            print(n-1)

    
if __name__ == "__main__":
    data = input()
    b1789 = Example(int(data))
    b1789.sol()
