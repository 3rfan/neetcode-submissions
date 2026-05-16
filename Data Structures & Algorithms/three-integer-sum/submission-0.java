class Solution {
    //Goal:
    //- return distinct triplets [nums[i],nums[j],nums[k]] where their sum is 0
    //- - no duplicate triplets allowed 

    //Initial plan (bruteforce):
    //- Sort nums[] using Arrays.sort
    //- initialise result Set of List<Integer> entries to hold triplets
    //- loop over nums[] for i = 0, for j = i+1 and for k = j+1;
    //- - inside last loop for k:
    //- - - if nums[i] + nums[j] + nums[k] == 0, add to res
    //- return new ArrayList out of res set

    //Initial Complexities:
    //Space: O(n) (+ sorting space)
    //Time: O(n^3)

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            for (int j = i+1; j < nums.length; j++){
                for (int k = j+1; k < nums.length; k++){
                    if (nums[i] + nums[j] + nums[k] == 0){
                        res.add(List.of(nums[i], nums[j], nums[k]));
                    }
                }
            }
        }

        return new ArrayList<>(res);
    }
}
