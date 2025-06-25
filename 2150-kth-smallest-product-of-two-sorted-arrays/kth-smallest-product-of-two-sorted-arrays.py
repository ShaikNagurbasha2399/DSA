class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def pair(x):
            count = 0
            for n1 in nums1:
                if n1 > 0:
                    count += bisect.bisect_right(nums2, x // n1)
                elif n1 < 0:
                    count += len(nums2) - bisect_left(nums2, ceil(x / n1))
                elif x >= 0:
                    count += len(nums2)
            return count

        low = -10**10 - 1
        high = 10**10 + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if pair(mid) >= k:
                high = mid
            else:
                low = mid
        return low + 1