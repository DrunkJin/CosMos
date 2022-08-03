def solution(priorities, location) :
    # 문서들의 최초 인덱스 저장
    idx = [i for i in range(len(priorities))]
    d = {}
    cnt = 1

    # 문서를 정렬하여 한개씩 출력
    # 출력이 끝날때까지 반복
    # 문서 중요도 priorities 와 문서들의 최초 인덱스 idx 리스트가 함께 변경됨
    while priorities :
        # 중요도 최대값 문서 인덱스 추출
        first = priorities.index(max(priorities))
        # 중요도 최대값 문서 앞 문서들 추출 (중요도에 밀려서 뒤로 정렬 필요)
        tmp_p = priorities[:first]
        tmp_i = idx[:first]
        # 중요도 최대값 부터 뒷 문서들로 리스트 업데이트
        priorities = priorities[first:]
        idx = idx[first:]
        # 중요도 최대값보다 앞에 있던 문서들(tmp_p,tmp_i)을 뒤로 붙이기
        priorities.extend(tmp_p)
        idx.extend(tmp_i)
        # 중요도 최대값 문서 출력 pop
        im = priorities.pop(0)
        key = idx.pop(0)
        # 출력된 문서의 최초 인덱스를 key로 , 출력된 순서를 value로 딕셔너리에 저장
        d[key] = cnt
        cnt += 1

    return d[location]