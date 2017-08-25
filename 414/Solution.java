class Solution {
    public int thirdMax(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 1; i < 4; i++){
            map.put(i, -1);
        }
        for(int i : nums){
            if(i > map.get(1)){
                map.put(3, map.get(2));
                map.put(2, map.get(1));
                map.put(1, i);
            }
            else if(i > map.get(2) && i != map.get(1)){
                map.put(3, map.get(2));
                map.put(2, i);
            }
            else if(i > map.get(3) && i != map.get(2)){
                map.put(3, i);
            }
        }
        return (map.get(2) == -1) ? map.get(1) : (map.get(3) == -1) ? map.get(2) : map.get(3);
    }
}
