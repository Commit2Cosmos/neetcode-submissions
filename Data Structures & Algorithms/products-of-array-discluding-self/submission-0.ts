class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const left_product: number[] = [nums[0]];

        for (let i = 1; i < nums.length; i++) {
            left_product[i] = nums[i] * left_product[i-1];
        }

        const right_product: number[] = new Array(nums.length);
        right_product[right_product.length-1] = nums[nums.length-1]
        for (let i = nums.length-2; i >= 0; i--) {
            right_product[i] = nums[i] * right_product[i+1];
        }

        const res: number[] = new Array(nums.length).fill(1);
        for (let i = 0; i < nums.length; i++) {
            if (i != 0) {
                res[i] *= left_product[i-1]
            }
            if (i != nums.length-1) {
                res[i] *= right_product[i+1]
            }
        }

        return res
    }
}
