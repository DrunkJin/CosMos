class example:
    def __init__(self, price):
        self.price = price

    def sol(self):
        target = 1000-self.price
        cnt = 0
        changes = [500,100,50,10,5,1]

        for change in changes:
            while True:
                if target // change == 0:
                    break
                else:
                    cnt += target // change
                    target = target % change
        return print(cnt)

if __name__ == '__main__':
    b5585 = example(int(input()))
    b5585.sol()
