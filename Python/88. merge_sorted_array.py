class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Remove any extra zeros or unwanted elements from nums1
        del nums1[m:]

        # Extend nums1 with nums2
        nums1.extend(nums2[:n])

        # Sort nums1
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Create a copy of nums1 up to m elements
        nums1_copy = nums1[:m]

        # Pointers for nums1_copy and nums2
        p1, p2 = 0, 0

        # Index for modified nums1
        p = 0

        # Compare elements from nums1_copy and nums2 and merge.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        # If there are remaining elements in nums1_copy or nums2, add them.
        while p1 < m:
            nums1[p] = nums1_copy[p1]
            p1 += 1
            p += 1
        while p2 < n:
            nums1[p] = nums2[p2]
            p2 += 1
            p += 1
