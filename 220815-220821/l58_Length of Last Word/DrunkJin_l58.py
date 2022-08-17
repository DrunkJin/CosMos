class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])

"""
Runtime: 36 ms, faster than 82.49% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 80.81% of Python3 online submissions for Length of Last Word.
"""