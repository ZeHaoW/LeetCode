/**
 * @param {number} rowIndex
 * @return {number[]}
 */
 //笨方法
var getRow = function(rowIndex) {
    var nums = [];
    if(rowIndex === 0){
      nums = [1];
      return nums;
    }
    else if (rowIndex === 1) {
      nums = [1,1];
      return nums
    }
    else{
      nums = [1,1]
      for(var i = 2; i < rowIndex; i++){
        for(var j = i - 1; j > 0; j--){
          nums[j] += nums[j-1];
        }
        nums[0] = 1;
        nums[i] = 1;
      }
      return nums;
    }
};

//优化版
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    var nums = [1];
      for(var i = 1; i <= rowIndex; i++){
        for(var j = i - 1; j > 0; j--){
          nums[j] += nums[j-1];
        }
                nums[i] = 1;
      }

      return nums;
};
