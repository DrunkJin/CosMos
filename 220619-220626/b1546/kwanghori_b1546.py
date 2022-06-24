class Example:

    def __init__(self, times, scores):
        self.times = times
        self.scores = scores
    
    def sol(self):
        max_score = max(self.scores)
        total_scores = 0
        for idx in range(len(self.scores)):
            total_scores += self.scores[idx] / max_score * 100

        print(f'{total_scores/self.times:.4f}')

    
if __name__ == "__main__":
    times = int(input())
    scores = [int(i) for i in input().split()]
    b1546 = Example(times, scores)
    b1546.sol()
