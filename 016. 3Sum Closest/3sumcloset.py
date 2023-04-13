class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # sort the list to easily move left and right pointers

        closet_sum = float('inf') # initialize closet sum to a large value

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closet_sum - target):
                    closet_sum = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                
                elif curr_sum < target:
                    left += 1

                else:
                    right -= 1

        return closet_sum