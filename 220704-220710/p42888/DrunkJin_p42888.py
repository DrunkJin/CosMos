def solution(record):
    answer = []
    check = {}  # 닉네임 딕셔너리
    for msg in record:
        msg = msg.split(" ") 
        if "Leave" in msg:
            pass
        else:
            check[msg[-2]] = msg[-1]    # Enter uid1234 Prodo, Change uid1234 Ryan => 모두 이런 식. 1,2로 해도 될듯함
        
    for msg in record: # 출력부분에서 고민을 많이 함. uid가 포함된 부분만 사용할 수 없을 지에 대해서 그런데 찾지 못하였음
        msg = msg.split(" ")
        if "Change" in msg:
            pass
        else:
            if len(msg) == 3:   # Enter의 경우가 길이가 3임 "Enter" in msg라고 해도 될듯. 그렇게 하는게 더 직관적인 것 같기도하고 
                answer.append(f"{check[msg[1]]}님이 들어왔습니다.")
            else:
                answer.append(f"{check[msg[1]]}님이 나갔습니다.")
            
    return answer

"""
작년에 이 문제보고 뭔가 되게 까다롭게 생겨서 어려울 것이라고 생각했는데 생각보다 방법이 금방 생각난 걸 보면 조금씩 늘고 있나봄
"""