public class Solution {
    public int[] twoSum(int[] numbers, int target) {
                int index1 = 1,index2 = numbers.length;
        for(int i = numbers.length - 1; numbers[i] > target; i--) {
        		index2--;
        }
        while(numbers[index1-1] + numbers[index2-1] != target) {
        	if(numbers[index1-1] + numbers[index2-1] < target) {
        		index1++;
        	}
        	else {
        		index2--;
        	}
        }
        if(index1 > index2){
            int tmp = index1;
            index1 = index2;
            index2 = tmp;
        }
        		int[] list = {index1, index2};
        		return list;
    }
}