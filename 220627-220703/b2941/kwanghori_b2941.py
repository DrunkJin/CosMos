class Example:

    def __init__(self, word:str):
        self.word = word

    def sol(self):
        '''
        c=, c-, dz=, d-, lj, nj, s=, z=
        '''
        cro_alphabets = ['c','d','l','n','s','z']       # 크로아티아 변환 알파벳의 첫번째 글자
        target = self.word
        cnt = 0
        for idx in range(len(self.word)):
            
            if idx == len(self.word) - 1:       # 인덱스 넘버 초과를 막기 위함
                if target[idx] in cro_alphabets:
                    cnt += 1
                    break
            elif target[idx] == 'c':    # c-, c=
                if target[idx+1] == '-' or target[idx+1] == '=':
                    cnt -= 1
            elif target[idx] == 'd' and target[idx+1] == '-':   # d-
                    cnt -= 1
            elif target[idx] == 'l' or target[idx] == 'n':  # lj, nj
                if target[idx+1] == 'j':
                    cnt -= 1
            elif target[idx] == 's':    # s=
                if target[idx+1] == '=':
                    cnt -= 1
            elif target[idx] == 'z':    # dz=
                if target[idx+1] == '=':
                    if target[idx-1] == 'd':
                        cnt -= 2
                    else:
                        cnt -= 1
            cnt += 1
        
        print(cnt)

                

    
if __name__ == "__main__":
    data = input()
    b2941 = Example(data)
    b2941.sol()
