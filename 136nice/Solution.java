//利用异或，相同为0，相异为1，且满足交换律
class Solution {
    public int singleNumber(int[] nums) {
        int result = nums[0];
        for(int i : nums){
            result = result ^ i;
        }
        return result;
    }
}
