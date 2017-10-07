class Solution {
    public String[] findRelativeRanks(int[] nums) {
    	int[][] arr = new int[nums.length][2];
    	String[] res = new String[nums.length];
    	for(int i = 0; i < nums.length; i++){
    		arr[i][0] = nums[i];
    		arr[i][1] = i;
    	}
    	Arrays.sort(arr, (a, b) -> (b[0]-a[0]));
    	for(int j = 0; j < nums.length; j++){
    		if(j == 0) res[arr[j][1]] = "Gold Medal";
    		else if(j == 1) res[arr[j][1]] = "Silver Medal";
    		else if(j == 2) res[arr[j][1]] = "Bronze Medal";
    		else res[arr[j][1]] = j + 1 + "";
    	}
    	return res;
    }
}