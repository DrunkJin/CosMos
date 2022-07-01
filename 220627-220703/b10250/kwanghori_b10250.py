class example:

    def __init__(self, h, w, n):
        '''
        w 개의 방이 있는 h층 건물
        n번째 손님
        '''
        self.h = h
        self.w = w
        self.n = n

    def sol(self):
        # 호실 계산
        if self.n / self.h == self.n // self.h:     # ex) 6 1 6 일때 602 출력과 같은 경우를 제외하기 위함
            room_num = self.n // self.h
        else:
            room_num = (self.n // self.h) + 1
        # 층 계산
        floor = self.n % self.h                     # 꼭대기 층에서의 예외 처리 ex) 6 1 6 일때 001 출력
        if floor == 0:
            floor = self.h
        if room_num < 10:                           # ##호 이므로 자릿수를 맞춰주기 위함
            return print(f'{floor}0{room_num}')
        else:
            return print(f'{floor}{room_num}')

if __name__ == '__main__':
    for _ in range(int(input())):
        h,w,n = [int(i) for i in input().split()]
        b10250 = example(h,w,n)
        b10250.sol()
