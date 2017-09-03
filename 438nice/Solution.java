class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList();
        int[] arr = new int[256];
        int count = p.length();
        int left = 0;
        int right = 0;
        for(int i = 0; i < p.length(); i++){
            arr[p.charAt(i)]++;
        }
        while(right < s.length()){
            if(arr[s.charAt(right++)]-- > 0)
                count--;
            if(count == 0)
                list.add(left);
            if(right - left == p.length() && arr[s.charAt(left++)]++ >= 0)
                count++;
        }
        return list;
    }
}