class example:
    
    def __init__(self, data, data_list) -> None:
        self.pnum, self.s = data
        self.correction = self.pnum * self.s
        self.data = data_list
        
    def sol(self):
        
        answer = [str(data - self.correction) for data in self.data]
        return " ".join(answer)


if __name__ == "__main__":
    data = [int(num) for num in input().split()]
    data_list = [int(num) for num in input().split()]
    result = example(data, data_list)
    print(result.sol())