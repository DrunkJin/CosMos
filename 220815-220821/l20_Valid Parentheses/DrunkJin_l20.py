class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{', ']':'['}
        check = []
        for i in s:                 
            if i in dic and check:
                tmp = dic[i]       
                if check[-1] == tmp:
                    check.pop()
                else:
                    check.append(i)
            else:
                check.append(i)
                
        if check:
            return False
        else:
            return True
"""
Runtime: 60 ms, faster than 22.64% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 71.12% of Python3 online submissions for Valid Parentheses.
"""