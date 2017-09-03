class Solution {
    public boolean wordPattern(String pattern, String str) {
        Map<Character, String> map = new HashMap();
        Set<String> set = new HashSet();
        String[] arr = str.split(" ");
        if(pattern.length() != arr.length)
            return false;
        for(int i = 0; i < pattern.length(); i++){
            if(map.containsKey(pattern.charAt(i))){
                if(map.get(pattern.charAt(i)) == arr[i])
                    continue;
                else
                    return false;
            }
            if(!map.containsKey(pattern.charAt(i)))
                map.put(pattern.charAt(i), arr[i]);
        }
        for(Map.Entry<Character, String> me : map.entrySet()){
            if(set.add(me.getValue()))
                continue;
            return false;
        }
        return true;
    }
}System.out.println()