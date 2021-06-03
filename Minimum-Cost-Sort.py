class Solution:
    def solve(self, nums):
        l1 = sorted(nums)
        l2 = sorted(nums, reverse = True)
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            sum1 += abs(nums[i]-l1[i])
        for i in range(len(nums)):
            sum2 += abs(nums[i]-l2[i])
        return(min(sum1,sum2))