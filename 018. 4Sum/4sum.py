class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array to make it easier to check for duplicates
        nums.sort()
        n = len(nums)
        res = []
        # Loop through all possible pairs of indices i,j
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                # Skip duplicate values of i
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    # Skip duplicate values of j
                    continue
                # Use two pointers to find the other two numbers that add up to target
                left = j+1
                right = n-1
                while left < right:
                    # Check if the sum of the four numbers equals the target
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            # Skip duplicate values of left
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            # Skip duplicate values of right
                            right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return res
