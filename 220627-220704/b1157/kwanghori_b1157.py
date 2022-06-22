class Example:

    def __init__(self, data:str):
        self.word = data

    def sol(self):
        if len(self.word) == 1:   # 한 글자의 단어 입력 시 바로 결과 출력
            return print(self.word.upper())
            
        word = self.word.upper()  # 단어 대문자 변환
        dic = dict()
        for idx in range(len(word)):
            if word[idx] in dic.keys():
                dic[word[idx]] += 1
            else:
                dic[word[idx]] = 1

        result = sorted(dic.items(), key=lambda x : x[1], reverse=True)

        if result[0][1] == result[1][1]:
            print('?')
        else:
            print(result[0][0])

    
if __name__ == "__main__":
    data = input()
    b1157 = Example(data)
    b1157.sol()
