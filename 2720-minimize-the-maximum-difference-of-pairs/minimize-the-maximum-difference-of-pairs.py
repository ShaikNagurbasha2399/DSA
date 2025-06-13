class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def pairing(diff):
            count = i = 0
            while i < n - 1 and count < p:
                if nums[i + 1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if pairing(mid):
                r = mid
            else:
                l = mid + 1
        return l