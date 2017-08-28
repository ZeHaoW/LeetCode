class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> map = new HashMap();
        List<String> res = new ArrayList();
        for(int i = 0; i < list1.length; i++){
            map.put(list1[i], i);
        }
        int minsum = Integer.MAX_VALUE;
        for(int j = 0; j < list2.length; j++){
            Integer k = map.get(list2[j]);
            if(k != null && k + j <= minsum){
            if(k + j < minsum){res = new ArrayList(); minsum = k + j; }
            res.add(list2[j]);
            }
        }
        return res.toArray(new String[0]);
    }
}
