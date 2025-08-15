class Solution:
    def robHouse(self, nums, n):
        prev2 = 0
        prev = nums[0]

        for i in range(1, n):
            pick = nums[i] + prev2
            not_pick = prev
            curr = max(pick, not_pick)
            prev, prev2 = curr, prev

        return prev
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        return max(self.robHouse(nums[:n-1], n-1), self.robHouse(nums[1:], n-1))    