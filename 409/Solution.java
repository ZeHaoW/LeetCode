class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> map = new HashMap();
        char[] arr = s.toCharArray();
        int len = 0;
        int flag = 0;
        for(char i : arr){
          if(map.containsKey(i)) map.get(i)++;
          else map.put(i, 1);
        }
         for(Map.Entry me : map.entrySet()) {
           if(me.getValue() % 2 == 0)
              len += me.getValue();
          else{
              len += me.getValue() - 1;
              flag = 1;
          }
         }
        if (flag == 1)
            len++;
        return len;
    }
}
