# 테스트 25 ~ 32는 100ms ~ 150ms 정도 소요되네요.
def solution(record):
    answers = []    # 채팅방에 출력될 메세지를 담을 리스트
    data = []       # 명령과 유저id를 저장할 리스트
    user_dict = {}  # 유저id와 닉네임을 딕셔너리 형태로 업데이트
    
    # User Nickname Update
    for log in record:
        try:    # Enter, Change 일때 ex) Enter uid1234 Muzi
            event, user_id, nickname = log.split()   
        except: # Leave 일때 ex) Leave uid1234
            event, user_id = log.split()
        
        data.append([event, user_id])  # event와 유저id 저장

        if event == "Enter" or event == "Change":   # 입장하거나 닉네임을 바꿀때 딕셔너리 업데이트
            user_dict[user_id] = nickname
       
    # 메세지 출력
    for command, user_id in data:   # 모든 로그는 최신화된 닉네임으로 출력돼야 하므로 마지막에 출력함
        if command == "Enter":
            answers.append(f'{user_dict[user_id]}님이 들어왔습니다.')
        elif command == "Leave":
            answers.append(f'{user_dict[user_id]}님이 나갔습니다.')

    return answers
