def solution(participant, completion):
    srtlst1 = sorted(participant)
    srtlst2 = sorted(completion)
    
    for i in range(len(srtlst2)):
        if srtlst1[i] != srtlst2[i]:
            return srtlst1[i]
            
    return srtlst1[-1]