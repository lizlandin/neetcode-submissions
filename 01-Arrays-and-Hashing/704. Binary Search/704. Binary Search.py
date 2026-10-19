1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        left = 0
4        right = len(nums)- 1
5        mid = (right + left) // 2
6        
7        while left <= right:
8            mid = (right + left) // 2
9            
10            if nums[mid] == target:
11                return mid 
12            elif nums[mid] > target:
13                right = mid - 1
14                
15            else:
16                nums[mid] < target
17                left = mid + 1
18                
19             
20        return -1
21        
22                
23
24
25
26
27
28
29
30
31
32
33        