class Solution {
    //Goal:
    // - return indices i and j where i != j, such that nums[i] + nums[j] == target

    //Initial plan (bruteforce):
    // - 2 pointers, left and right
    // - For every left pointer, 
    // - - move right pointer to the end of the arr till target addition is reached

    //Complexities:
    // - Space: O(1)
    // - Time: O(n^2)
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[i] + nums[j] == target) return new int[]{i, j};
            }
        }

        return new int[]{};
    }
}
