class Solution {
    // input: arr
    // type: int[]

    // Goal: check for duplicate values in arr
    // - return true if there are duplicates
    // - return false otherwise

    // initial plan (bruteforce):
    // - 2 pointers, keep moving right pointer till end for each left pointer
    // - - if the right pointer is equal to the left pointer, return true
    // - - else return false
    // time: O(n^2), space: O(1)

    // Optimize:
    // - use a Set (hashset)
    // - iterate through arr
    // - - if the value at i is in the set, return true
    // - - else add value to set
    // - if values not alr in set, return false

    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums){
            if (set.contains(i)){
                return true;
            } else {
                set.add(i);
            }
        }

        return false;
    }

    // initial plan
    // public boolean hasDuplicate(int[] nums) {
    //     for (int left = 0; left < nums.length - 1; left++){
    //         for (int right = left + 1; right < nums.length; right++){
    //             if (nums[left] == nums[right]){
    //                 return true;
    //             }
    //         }
    //     }

    //     return false;
    // }
}