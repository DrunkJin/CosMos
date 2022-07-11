def solution(id_list, report, k):
    #0. 중복된 신고는 무시함
    report = list(set(report))
    report_dic = {}
    answer_dic = {}
    #1. 리포트 횟수를 저장하는 딕셔너리 생성
    for i in report:
        violator = i.split()[1]
        if violator in report_dic:
            report_dic[violator] += 1
        else:
            report_dic[violator] = 1
    #2. 제재 성공 횟수를 알기 위한 딕셔너리 생성
    for member in id_list:
        answer_dic[member] = 0
    
    #3. 리포트를 보며 violator값이 report_dic에서 k이상의 값이면 reporter를 1개 더해줌
    for i in report:
        reporter = i.split()[0]
        violator = i.split()[1]
        if report_dic[violator] >= k:
            answer_dic[reporter] += 1

    return list(answer_dic.values())

    """
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (211.24ms, 39.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (1.27ms, 10.3MB)
테스트 7 〉	통과 (1.80ms, 10.7MB)
테스트 8 〉	통과 (2.32ms, 10.9MB)
테스트 9 〉	통과 (98.43ms, 23.9MB)
테스트 10 〉	통과 (79.50ms, 23.8MB)
테스트 11 〉	통과 (197.73ms, 39.4MB)
테스트 12 〉	통과 (0.24ms, 10.2MB)
테스트 13 〉	통과 (0.33ms, 10.4MB)
테스트 14 〉	통과 (66.73ms, 20MB)
테스트 15 〉	통과 (150.11ms, 31.3MB)
테스트 16 〉	통과 (0.28ms, 10.4MB)
테스트 17 〉	통과 (0.22ms, 10.4MB)
테스트 18 〉	통과 (0.48ms, 10.3MB)
테스트 19 〉	통과 (0.74ms, 10.3MB)
테스트 20 〉	통과 (63.30ms, 20MB)
테스트 21 〉	통과 (101.23ms, 31.4MB)
테스트 22 〉	통과 (0.01ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10.1MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
    """