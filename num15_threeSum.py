from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        if len(nums) < 3:  # 特殊情况
            return result

        nums.sort()

        for i in range(len(nums)):

            if nums[i] > 0:
                return result  # 结束条件之一，三个数的第一个数大于0，后续不可能再有和为0的组合，直接返回

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 重复元素，跳过

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])  # 找到一个组合
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    right -= 1
                    left += 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
