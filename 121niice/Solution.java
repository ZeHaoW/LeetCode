public class Solution {
    public int maxProfit(int[] prices) {
        int max_ending_here, max_so_far;
        max_ending_here = max_so_far =0;
        for(int n = 1; n < prices.length; n++){
            max_ending_here = Math.max(max_ending_here + prices[n] - prices[n-1], prices[n] - prices[n-1]);
            max_so_far = Math.max(max_ending_here, max_so_far);
        }
        return max_so_far;
        }
    }
