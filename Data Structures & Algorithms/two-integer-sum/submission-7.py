# Inputs: nums: List[int], target: int
# Goal: find indices i and j such that nums[i] + nums[j] == target
#
# Constraints:
# - nums.length is between 2 and 1000
# - there is always a solution
# - there is always ONE valid solution
# 
# Questions:
#
# Initial solution:
# Bruetforce - for each item i, check all of the other items in the list, see if that is equal to target
# (C) Time: O(N^2)
# (C) Space: O(1)
# 
# Optimization:
# - we use a hashmap, keys = items inside list, values = indices of the keys
# - then we iterate through the list, and check if the difference between the target and our current item is found in the map
# (C) Time: O(n)
# (C) Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []
        