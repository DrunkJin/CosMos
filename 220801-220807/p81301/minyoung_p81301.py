dicts = {'zero': '0', 'one':'1', 'two': '2', 'three':'3', 'four':'4','five':'5'
         ,'six':'6', 'seven':'7', 'eight':'8', 'nine': '9'}

def solution(s):
    for d in dicts.keys():
        if s.find(d) != -1:
            s = s.replace(d, dicts.get(d))
            
    return int(s)


# 약 2달 전 코드
# dicts = {'zero': '0', 'one':'1', 'two': '2', 'three':'3', 'four':'4','five':'5'
#          ,'six':'6', 'seven':'7', 'eight':'8', 'nine': '9'}
# values = list(dicts.keys())

# def solution(mysite):
#     for i in range(len(values)):
#         if values[i] in mysite:
#             mysite = mysite.replace(values[i], dicts[values[i]])
            
#     return int(mysite)