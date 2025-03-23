class Solution {
  public static int maxProfit(int[] prices) {
      int min = Integer.MAX_VALUE;
      int result = 0;

      for (int i = 1; i < prices.length; i++){
          // 더 작은 값이 있으면 갱신 
          if (min > prices[i-1]){
              min = prices[i-1];
          }
          
          result = Math.max(result, prices[i] - min);
      }

      return result;
  }
}