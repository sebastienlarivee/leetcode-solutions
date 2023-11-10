class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        while k < len(nums):
            if nums[k] == val:
                nums.pop(k)
            else:
                k += 1
        return k
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow