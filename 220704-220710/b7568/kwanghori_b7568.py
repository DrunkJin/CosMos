class example:

    def __init__(self, array) -> None:
        self.array = array

    def sol(self):
        records = []   # 등수를 저장
        for tup_1 in self.array:    #등수를 판별할 데이터
            k = 1
            for tup_2 in self.array:    # 비교 데이터
                if tup_1 == tup_2: pass  # 자기자신이므로 넘어감
                elif tup_1[0] < tup_2[0] and tup_1[1] < tup_2[1]:   # 비교 데이터가 키와 몸무게 모두 크다면 +1등
                    k += 1
                else: pass
            
            records.append(str(k))

        return print(' '.join(records))

if __name__ == '__main__':
    physical_record = []
    for _ in range(int(input())):
        a,b = input().split()
        physical_record.append((int(a),int(b)))     # 몸무게와 키를 튜플로 받아 리스트에 저장 ex) [(weight1, height1), ...]
    b7568 = example(physical_record)
    b7568.sol()
