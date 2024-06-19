class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0
        
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] != 0 and nums[j - 1] == 0:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1


        return nums
