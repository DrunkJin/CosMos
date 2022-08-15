# 잘 돌아가긴 하는데, 어떻게 해야 사이트에서 돌아가는지 몰라서 우선 돌아가는대로 코드만 짬
class Solution:
    def isValid(s):
    
        dic = {'(': ')', '{': '}', '[':']'}

        result = []

        for d in dic.keys():
            if s.count(d) !=0:
                if s.count(d) == s.count(dic.get(d)):
                    result.append('true')

                else:
                    result.append('flase')

        if len(list(set(result))) == 1:
            res = 'true'

        else:
            res = 'flase'
        
        return res