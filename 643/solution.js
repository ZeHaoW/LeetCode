/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    var sum = 0;
    var max = 0;
    for(var i = 0; i < k; i++){
        sum += nums[i];
    }
    max = sum;
    for(var j = k; j < nums.length; j++){
        sum += nums[j] - nums[j-k];
        max = Math.max(sum, max);
    }
    return max/k;
};
