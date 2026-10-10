# Input: nums: List[int], target: int
# Goal: return indices i and j such that nums[i] + nums[j] == target AND i != j
# 
# Constraints:
# - always 1 unique solution
# - return the smaller index first (so [i,j] where i < j)
# - nums is NOT empty
# - 2 <= numss.length <= 1000
#
# Scenarios:
# - inp: nums = [3,4,5,6], target = 7
# - out: [0,1]
#
# - inp: nums = [5,5], target = 10
# - out: [0,1]
#
# Initial plan (Bruteforce):
# - iterate over nums, for each item i
# - compare all the other items with this item i to see if it equals to the target
# (C) Time: O(n^2)
# (C) Space: O(1)
# 
# Optimize:
# - hashmap, to store items (keys) and indices (value)
# - iterate through nums, for each i, we check if the difference between target and i is already seen
# - if that is the case, we return [differenceIndex, currIndex]
# - if that is NOT the case, we add the current item with index to our seen hashmap
# (C) Time: O(n)
# (C) Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, item in enumerate(nums):
            if (target - item) in seen:
                return [seen[target - item], i]
            seen[item] = i
        return []
        

# if __name__ == "__main__":
#     solver = Solution()

#     assert solver.twoSum([3,4,5,6], 7) == [0,1], "Failed standard case"

#     assert solver.twoSum([4,5,6], 10) == [0,2], "Failed non-neighbouring case"

#     assert solver.twoSum([5,5], 10) == [0,1], "Failed similar item, different index case"

#     assert solver.twoSum([5,10,2], 200) == [], "Failed no-solution existing case"

