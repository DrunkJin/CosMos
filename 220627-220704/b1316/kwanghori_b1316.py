class Example:

    def __init__(self, n):
        self.n = n
    
    def sol(self):
        cnt = self.n  # 조건을 충족하지 못하는 단어의 갯수를 차감

        for _ in range(self.n):
            word = input()
            check = []    # 알파벳 저장을 위한 리스트
            for idx in range(len(word)):
                if word[idx] in check:  # 알파벳이 check 리스트에 존재할 경우
                    if word[idx-1] == word[idx]:  # 연속되는 경우 패스
                        pass
                    else:
                        cnt -= 1    # 아닌 경우 차감
                        break
                else:   # 알파벳이 check 리스트에 없는 경우
                    check.append(word[idx])

                
        return print(cnt)


if __name__ == "__main__":
    n = int(input())
    b1316 = Example(n)
    b1316.sol()
