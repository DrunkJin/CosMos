# 효율성 통과 못했습니다
def solution(participant, completion):
    re = participant.copy() 

    for p in participant:
        if p in completion:
            completion.remove(p)
            re.remove(p)

    return ','.join(re)