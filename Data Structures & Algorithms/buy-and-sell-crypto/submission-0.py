# Goal: return the maximum profit we can achieve by buying neetcoin on the ith day and selling it in some future day
# Input: array[int] where array[i] denotes the price of neetcoin on the ith day
#
# Questions: 
# - [5,5,5,5,5] -> 0 ? yes
# - is there any constraint on how many days in the future we can select up to? no
# - can list length just be 1? yes
#
# Initial plan:
# - current max = 0
# - loop over all value combinations
# - [10,1,5,3,7,1] 
#   1 - 10 = -9 -> is it bigger than max? yes? overwrite max
# - return current max
# Time: O(n*2)
# Space: O(1)
#
# Optimized plan:
# - current max = 0
# - use a sliding window, we go over the whole array and find the answer in a single pass
# - while (right < len(arr))
# - we do arithmetics with the values at the left and the right pointer
# - if prices[right] > prices[left]
#       if the subtraction is bigger than our curr max 
#           update current max to this value
# - else (prices[right] =< prices[left])
#       set left pointer to where right is, 
#
#   move right pointer forward   
#
# - return current max
# Time: O(n)
# Space: O(1)
#
# Why does this work? look at the case: [10,2,5,4,3,100,1,300,1000]
#
# - the only case where we would want to move our left pointer, is if the right pointer value is LOWER than our left pointer
# - if that is the case we should look ONLY at the possible combinations AFTER that new lowest value, there is no combination BEFORE that value that can make the current sum bigger
# - - - - try to visualise it you will understand 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        curr_max = 0

        while (right < len(prices)):
            if prices[right] > prices[left]:
                curr_max = max(curr_max, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return curr_max

if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit([5,5,5,5]) == 0, "Failed same value case"
    assert sol.maxProfit([10,8,5,4,3,2]) == 0, "Failed decreasing list case"
    assert sol.maxProfit([10,1,5,6,7,1]) == 6, "Failed standard example case"
    assert sol.maxProfit([100]) == 0, "Failed single value case"

    print("All tests pass")
        