class Solution {
    // input: arr
    // type: int[]

    // Goal: check for duplicate values in arr
    // - return true if there are duplicates
    // - return false otherwise

    // initial plan:
    // - 2 pointers, keep moving right pointer till end for each left pointer
    // - - if the right pointer is equal to the left pointer, return true
    // - - else return false
    public boolean hasDuplicate(int[] nums) {
        for (int left = 0; left < nums.length - 1; left++){
            for (int right = left + 1; right < nums.length; right++){
                if (nums[left] == nums[right]){
                    return true;
                }
            }
        }

        return false;
    }
}