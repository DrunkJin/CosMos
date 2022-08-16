# while 문 활용, I, X, C의 경우 뒷 문자 고려, 한번 건너 뛰어야 하므로 i를 한번 더 더함, 중복 코드가 너무 많음

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        length = len(s)
        i = 0

        while (i != length):
        
            if s[i] == 'I':
                result += 1
                try:
                    if s[i+1] == 'V':
                        result += 3
                        i += 1
                    elif s[i+1] == 'X':
                        result += 8
                        i += 1
                    
                except: pass
                    
            
            elif s[i] == 'X':
                result += 10
                try:
                    if s[i+1] == 'L':
                        result += 30
                        i += 1
                    elif s[i+1] == 'C':
                        result += 80
                        i += 1
                except: pass

            elif s[i] == 'C':
                result += 100
                try:
                    if s[i+1] == 'D':
                        result += 300
                        i += 1
                    elif s[i+1] == 'M':
                        result += 800
                        i += 1
                except: pass
            
            elif s[i] == 'V':
                result += 5
            
            elif s[i] == 'L':
                result += 50
            
            elif s[i] == 'D':
                result += 500
            
            elif s[i] == 'M':
                result += 1000
            i += 1

        return result
      
# Runtime: 66 ms, faster than 69.21% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 31.19% of Python3 online submissions for Roman to Integer.
