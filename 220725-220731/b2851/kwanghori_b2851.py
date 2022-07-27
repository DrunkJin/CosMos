def Reach100():
    scores = [0, 0]     # 결과 출력 시점에서 비교하기 위해 두 수를 리스트에 저장
    i = 0       # 10번을 확인하기 위한 변수
    while (scores[1] < 100):
        
        score = int(input())    
        scores[0] = scores[1]   
        scores[1] += score      
        i += 1  # 횟수 카운트

        if scores[1] >= 100:        # 결과 출력은 총합이 100 이상일 때 부터
            if abs(100 - scores[0]) < abs(scores[1] - 100):     # 100에 더 가까운 수를 반환, 작은 수를 반환하는 유일한 경우
                return scores[0]    
            else:
                return scores[1]

        if i == 10:     # 10개의 숫자를 모두 더해 100이 넘지 않더라도 반환해주어야함, 이 조건이 없을 때 런타임 에러 발생...
            return scores[1]
if __name__ == '__main__':
    print(Reach100())
    
    
메모리  시간
30840KB 68ms    
