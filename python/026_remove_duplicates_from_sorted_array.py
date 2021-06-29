# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lc = len(nums)
        if lc == 0:
            return 0

        pos = 0
        for i in range(1, lc):
            if nums[pos] == nums[i]:
                continue
            else:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1

# @lc code=end
