# Goal: encode list of strings to str and decode the other way around
# 
# Questions: 
# - input validation? -> yes
# - strings inside list of strings -> valid ascii characters? -> yes
# 
# Initial plan:
# - encode: loop over stringList, concatenate all of the strings with a separator "-"
# - decode: split the input string based on separator
# - Time encode: O(n)
# - Space encode: O(n)
# - Time decode: O(n)
# - Space decode: O(s), s = half of the length of encodedstring

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "emptyArr"
        # a-b-c-d
        return "+".join(string for string in strs)

    def decode(self, s: str) -> List[str]:
        if s == "emptyArr":
            return []
        return s.split("+")
