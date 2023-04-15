class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1: Find the firt pair of adjacent elements(i, i+1) from the rightmost that satisfy nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # if no such pair is found, the list is already the highest permutation, so we reverse if to get the lowest permutation
        if i == -1:
            nums.reverse()
            return

        # step 2: Find the first element from the right that is greater than nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        #  step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # step 4: Reverse the sublist nums[i+1:] to get the lexicographically next greater permutation
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1