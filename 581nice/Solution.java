class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int end = -2;
        int beg = -1;
        int max = nums[0];
        int min = nums[nums.length - 1];
        for(int i = 0; i < nums.length; i++){
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[nums.length-i-1]);
            if(nums[i] < max)
                end = i;
            if(nums[nums.length-i-1] > min)
                beg = nums.length-i-1;
        }
        return end - beg + 1;
    }
}
