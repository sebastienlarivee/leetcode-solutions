class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, currentEnd, farthest = 0, 0, 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        return jumps