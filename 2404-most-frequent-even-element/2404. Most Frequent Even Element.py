class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        max_even = -1
        max_length = 1

        while l < len(nums):
            if nums[l] % 2 == 0:
                length = 1
                r = l
                while r < len(nums) and nums[r] == nums[l]:
                    r += 1
                    length = r - l + 1

                if length > max_length:
                    max_even = nums[l]
                    max_length = length
                l = r
            else:
                l += 1
        return max_even       