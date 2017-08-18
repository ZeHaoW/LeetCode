class Solution {
    public int maxSubArray(int[] nums) {
        int m = nums[0];
        int n = nums[0];
        for(int i = 0; i < nums.length; i++){
            m = Math.max(nums[i], m + nums[i]);
            n = Math.max(m, n);
        }
        return n;
    }
}
