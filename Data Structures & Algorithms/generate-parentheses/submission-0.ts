class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n: number): string[] {
        const res = [];

        function recur(right: number, left: number, curr: string) {
            if (curr.length == n*2) {
                res.push(curr);
                return;
            }

            if (left > 0) {
                recur(right, left-1, curr+"(");
            }
            if (right > 0 && left<right) {
                recur(right-1, left, curr+")");
            }
        }

        recur(n, n, "");

        return res;
    }
}
