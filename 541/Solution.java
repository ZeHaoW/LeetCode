class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder str = new StringBuilder(s);
        if(s.length() < k) return str.reverse().toString();
        for(int i = 0; i < s.length(); i=i+2*k){
        	if(i+k-1 > s.length() - 1) str = reverseSubStr(str, i, s.length());
        	else str = reverseSubStr(str, i, i+k);
        }
        return str.toString();
    }

    private StringBuilder reverseSubStr(StringBuilder str, int start, int end){
    	StringBuilder tem_str = new StringBuilder(str.substring(start, end));
    	return str.replace(start, end, tem_str.reverse().toString());
    }
}