from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = cursor = 0
        tail = len(nums) - 1

        while cursor <= tail:

            if nums[cursor] == 2:
                nums[cursor], nums[tail] = nums[tail], nums[cursor]
                tail -= 1

            elif nums[cursor] == 0:  # 因为2都会被移到后面，所以前面被换过来的只能1
                nums[cursor], nums[head] = nums[head], nums[cursor]
                head += 1
                cursor += 1

            else:
                cursor += 1


if __name__ == "__main__":
    nums = [0, 2, 2, 1, 1, 2, 0]
    Solution().sortColors(nums)
    print(nums)

