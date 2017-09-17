class Solution{
	public int findComplement(int num){
		num = ~num;
		int mask = Integer.highestOneBit(num) - 1;
		return num & mask;
	}
}