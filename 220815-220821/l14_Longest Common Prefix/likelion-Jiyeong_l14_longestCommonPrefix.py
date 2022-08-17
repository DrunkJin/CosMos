from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length==0:
            return ""
        if length==1:
            return strs[0]
        strs.sort()
        end = min(len(strs[0]), len(strs[length-1])) # 가장 처음단어와 마지막 단어 중 최소 length 찾기
        
        i=0
        while (i < end and strs[0][i]==strs[length-1][i]):
            i+=1
        
        pre = strs[0][0:i]
        return pre
            
        
obj = Solution()
res = obj.longestCommonPrefix(["flower","flow","flight"])