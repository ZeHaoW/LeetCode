/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for(var i = digits.length - 1; i >= 0; i--){
        if(digits[i] < 9){
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    var nums = new Array(digits.length + 1);
    nums[0] = 1;
    for(var j = 1; j < nums.length; j++){
        nums[j] = 0;
    }
    return nums;
};
