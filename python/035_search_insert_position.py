
class Solution:
    # solution 1: O(1), 32ms, 15.3MB
    def searchInsert(self, nums: List[int], target: int) -> int:
        min, max = 0, len(nums) - 1
        while min <= max:
            if target <= nums[min]:
                return min
            min += 1
        return max + 1
    # solution 2: O(logn) 44ms, 15.4MB
    def searchInsert(self, nums: List[int], target: int) -> int:
        min, max = 0, len(nums) - 1
        mid = 0

        while min <= max :
            mid = int((min + max) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                max = mid - 1
            else:
                min = mid + 1
        if  min > mid :
            return mid + 1
        return mid