class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target: number, position: number[], speed: number[]): number {
        let sorted_idx = position
            .map((_, i) => i)
            .sort((i, j) => position[i]-position[j]);

        let time_to_target = sorted_idx.map(i => (target - position[i])/speed[i]);

        let res = 0;
        let stack = [];

        for (let i = time_to_target.length-1; i >= 0; i--) {
            if (stack.length > 0 && time_to_target[i] > stack[stack.length-1]) {
                stack.pop();
            }

            if (stack.length == 0) {
                res += 1;
                stack.push(time_to_target[i])
            }
        }

        return res;
    }
}
