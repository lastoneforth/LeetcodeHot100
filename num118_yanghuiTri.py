from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = []
        result.append([1])
        result.append([1, 1])

        for num in range(2, numRows):
            temp = [1]
            for i in range(1, len(result[num - 1])):
                temp.append(result[num - 1][i - 1] + result[num - 1][i])
            temp.append(1)
            result.append(temp)

        return result


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))