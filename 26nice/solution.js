/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var id = 1;
    for(var i = 1; i < nums.length; i++){
      if(nums[i] != nums[i-1]){
        nums[id++] = nums[i];
      }
    }
    return id;
};
