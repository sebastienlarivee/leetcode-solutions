class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        nums_bad = []
        while k < len(nums):
            if nums[k] in nums_bad:
                nums.pop(k)
            else:
                nums_bad.append(nums[k])
                k += 1
        return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()
        write_index = 0
        
        for read_index in range(len(nums)):
            if nums[read_index] not in seen:
                seen.add(nums[read_index])
                nums[write_index] = nums[read_index]
                write_index += 1
                
        return write_index
