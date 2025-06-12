class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        sum=0
        for n in nums:
            if sum<0:
                sum=0
            sum+=n
            maxSub=max(maxSub,sum)
        return maxSub
        