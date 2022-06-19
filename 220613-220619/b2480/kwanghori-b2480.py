class example:
    
    def __init__(self, data) -> None:
        self.i, self.j, self.k = data
        self.data = data
        # print(f"입력된 값: {self.i}, {self.j}, {self.k}")
        
    def sol(self):
        
        if self.i == self.j == self.k:
            return 10000 + 1000*self.i
        
        elif self.i!=self.j and self.j!= self.k and self.i!=self.k:
            return max(self.data)*100
        
        else:
            if self.i == self.j:
                return 1000+100*self.i
            elif self.i == self.k:
                return 1000+100*self.i
            else:
                return 1000+100*self.j


if __name__ == "__main__":
    data = [int(num) for num in input().split()]
    result = example(data)
    print(result.sol())