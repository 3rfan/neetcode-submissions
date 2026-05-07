class Solution {
    public void rotate(int[] nums, int k) {
        int times = k % nums.length;

        reverse(nums,0,nums.length-1);
        reverse(nums,0,times -1);
        reverse(nums,times,nums.length -1);
    }

    public void reverse(int[] nums, int start, int end){
        while (start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;

            start++;
            end--;
        }
    }
}