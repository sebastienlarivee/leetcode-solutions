class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = nums[0]
        for i in range(1, len(nums)):
            if maxReach < i:  # if we're stuck and can't reach this index
                return False
            maxReach = max(maxReach, i + nums[i])
        return True