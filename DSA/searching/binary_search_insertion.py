class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if target < nums[mid]: h = mid - 1
            elif target > nums[mid]: l = mid + 1
            else: return mid
        return l