public class Solution {
    public int majorityElement(int[] nums) {
    int left = 0;
    int right = nums.length/2;
    int j = 0;
    Arrays.sort(nums);
    for(int i = 0; i <= nums.length/2; i++){
        for(j = left + i; j < right + i; j++){
            if(nums[j+1] != nums[j])
                break;
        }
        if(j == right + i)
            break;
    }
    return  nums[j];
    }
}
