class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet();
        return fun(n, set);
    }

    private boolean fun(int n, Set<Integer> set){
        int len = 0;            
        int res = 0;
        String s = "" + n;
        for(int i = 0; i < s.length(); i++){
        res += (s.charAt(i) - '0') * (s.charAt(i) - '0');
        }
        if(res == 1)
            return true;
        else{
            len = set.size();
            set.add(res);
            if(set.size() == len)
                return false;
            else
                return fun(res, set);
        }
    }
}