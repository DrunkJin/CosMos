
word = input()

word = word.upper() # 모두 대문자로 변환

if len(set(word)) == 1: # 한가지 글자로 이루어진 경우 하나 출력
    print(word[0])
    
else:
    count_dict = {} # 알파벳 숫자 셀 딕셔너리 생성
    for alpha in word: # 단어에서 알파벳을 하나씩 넣어봄
        if alpha in count_dict: # 딕셔너리에 알파벳이 있다면 +1
            count_dict[alpha] += 1
            
        else: #딕셔너리에 알파벳이 없다면 1 생성
            count_dict[alpha] = 1 

    sort_count_dict = sorted(count_dict, key = lambda x : count_dict[x], reverse=True) # 생성된 딕셔너리를 내림차순 정렬 => 키값이 내림차순정렬로 리스트형태로 저장됨

    if count_dict[sort_count_dict[0]] == count_dict[sort_count_dict[1]]: # 딕셔너리에서 생성해둔 리스트에서 첫번째와 두번째의 value값이 같다면 물음표 출력
        print("?")

    else:
        print(sort_count_dict[0]) # 그 이외에는 리스트 첫번째값 출력