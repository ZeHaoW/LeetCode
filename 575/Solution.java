class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> set= new HashSet();
        int sum = candies.length/2;
        for(int i : candies){
            set.add(i);
        }
        if(set.size() >= sum)
            return sum;
        else
            return set.size();
    }
}
