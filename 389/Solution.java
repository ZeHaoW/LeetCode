class Solution {
    public char findTheDifference(String s, String t) {
        StringBuffer sb = new StringBuffer();
        sb.append(s);
        sb.append(t);
        int result = 0;
        for(int i = 0; i < sb.length(); i++){
            result ^= (int)sb.charAt(i);
        }
        return (char)result;
    }
}
