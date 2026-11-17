# Goal: find the smallest amount of bananas we can eat k, such that we finish all of the bananas within h hours
# Input: piles[i], h 
#
# Questions/information:
# - len(piles[i]) 0 and 10,000
# - i between 1 and 10^9
#
# Initial plan:
# - bruteforce: 
#       - iterate through piles, 
#       - sum up amount of bananas, 
#       - starting from n=1 until m (m = highest value inside piles) divide totalSum by n
#       - as soon as we have an n <= h, we return n
# - Time: O(n*m), n = length of piles, m = max value of piles item
# - Space: O(k), k = size of largest possible totalSum 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return 1
        