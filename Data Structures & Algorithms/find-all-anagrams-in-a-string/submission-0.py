# Goal: return the start index of every substring of s that is an anagram of p
# Inputs: s: str, p: str
# 
# Constraints:
# - length of p and s is within 1 and 30000
#       no empty strings
#       no memory overflow
# - only lowercase english letters
#
# Questions:
# - Does the output order of indices matter? -> no
# - If there is no anagram of p inside s, what should be returned? -> empty string
#
# Scenarios / edge-cases:
# - pattern longer than string
# - single char s and p && match
# - single char s and p && no-match
# - multi char s and single char p (all match)
# - multi char s and single char p (no match)
# - indices are at start/end of s

# Optimized plan:
# - Handle edge case: if len(s) < len(p), return an empty list immediately
# - Use two fixed 26-slot frequency arrays: p_count and s_count to track character counts for 'a'-'z'
# - Populate p_count for string p, and s_count for the first window of s (from index 0 to len(p) - 1)
# - Compare s_count with p_count; if they match, record index 0 in the result list
# - Slide the window of length len(p) across the remainder of s (from right = len(p) to len(s) - 1):
#       - Increment the count of the incoming character at s[right]
#       - Decrement the count of the outgoing character at s[right - len(p)]
#       - If s_count == p_count, append the start index (right - len(p) + 1) to the result list
# - Return the result list
# (C) Time: O(N), where N = len(s) (O(1) update and comparison per shift)
# (C) Space: O(1) (fixed 26-element arrays)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)

        # if pattern is longer than str, return
        if (k > n):
            return []

        # freq arrays to keep track of chars in s and p
        p_count = [0] * 26
        s_count = [0] * 26

        # populate p and s arrays for initial window size k of string s
        for i in range(k):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        result = []

        # if initial window produced matching anagram substr, add 0 (left) to resultlist
        if s_count == p_count:
            result.append(0)

        # slide window of size k, one char at a time across the rest of s
        # add the freq of incoming char from right, remove leaving freq of char on left
        for right in range(k, n):
            s_count[ord(s[right]) - ord('a')] += 1
            s_count[ord(s[right - k]) - ord('a')] -= 1

            # curr window starts at: right -k + 1
            if s_count == p_count:
                result.append(right - k + 1)
        
        return result

# if __name__ == "__main__":
#     sol = Solution()

#     # normal multiple anagrams case
#     assert sol.findAnagrams("cbaebabacd", "abc") == [0,6], "Failed on normal multi anagram case" 
#     # overlapping anagrams
#     assert sol.findAnagrams("abab", "ab") == [0,1,2], "Failed on overlapping anagrams"
#     # exact match (len(s) == len(p)) 
#     assert sol.findAnagrams("bca", "abc") == [0], "Failed on exact len match"
#     # pattern longer than s string 
#     assert sol.findAnagrams("b", "abc") == [], "Failed on pattern longer than s string case" 
#     # no match 
#     assert sol.findAnagrams("hello", "world") == [], "Failed on no match case" 



        

