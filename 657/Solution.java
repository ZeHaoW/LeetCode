class Solution {
    public boolean judgeCircle(String moves) {
    	int horizon = 0;
    	int vertical = 0;
        for(int i = 0; i < moves.length(); i++){
        	if(moves.charAt(i) == 'L') horizon++;
        	if(moves.charAt(i) == 'R') horizon--;
        	if(moves.charAt(i) == 'U') vertical++;
        	if(moves.charAt(i) == 'D') vertical--;
        }
        if(horizon == 0 && vertical == 0) return true;
        else return false;
    }
}