//只用计算每个格子下面的和右面的是否为1即可
class Solution {
    public int islandPerimeter(int[][] grid) {
        int width = grid[0].length;
        int height = grid.length;
        int island = 0;
        int neighbor = 0;
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                if(grid[i][j] == 1){
                    island++
                    if(i < height - 1 && grid[i + 1][j] == 1) neighbor++;
                    if(j < width - 1 && grid[i][j + 1] == 1) neighbor++;
                }
            }
        }
        return island*4 - neighbor*2
    }
}
