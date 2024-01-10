from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 1:
            return 1

        nums.sort()

        head = tail = 0
        max_len = 0
        cur_len = 0
        while tail <= length - 1:

            if nums[tail] - nums[head] == tail - head:  # 连续数字
                tail += 1
                cur_len += 1
            else:
                head = tail
                tail += 1
                max_len = cur_len if cur_len > max_len else max_len
                cur_len = 0

        return max(max_len, cur_len+1)


if __name__ == "__main__":
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    print(Solution().longestConsecutive(nums))
