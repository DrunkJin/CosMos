# strip을 이용한 양 옆의 공백 제거 후, 
# 띄어쓰기로 split,
# 마지막 단어 [-1]를 선택 후 
# 길이 len() return

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(' ').split(' ')[-1])
      
# Runtime: 50 ms, faster than 41.66% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.9 MB, less than 39.32% of Python3 online submissions for Length of Last Word.
