public class Solution{
  public List<Integer> findDisappearedNumbers(int[] nums) {
    List<Integer> new_num = new ArrayList<Integer>();
    for(int i = 0; i < nums.length; i++){
      if(nums[Math.abs(nums[i]) - 1] > 0)
      nums[Math.abs(nums[i]) - 1] = -nums[Math.abs(nums[i]) - 1];
    }
    for(int j = 0; j < nums.length; j++){
      if(nums[j] > 0){
        new_num.add(j+1);
      }
    }
        return new_num;
   }
}
