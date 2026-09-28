class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {

        let left: number = 0; 
        let right: number = nums.length-1;
        let res = -1;

        // console.log(curr);

        while (left <= right) {
            console.log(`${left} -- ${right}`);
            let curr: number = Math.floor((left + right + 1)/2);
            console.log(`Curr: ${curr}`);
            
            if (nums[curr] == target) {
                return curr
            }

            if (nums[left] < nums[curr]) {
                if (nums[left] <= target && target < nums[curr]) {
                    right = curr-1;
                } else {
                    left = curr+1;
                }
            } else {
                if (nums[curr] < target && target <= nums[right]) {
                    left = curr+1;
                } else {
                    right = curr-1;
                }
            }
        }

        return -1;
    }
}
