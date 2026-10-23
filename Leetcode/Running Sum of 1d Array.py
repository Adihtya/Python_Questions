class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        # Loop starting from the second element (index 1)
        for i in range(1, len(nums)):
            # Add the previous element's value to the current one
            nums[i] = nums[i] + nums[i - 1]
            
        return nums
