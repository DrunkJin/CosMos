def solution(id_list, report, k):
    report = list(set(report))  # 같은 아이디의 중복신고 제거
    
    rep_rec = {}    # 신고된ID:신고횟수 딕셔너리
    tmp = []        # ex) [("muzi", "frodo"), ("apeach", "frodo")...]
    result = [0] * len(id_list) # id_list 갯수만큼 0 만들기
    
    for log in report:     # 신고 데이터, 유저ID와 신고된ID로 나누어 저장 ex) "muzi frodo"
        userID, reportedID = log.split()
        tmp.append(tuple([userID, reportedID]))
        if reportedID in rep_rec.keys():
            rep_rec[reportedID] += 1
        else: 
            rep_rec[reportedID] = 1
    
    suspend = tuple([key for key, val in rep_rec.items() if val >= k])  # 이용정지된 아이디 목록 저장
    tmp = tuple(tmp)    # 연산속도를 위해 튜플로 변환
    
    for idx in range(len(id_list)):
        for userID, reportedID in tmp:        
            if id_list[idx] != userID:
                pass
            else:
                if reportedID not in suspend:
                    pass
                else: 
                    result[idx] += 1
                
    return result
  
  
# 튜플 변환해서 시간 겨우 통과... 매우 별로인듯..
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (9728.54ms, 62.1MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.1MB)
테스트 6 〉	통과 (4.36ms, 10.5MB)
테스트 7 〉	통과 (6.72ms, 10.7MB)
테스트 8 〉	통과 (8.10ms, 11.3MB)
테스트 9 〉	통과 (2381.46ms, 34MB)
테스트 10 〉	통과 (1929.07ms, 34.1MB)
테스트 11 〉	통과 (9516.36ms, 62.1MB)
테스트 12 〉	통과 (2.45ms, 10.4MB)
테스트 13 〉	통과 (2.27ms, 10.3MB)
테스트 14 〉	통과 (3543.13ms, 30.2MB)
테스트 15 〉	통과 (4166.19ms, 43MB)
테스트 16 〉	통과 (0.60ms, 10.2MB)
테스트 17 〉	통과 (2.43ms, 10.4MB)
테스트 18 〉	통과 (4.79ms, 10.2MB)
테스트 19 〉	통과 (9.15ms, 10.2MB)
테스트 20 〉	통과 (3536.10ms, 30.2MB)
테스트 21 〉	통과 (4388.05ms, 43MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
'''
