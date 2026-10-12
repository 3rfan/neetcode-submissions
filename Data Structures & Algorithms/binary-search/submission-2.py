class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            # take left, add HALF of the distance between left and right (finds true midpoint)
            curr = left + (right - left) // 2
            if (nums[curr] == target):
                return curr
            elif (target < nums[curr]):
                right = curr - 1
            else:
                left = curr + 1
                
        return -1