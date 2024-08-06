class Solution {
    public int maxProduct(int[] nums) {
        int ans = -99999999;
        for(int i = 0; i < nums.length; i++){
            int prod = nums[i];
            if(prod > ans){
                ans = prod;
            }
            for(int j = i + 1; j < nums.length; j++){
                long x = prod;
                x = x * nums[j];
                if (x > 2147483647){
                    continue;
                }
                else{
                    prod = (int)x;
                }
                if(prod > ans){
                    ans = prod;
                }
            }
        }
        return ans;
    }
}