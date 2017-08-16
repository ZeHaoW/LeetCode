public class Solution {
    public void moveZeroes(int[] nums) {
         for(int i = 0; i < nums.length; i++){
             if(nums[i]==0 || (nums[i]!=0 && (i-1 < 0 || nums[i-1]!=0))){
                 continue;
             }
             else{
                 for(int k = i-2;; k--){
                     if(k < 0 || nums[k] != 0){
                         nums[k+1] = nums[i];
                         nums[i] = 0;
                         break;
                     }
                 }
             }
         }
    }
}
