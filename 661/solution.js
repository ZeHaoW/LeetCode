/**
 * @param {number[][]} M
 * @return {number[][]}
 */
var imageSmoother = function(M) {
    var A = M;
    var rowindex = 0;
    var colindex = 0;
    var sum = 0;
    var count = 0;
    for(var row of M){
        for(var j of row){
            if(rowindex-1 < 0 && colindex-1 < 0){
                sum = M[rowindex][colindex] + M[rowindex][colindex + 1] + M[rowindex+1][colindex] + M[rowindex+1][colindex+1];
                count = 4;
            }
            else if (rowindex-1 < 0){
                sum = M[rowindex][colindex] + M[rowindex + 1][colindex] + M[rowindex][colindex + 1] + M[rowindex+1][colindex+1] + M[rowindex][colindex-1] + M[rowindex+1][colindex-1];
                count = 6;
            }
            else if (colindex-1 < 0){
                sum = M[rowindex][colindex] + M[rowindex][colindex + 1] + M[rowindex+1][colindex] + M[rowindex+1][colindex+1] + M[rowindex-1][colindex] + M[rowindex-1][colindex+1];
                count = 6;
            }
            else{
                sum = M[rowindex][colindex] + M[rowindex][colindex + 1] + M[rowindex][colindex-1] + M[rowindex+1][colindex] + M[rowindex+1][colindex+1] + M[rowindex+1][colindex-1] + M[rowindex-1][colindex] + M[rowindex-1][colindex+1] + M[rowindex-1][colindex-1];
                count = 9;
            }
            A[rowindex][colindex] = parseInt(sum/count);
            colindex++;
        }
        rowindex++;
        colindex = 0;
    }
    return A;
};

var M =  [[1,1,1],[1,0,1],[1,1,1]];
imageSmoother(M);
