class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        map = {}

        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1
            res += map[n] - 1
        return res