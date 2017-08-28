class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap();
        for(int i : num1){
            map.put(i, 0);
        }
        List<Integer> list = new ArrayList();
        for(int i : num2){
            if(map.containsKey(i)){
                list.add(i);
                map.remove(i);
            }
            else
                continue;
        }
        int[] arr = list.toArray(new int[0]);
        return arr;
    }
}
