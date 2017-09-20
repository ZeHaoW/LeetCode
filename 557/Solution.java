class Solution {
    public String reverseWords(String s) {
 		String[] arr = s.split(" ");
 		StringBuilder result = new StringBuilder();
 		for(String t : arr){
 			t = new StringBuilder(t);
 			t.reverse().toString();
 			result.append(t + " ");
 		}
 		return result.toString().trim();
    }
}