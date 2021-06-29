from typing import List
# @lc code=start
from typing import Mapping


class Solution:
    # # solution 1: O(n^2) 3544ms 15.2MB
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     # n ^ 2
    #     lens = len(nums)
    #     for i in range(lens-1):
    #         for j in range(i+1, lens):
    #             if nums[i] + nums[j] == target:
    #                 return i, j

    # # solution 2: O(nlogn) 64ms 16.5MB
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     new_nums = []
    #     for index, num in enumerate(nums):
    #         new_nums.append([num, index])

    #     new_nums.sort()
    #     min, max = 0, len(nums)-1
    #     while min < max:
    #         if new_nums[min][0] + new_nums[max][0] == target:
    #             return new_nums[min][1], new_nums[max][1]
    #         elif new_nums[min][0] + new_nums[max][0] > target:
    #             max -= 1
    #         else:
    #             min += 1

    # # solution 2: O(nlogn) 44ms 16.2MB
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     new_nums = [(num, index) for index, num in enumerate(nums)]

    #     new_nums.sort()
    #     min, max = 0, len(nums)-1
    #     while min < max:
    #         if new_nums[min][0] + new_nums[max][0] == target:
    #             return new_nums[min][1], new_nums[max][1]
    #         elif new_nums[min][0] + new_nums[max][0] > target:
    #             max -= 1
    #         else:
    #             min += 1


    # solution 3:  36ms 15.7MB
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for index in range(len(nums)):
            another = target - nums[index]
            try:
                hash_nums[another]
                return index, hash_nums[another]
            except:
                hash_nums[nums[index]] = index

# @lc code=end

if __name__ == '__main__':
    s = Solution()

    nums = [20, 2, 7, 11, 15]
    target = 9

    # nums = [3, 3]
    # target = 6

    print(s.twoSum(nums, target))