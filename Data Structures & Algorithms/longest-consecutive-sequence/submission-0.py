# Inputs: nums: List[int]
# Goal: return length of longest consecutive sequece of els
#   which means each el is EXACTLY 1 greater than the previous el
#
# Constraints:
# - We need an algo that runs in O(n) time
# - length of nums is between 0 and 100,000
# - num[i] are between -10^9 and 10^9
# 
# Questions:
# - is it possible that there is no solution, so no sequence? -> yes
#
# Scenarios:
# inp: [2,20,3,4,5,6,32]
# out: 5 (2,3,4,5,6)
#
# inp: []
# out: 0
#
# inp: [5,42,1,3,432,3,2]
# out: 4 (1,2,3,5)
#
# Initial plan: 
# - instantiate max with 0
# - put nums into a hashset
# - iterate over the nums, if num-1 is NOT in hashset (this is a start of a sequence), we count from this num onward to see how long of a sequence with this starting num is present in hashset
# - compare with global max, return max

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in num_set:
                curr = num
                curr_streak = 1

                while curr + 1 in num_set:
                    curr_streak += 1
                    curr += 1

                longest_streak = max(curr_streak, longest_streak)

        return longest_streak
        
# if __name__ == "__main__":
#     sol = Solution()

#     assert sol.longestconsecutive([]) == 0, "failed empty list case"
#     assert sol.longestconsecutive([5,42,1,3,432,3,2]) == 4, "failed non consecutive in original array case"
#     assert sol.longestconsecutive([2,20,3,4,5,6,32]) == 5, "failed general case"