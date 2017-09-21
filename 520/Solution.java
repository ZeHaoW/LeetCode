class Solution {
    public boolean detectCapitalUse(String word) {
    	if(word == null) return false;
    	if(word.length() == 1) return true;
        if(word.charAt(0) >= 'A' && word.charAt(0) <= 'Z' && word.charAt(1) >= 'A' && word.charAt(1) <= 'Z'){
        	for(int n = 1; n < word.length(); n++){
        		if(word.charAt(n) >= 'a' && word.charAt(n) <= 'z') return false;
        	}
        	return true;
        }
         else if(word.charAt(0) >= 'A' && word.charAt(0) <= 'Z' && word.charAt(1) >= 'a' && word.charAt(1) <= 'z'){
        	for(int n = 1; n < word.length(); n++){
        		if(word.charAt(n) >= 'A' && word.charAt(n) <= 'Z') return false;
        	}
        	return true;
        }
         else{
        	for(int n = 1; n < word.length(); n++){
        		if(word.charAt(n) >= 'A' && word.charAt(n) <= 'Z') return false;
        	}
        	return true;
        }
    }
}

//正则表达式法
class Solution{
    public boolean detectCapitalUse(String word) {
    	return word.matches("[A-Z]+|[a-z]+|[A-Z][a-z]+");
}