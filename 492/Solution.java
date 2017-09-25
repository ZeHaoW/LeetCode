public class Solution{
    public int[] constructRectangle(int area){
         int num = 0;
         int[] res = new int[2];
         int end = (int)Math.sqrt(area);
         for(int i = 1; i <= end; i++){
           if(area%i == 0 && area/i - i < num){
             num = area/i - i;
             res[0] = area/i;
             res[1] = i;
           }
         }
         return res;
    }
}
  
