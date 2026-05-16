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

    //Optimization:
    //- Sort nums[]
    //- initialise new result Arraylist
    //- use 3 pointers, 1st pointer b fixed during each iteration
    //- left pointer l at b + 1
    //- right pointer r at nums.length - 1

    //- if nums[b] > 0, break and return empty list
    //- if b pointer > 0 AND nums[b] == nums[b - 1] (duplicate value) -> skip it (continue)
    //- while l < r:
    //- - move l and r forward and backward according to the sum of the entries
    //- - if sum == 0, make new list and add them to res array

    //New Complexities:
    //Time: O(n^2)
    //Space: O(1) (+ sorting algo space)

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int b = 0; b < nums.length; b++){

            if (nums[b] > 0) break;
            if (b > 0 && nums[b] == nums[b - 1]) continue;

            int l = b+1, r = nums.length - 1;
            while (l < r){
                int sum = nums[b] + nums[l] + nums[r];

                if (sum > 0) {
                    r--;
                }
                else if (sum < 0) {
                    l++;
                }
                else {
                    res.add(List.of(nums[b], nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]){
                        l++;
                    }
                }
            }
        }

        return res;
    }
}
