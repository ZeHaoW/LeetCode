/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
 //超时答案
var containsNearbyDuplicate = function(nums, k) {
  for(var i = 0; i < nums.length; i++){
    for(var j = i + 1; j <= i + k; j++){
      if(nums[i] != nums[j])
        continue;
      else
        return true;
    }
  }
  return false;
};

//java with set,15ms
class Solution{
  public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
          if(i > k)
            set.remove(nums[i - k -1]);
          if(!set.add(nums[i]))
            return true;
        }
        return false;
    }
}

//javascript with set,128ms
var containsNearbyDuplicate = function(nums, k) {
  var set = new Set();
  for(var i = 0; i < nums.length; i++){
    if(i > k)
      set.delete(nums[i-k-1]);
    if(set.has(nums[i]))
      return true;
    else
      set.add(nums[i]);
  }
  return false;
}
