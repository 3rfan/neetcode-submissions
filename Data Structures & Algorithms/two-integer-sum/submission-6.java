/*
* Inputs: int[] nums, int target
* Goal: return int[] containing indice i and j such that nums[i] + nums[j] == target
* 
* Constraints: 
* - nums[] is not that long and contains at least 2 elements
* - only 1 valid answer 
* - integers inside nums are within -10mil and +10mil so is the target
* - every input has an answer
* - output small index first
* 
* Questions: 
* - 
* 
* Initial plan:
* - brute-force solution: for every index i, check all other index combinations, return [i, j] where j is one of the other inputs and NOT equal to i
*
* Initial complexities:
* - time: O(n^2)
* - space: O(1)
*
* Optimization:
* - 
*/

class Solution {
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
