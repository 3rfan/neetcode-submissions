
class Solution {
    //Goal:
    // - return indices i and j where i != j, such that nums[i] + nums[j] == target

    //Initial plan (bruteforce):
    // - 2 pointers, left and right
    // - For every left pointer, 
    // - - move right pointer to the end of the arr till target addition is reached

    //Initial complexities:
    // - Space: O(1)
    // - Time: O(n^2)

    //Optimalization:
    // - we use a hashmap (value : index), we iterate once over array
    // - - we evaluate the diff of {target - nums[i]} 
    // - - we check if that diff is in the hashmap
    // - - - if it is -> return hashmap val + current i
    // - - - if not -> put index + curr val in hashmap
    // - - if not present in hashmap, return new mepty int arr

    //Optimized complexities:
    // - Space: O(n)
    // - Time: O(n)
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            if (map.containsKey(diff)){
                return new int[]{map.get(diff),i};
            }

            map.put(nums[i], i);
        }

        return new int[0];
    }
}
