class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        text = s.split()
        return len(text[-1])
    
obj = Solution()
res = obj.lengthOfLastWord("   fly me   to   the moon  ")
