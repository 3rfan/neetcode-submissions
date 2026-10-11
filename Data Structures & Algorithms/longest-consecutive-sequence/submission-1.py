# Inputs: nums: List[int]
# Goal: return the len of the longest consecutive sequence of elements that can be formed. Conseq sequence = each element after in the sequence is EXACTLY 1 bigger than the one before it.
#
# Constraints:
# - algo MUST run in O(n) time
# - elements are counted only ONCE (so 2,2,2 is not 3, just 1)
# - nums is between 0 and 100,000 elements long
# 
# Scenarios:
# - inp: []
# - out: 0
# 
# - inp: [1,2]
# - out: 2
#
# - inp: [2,1]
# - out: 2
# 
# - inp: [3,2,4,5,784,10,15,13,11,12,14]
# - out: 6 NOT 4
#
# Inital plan:
# - iterate over nums, put each item in a hashset, 
# - how to identify start of seq: iterate again over nums, for each item i, check if i - 1 is NOT present in hashset, if that is the case, we have found start of a sequence
# - for each start of sequence ss, we can check if ss + 1 is inside hashset, and keep checking as long as ss + 1 is inside hashset
# - keep track of a global max and for each start of a sequence, check if we can find a sequence larger than current global max
# (C) Time: O(2n) = O(n)
# (C) Space: O(n) for the hashset

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # global longest streak
        longest_streak = 0
        # hashset
        nums_set = set(nums)
        # iterate over nums, find start of sequence
        for num in nums:
            # start of sequence
            if num - 1 not in nums_set:
                curr = num
                curr_streak = 1
                # check streak for this ss
                while curr + 1 in nums_set:
                    curr_streak += 1
                    curr += 1
                if (curr_streak > longest_streak):
                    longest_streak = curr_streak

        return longest_streak

# if __name__ == "__main__":
#     sol = Solution()

#     assert sol.longestConsecutive([]) == 0, "Failed empty list case"
#     assert sol.longestConsecutive([1,2]) == 2, "Failed 2 items consequtive case"
#     assert sol.longestConsecutive([2,1]) == 2, "Failed 2 items non-consequtive case"
#     assert sol.longestConsecutive([5]) == 1, "Failed single item case"
#     assert sol.longestConsecutive([3,2,4,5,784,10,15,13,11,12,14]) == 6, "Failed longer sequence later in list case"
        