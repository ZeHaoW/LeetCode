//法一，取余求解
class Solution {
    public void rotate(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++ ) {
        int m = (i + k) % nums.length;
        map.put(nums[i], m)
    }
    for(int j = 0; j < nums.length; j++){
        nums[j] = map.get(j);
    }
    }
}

//法二，翻转求解，思路很新颖

class Solution {
    public void rotate(int[] nums, int k) {
    k %= nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
}

public void reverse(int[] nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}
}
