public class Solution {
    public int maxProfit(int[] prices) {
        int i = 0;
        int profit = 0;
        while(true){
            if(i + j == prices.length)
            break;
            int j = 0;
            if(prices[i+1] < prices[i]){
                i++;
                continue;
            }
            else{
                while(j < prices.length - i){
                    if(prices[i + j] < prices[i + j - 1]){
                        if(prices[i + j - 1] - prices[i] > profit)
                            profit = prices[i + j - 1] - prices[i];
                        i += j;
                        break;
                    }
                    j++;
                    if(i + j == prices.length){
                        if(prices[i + j - 1] - prices[i] > profit)
                            profit = prices[i + j - 1] - prices[i];
                    }
                }
            }
            }
        return profit;
        }
    }
