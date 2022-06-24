class Example:

    def __init__(self, init_num) -> None:
        self.num = init_num

    def sol(self):
        init = self.num
        new = 100   # 0 ~ 99 사이의 숫자와 중복되지 않는 임의의 값
        iter = 0    # init 갱신 횟수

        while(self.num != new):   # 입력 값과 결과값이 같아질때까지 연산
            
            split_num = [int(i) for i in list(str(init))]   # 숫자를 자릿수로 쪼개 리스트에 저장
            if len(split_num) == 2:   # 두자리 수 일때
                mid = split_num[0] + split_num[1]
                if mid < 10:
                    new = int(str(split_num[1])+str(mid))
                else:
                    new = int(str(split_num[1])+str(mid)[1])
            else:   # 한자리 수 일때 (0~99까지 범위이므로)
                mid = split_num[0]
                new = int(str(split_num[0])+str(mid))

            # 연산이 끝난 후 갱신 횟수 추가 및 init 변수 결과로 치환
            iter += 1    
            init = new
        print(iter)
        
if __name__ == "__main__":
    data = input()
    ex = Example(int(data))
    ex.sol()
