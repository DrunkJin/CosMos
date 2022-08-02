def solution(s):
    answer = ''
    number_dic = {'zero':0, 'one':1,'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, \
                  'eight':8, 'nine':9}
    for i in number_dic:                    # 위에 만들어놓은 사전 돌려돌려돌림판
        s=s.replace(i, str(number_dic[i]))  # key값을 value값으로 치환(문자열로 해야 치환이 됨)
    return int(s)                           # 답안은 int값으로 반환