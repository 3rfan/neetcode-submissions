# Goal: make a data structure, that holds values for keys at particular timestamps
# Inputs: 
# - initilizing the datastructure
# - set values for keys at timestamps
# - getting values for given keys and timestamps
#
# Questions:
# - timestamps negative? -> No 
# - timestamps always increasing -> Yes
# - concurrent timestamp operations? -> Yes
# - - ensure the last call is the performed one
# - do we always perform data operation before returned the stored value? -> Yes
# - are get calls always made to valid existing keys and timestamps? -> No
# - - ensure keys/timestamps exist for get calls
# - what can timestamp be 0 - 10^7
# - are the get calls made in increasing timestamp order? -> false, we can add key, value for a timestamp in the future and call for a key, timestamp in the past
# 
# Initial plan (bruteforce):
# - create a hashmap, with (key, timestamp) as its key, as its value we just have the given value
# 
# Better plan:
# - create a hashmap, with given key as its key, and as values we would have a stack of (timestamp, value) tuples
# - to account for no values: either check for (timestamp, value) existence, given the key
# - perform binary search to find value given a time-stamp
# - get Time: O(logN)
# - set Time: O(1) (Amortized list appending)
# - Space: O(n) for the class as a whole


class TimeMap:

    def __init__(self):
        self.map: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # check if key is inside our map
        if key not in self.map:
            return ""
        
        entries = self.map[key]
        left = 0
        right = len(entries) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2
            entry_timestamp, entry_value = entries[middle]

            if entry_timestamp <= timestamp:
                result = entry_value
                left = middle + 1
            else:
                right = middle - 1
        
        return result
            
            
        
