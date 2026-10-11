# Inputs: nums: List[int], target: int
# Goal: given an array of distinct integers nums, return the index of target, else return -1
#
# Constraints:
# - nums only has DISTINCT integers (dont have to worry about multiple occurences of target)
# - in ascending order, can make use of binary search
# - algo MUST run in O(logn)
# - nums length is between 1 and 10000
#
# Question:
# - 0 indexed array? -> yes
# 
# Scenarios:
# - inp: [-1], target = 3
# - out: -1
#
# - inp: [2,3,4,6,7,8], target = 6
# - out: 3
#
# - inp: [1,2,3,5,88,99,100], target = 100
# - out: 6
#
# Initial plan:
# - binary search
# - compare target with element in middle of the array, if our target is smaller, we only check the left part to our current element, else only the right part
# - we repeat this process until the element we are currently at is equal to target, else we return -1 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            curr = (left + right) // 2
            if (nums[curr] == target):
                return curr
            elif (target < nums[curr]):
                right = curr - 1
            else: # target > nums[curr]
                left = curr + 1

        return -1
        