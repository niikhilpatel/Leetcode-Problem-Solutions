class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Binary search to find the leftmost position of the target
        def findLeft(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        #  Binary search to find the rightmost position of the target
        def findRight(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Call the helper to find the first and last position of the target
        left_idx = findLeft(nums, target)
        right_idx = findRight(nums, target)
        return [left_idx, right_idx]
