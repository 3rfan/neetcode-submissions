
/*
* goal: return true if a value returns more than once in array, else return false
* input: int[] nums
* 
* Initial plan:
* - make hashmap, keep track of numbers (key) and occurences (value)
* - iterate through nums, update hashmap with frequency of num
*/

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i: nums){
            if (map.containsKey(i)){
                return true;
            } else {
                map.put(i, 1);
            }
        }

        return false;
    }
}