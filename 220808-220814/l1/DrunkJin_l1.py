class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,j in enumerate(nums):                             # 인덱스를 찾기 위해 enumerate
            iter_list = nums.copy()                             # 본인을 제외하고 포함된 값을 찾기 위해 복사
            iter_list.pop(i)                                    # 본인 제거
            check = target - j                                  # target - 본인 값이 list에 있는가?
            if check in iter_list:
                first_index = i
                second_index = nums.index(check)                # 찾은 경우 해당 인덱스들을 저장
                break
            else:
                continue
        if first_index == second_index:                         # [3,3] 6 인 경우 0,0으로 됨
            iter_list = nums.copy()                             # 처음것을 지우고 그 부분에 해당하는 값의 인덱스 + 1하면 두번째 숫자의 인덱스값이 됨
            iter_list.pop(first_index)
            second_index = iter_list.index(nums[first_index])+1
        answer = []
        answer.append(first_index)
        answer.append(second_index)
        return sorted(answer)                                   # 정렬하여 제출

        """
        Runtime: 1982 ms, faster than 27.96% of Python3 online submissions for Two Sum.
        Memory Usage: 14.8 MB, less than 95.53% of Python3 online submissions for Two Sum.
        """