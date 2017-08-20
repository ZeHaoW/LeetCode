/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var temp = 0;
    for(let k of nums) if(k !== val) nums[temp++] = k;
    return temp;
};
