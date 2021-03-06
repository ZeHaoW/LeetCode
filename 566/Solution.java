public class Solution{
    public int[][] matrixReshape(int[][] nums, int r, int c){
        int[][] res = new int[r][c];
        if(r*c != nums.length*nums[0].length){
            return nums;
        }
        else{
            for(int i = 0; i < r*c; i++){
                res[i/c][i%c] = nums[i/nums[0].length][i%nums[0].length];
            }
        }
        return res;
}
}
