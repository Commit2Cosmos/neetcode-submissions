class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_first(left, right):
            mid = (left + right + 1) // 2

            if left >= right:
                return left

            if matrix[mid][0] > target:
                return binary_first(left, mid-1)
            else:
                return binary_first(mid, right) 

        row_idx = binary_first(0, len(matrix)-1)

        def binary_row(left, right):
            mid = (left + right + 1) // 2

            if left >= right:
                if matrix[row_idx][left] == target:
                    return True
                return False

            if matrix[row_idx][mid] > target:
                return binary_row(left, mid-1)
            else:
                return binary_row(mid, right)

        print(row_idx)
        return binary_row(0, len(matrix[0])-1)