class Solution {
    public int findLHS(int[] nums) {
        Map<Integer> map = new HashMap();
        int max = 0;
        for(int i : nums){
            map.put(i, map.getOrDefault(i, 0) + 1);
        } 
        for(Map.Entry<Integer, Integer> me : map.entrySet()){
            if(map.containsKey(me.getKey() + 1)){
                int count = me.getValue() + map.get(me.getKey() + 1);
                max = Math.max(count, max);
            }
        }
        return max;
    }
}