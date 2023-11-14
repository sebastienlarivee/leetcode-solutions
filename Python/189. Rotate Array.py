class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)

        if k == 0:
            return nums

        rotate_nums = nums[-k:]
        del nums[-k:]
        nums[0:0] = rotate_nums
