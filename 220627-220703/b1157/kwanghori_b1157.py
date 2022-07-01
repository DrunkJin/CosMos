class Example:

    def __init__(self, data:str):
        self.word = data

    def sol(self):
        word = self.word.upper()           
        dic = dict()

        if len(word) == 1:     # 모두 한 글자 단어 입력 시 결과 출력
            return print(word)
        
        for tok in list(word):
            if tok in dic.keys():
                dic[tok] += 1
            else:
                dic[tok] = 1

        result = sorted(dic.items(), key=lambda x : x[1], reverse=True)     # result = [(alphabet1, value1), (alphabet2, value2), ...] 형태로 반환

        if len(set(word)) == 1:     # 모두 같은 글자일 경우
            print(word[0])
        elif result[0][1] == result[1][1]:  # 가장 많이 사용된 알파벳이 두개 이상인 경우
            print('?')
        else:
            print(result[0][0])

    
if __name__ == "__main__":
    data = input()
    b1157 = Example(data)
    b1157.sol()
