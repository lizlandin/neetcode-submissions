1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        left = 0
4
5        for right in range(len(nums)):
6            if nums[right] != 0:
7                nums[left], nums[right] =  nums[right], nums[left]
8                left += 1
9                
10        
11                
12
13
14        
15
16
17
18
19
20        
21        