class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];

        int first;
        int second;

        for (int i = 0; i < nums.length - 1; i++){
            first = i;
            for (int j = i+1; j < nums.length; j++){
                second = j;
                if (nums[first] + nums[second] == target){
                    res[0] = first;
                    res[1] = second;
                    return res;
                }
            }
        }

        return res;
    }
}
