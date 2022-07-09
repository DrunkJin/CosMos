def solution(id_list, report, k):
    dic_singo = {}
    mail = []
    answer = []

    for rep in report:
        a, b = rep.split()

        if b not in dic_singo.keys():
            dic_singo[b] = []

        if a not in dic_singo[b]:
            dic_singo[b].append(a)

    for user in dic_singo.keys():
        if len(dic_singo[user]) >= k:
            mail += dic_singo[user]

    for user in id_list:
        answer.append(mail.count(user))

    return answer