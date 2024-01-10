import math
from typing import List


def majorityElement(nums: List[int]) -> int:
    nums.sort()

    head = 0
    length = len(nums)

    if length == 1:
        return nums[0]

    for i in range(1, length):
        if nums[i] != nums[head]:
            cur_len = i - head
            if cur_len > math.floor(length / 2):
                return nums[head]
            head = i

    # 如果前面都没有返回，说明最后一个元素就是多数元素
    return nums[length - 1]


def majorityElement1(nums: List[int]) -> int:
    temp = {}
    judge = math.floor(len(nums) / 2)

    for num in nums:
        try:
            temp[num] += 1
        except:
            temp[num] = 1

    for key, value in temp.items():
        if value > judge:
            return key


if __name__ == "__main__":
    nums = [3, 3, 4]
    print(majorityElement1(nums))
