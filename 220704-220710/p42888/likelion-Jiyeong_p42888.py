def solution(record):
    result = []
    dict_id = {}
    msg_arr = []
    for i in record:
        result.append(i.split())
    
    for x in result:
        if len(x) == 3:     # Enter와 Change의 경우 딕셔너리가 update 되야함
            dict_id[x[1]] = x[2]

    for x in result:
        if x[0] == "Enter":
            msg_arr.append(dict_id[x[1]]+"님이 들어왔습니다.")
        elif x[0] == "Leave":
            msg_arr.append(dict_id[x[1]]+"님이 나갔습니다.")
         
    return msg_arr


