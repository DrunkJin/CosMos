class example:
    def __init__(self, price):
        self.price = price

    def sol(self):
        target = 1000-self.price    # 받을 거스름돈
        cnt = 0     # 지폐 및 동전의 개수
        changes = [500,100,50,10,5,1]   # 거스름돈 종류

        for change in changes:
            while True:
                if target // change == 0:   # 해당된 거스름돈을 줄 수 없는 경우 break
                    break
                else:
                    cnt += target // change     # 몫 = 거스름돈 개수
                    target = target % change    # 나머지= 나머지 거스름돈으로 
        return print(cnt)

if __name__ == '__main__':
    b5585 = example(int(input()))
    b5585.sol()
