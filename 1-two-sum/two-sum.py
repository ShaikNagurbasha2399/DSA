class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    dict={}
    for i,num in enumerate(nums):
        needed=target-num
        if needed in dict:
            return [dict[needed],i]
        dict[num]=i