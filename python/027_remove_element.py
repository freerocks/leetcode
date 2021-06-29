# @lc code=start
class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     lc = len(nums)
    #     if lc == 0:
    #         return 0
    #     left = 0
    #     for i in range(lc):
    #         if nums[i] == val:
    #             continue
    #         else:
    #             nums[left] = nums[i]
    #             left += 1
    #     return left
    def removeElement(self, nums: List[int], val: int) -> int:
        lc = len(nums)
        if lc == 0:
            return 0

        index = 0
        count = 0
        while index < lc - count:
            if nums[index] == val:
                nums[index] = nums[lc - 1 - count]
                count += 1
            else:
                index += 1
        return lc - count
# @lc code=end