class Example:

    def __init__(self, data):
        self.words = [word for word in data.split()]
        print(len(self.words))
    
if __name__ == "__main__":
    data = input()
    a = Example(data)
