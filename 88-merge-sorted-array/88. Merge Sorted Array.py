class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create new array to sort the newly added-together arrays into sorted numbers

        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()


