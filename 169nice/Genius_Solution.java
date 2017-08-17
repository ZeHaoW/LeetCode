public class Genius_Solution{
    public int majorityElement(int nums[]){
        int majority = nums[0];
        int count = 1;
        for(int j = 0; j < nums.length; j++){
            if(count == 0){
                majority = nums[j];
                count = 1;
            }
            else if(majority == nums[j])
                count++;
            else
                count--
        }
        return majority;
    }
}
