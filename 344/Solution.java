class Solution {
    public String reverseString(String s) {
        if(s == null) return null;
        char[] arr = s.toCharArray();
        for(int i = 0; i < s.length()/2; i++){
            arr[i] = s.charAt(s.length() - i -1);
            arr[s.length() - i -1] = s.charAt(i);
        }

        return new String(arr);
    }
}
