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