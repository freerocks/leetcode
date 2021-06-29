
class Solution:
    # solution 1: O(1), 32ms, 15.3MB
    def searchInsert(self, nums: List[int], target: int) -> int:
        min, max = 0, len(nums) - 1
        while min <= max:
            if target <= nums[min]:
                return min
            min += 1
        return max + 1