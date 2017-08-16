public class Solution {
    public int maxProfit(int[] prices) {
        int cnt = 0;
      int profit = 0;
        for(int i = 1; i < prices.length; i++){
          if(prices[i] < prices[i-1]){
            profit += prices[i-1] - prices[i-1-cnt];
            cnt = 0;
          }
          else{
            cnt++;
          }
          while(i == prices.length - 1) {
        	  profit += prices[i] - prices[i-cnt];
              break;
          }
        }
        return profit;
    }
}
//while中要加break才能跳出循环