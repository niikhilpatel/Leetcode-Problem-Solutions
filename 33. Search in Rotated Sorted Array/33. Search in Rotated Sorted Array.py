class Solution:
    def search(self, nums, target):
        """
        Searches for target in a rotated sorted array using binary search.

        args:
        nums(List[int]): Rotated sorted array
        target(int): Target element to search for

        Return:
            int: Index of the target element in the array, or -1 if not found
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the left half
                    right =  mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
            
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # target is in the right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1
        
        return -1
