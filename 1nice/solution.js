/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var arr = [];
    var res = new Array(2);
    for (var i = 0; i < nums.length; i++) {
        if(arr.indexOf(target - nums[i]) != -1){
            res[1] = i;
            res[0] = arr.indexOf(target - nums[i]);
            return res;
        }
        arr[i] = nums[i];
    }
    return res;
};
