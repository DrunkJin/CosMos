def solution(id_list, report, k):
    answer = [0]*len(id_list)
    map_list = {}
    cnt_list = {} # id별 신고당한 count
    report = set(report)
    for i in report:
        a,b = i.split(' ')
        
        if b not in cnt_list: 
            cnt_list[b] = 1
        else:
            cnt_list[b] += 1

        if a not in map_list: # 신고한id, 신고당한 id 매핑
            map_list[a] = [b]
        elif b not in map_list[a]:
            map_list[a] += [b]
     
    for idx, n in cnt_list.items():
        if n >= k:
            for idx2, user2 in map_list.items():
                if idx in user2:
                    answer[id_list.index(idx2)] += 1
    return answer