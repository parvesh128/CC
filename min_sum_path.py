import sys

def minPathIter(mat):

	row, col = len(mat), len(mat[0])

	cost = [[0] * col for r in range(row)]


	for r in range(row):
		for c in range(col):
			if r == 0 and c == 0:
				cost[r][c] = mat[r][c]
			elif r == 0:
				cost[r][c] = cost[r][c - 1] + mat[r][c]
			elif c == 0:
				cost[r][c] = cost[r - 1][c] + mat[r][c]
			else:
				cost[r][c] = mat[r][c] + min(cost[r-1][c], cost[r][c-1])

	return cost[row-1][col-1]

def minPathRecur(mat):
	row, col = len(mat), len(mat[0])

	return minPathRecurImpl(mat, row, col, 0, 0)


def minPathRecurImpl(mat, rows, cols, r, c):

	if r == rows -1 and c == cols -1:
		return mat[r][c]

	right_path_len = sys.maxint
	if c + 1 < cols:
		right_path_len = minPathRecurImpl(mat, rows, cols, r, c + 1)

	down_path_len = sys.maxint
	if r + 1 < rows:
		down_path_len =  minPathRecurImpl(mat, rows, cols, r + 1, c)

	return mat[r][c] + min(right_path_len, down_path_len)






mat = [[4, 5, 6], [1, 2, 3], [0, 1, 2]]

print minPathRecur(mat)



