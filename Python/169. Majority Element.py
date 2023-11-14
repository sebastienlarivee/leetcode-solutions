class Solution:  # Too slow lol
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        c = 0
        num = 0

        for num in nums:
            num = num
            c = nums.count(num)
            if c > n:
                break

        return num


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
