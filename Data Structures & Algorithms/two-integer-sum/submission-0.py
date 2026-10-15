class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}

        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in indices:
                return [indices[complemento], i]
            indices [num] = i
            

        