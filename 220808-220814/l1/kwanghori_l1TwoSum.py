# 브루트포스 알고리즘을 이용한 index 값 구하기 (전체 탐색으로 속도가 빠르지 않음)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
