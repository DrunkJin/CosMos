class Example:

    def __init__(self) -> None:
        '''
        인스턴스 초기화하며 변수를 받아옴
        '''
        self.num = int(input())

    def sol(self):
        init = self.num     # 연산 후 갱신돼야 하므로 init이라는 변수에 별도 저장
        new = 100   # 0 ~ 99 사이의 숫자와 중복되지 않는 임의의 값
        iter = 0    # init 갱신 횟수

        while(self.num != new):   # 입력 값과 결과값이 같아질때까지 연산
            
            split_num = [int(i) for i in list(str(init))]   # 숫자를 자릿수로 쪼개 리스트에 저장
            if len(split_num) == 2:   # init이 두자리 수 일때
                mid = split_num[0] + split_num[1]   # 각 자릿수 더하기
                if mid < 10:    # 더한 수가 10보다 작을때 (한 자리 수 일때)
                    new = int(str(split_num[1])+str(mid))
                else:       # 더한 수가 두 자리 수 일때
                    new = int(str(split_num[1])+str(mid)[1])
            else:   # init이 한자리 수 일때 (0~99까지 범위이므로)
                mid = split_num[0]
                new = int(f'{mid}{mid}')

            iter += 1       # 연산이 끝난 후 갱신 횟수 추가 및 init 변수 결과로 치환
            init = new
        print(iter)
        
if __name__ == "__main__":
    b1110 = Example()
    b1110.sol()
