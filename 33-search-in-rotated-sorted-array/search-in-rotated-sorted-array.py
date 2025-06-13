class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        left, right = 0, len(nums) - 1
        pivot = -1

        # pivot (index of largest element)
        while left <= right:
            mid = (left + right) // 2

            if mid < n and nums[mid] > nums[mid + 1]:  
                pivot = mid
                break  

            if nums[mid] < nums[left]:  
                right = mid - 1
            else:  
                left = mid + 1

        def binary_search(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if pivot == -1:
            return binary_search(nums, 0, n, target)

        if nums[0] <= target <= nums[pivot]:
            return binary_search(nums, 0, pivot, target)
        return binary_search(nums, pivot + 1, n, target)
        