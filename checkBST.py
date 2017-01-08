import sys
class TreeNode:

	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None


	def checkBST(self, min_val, max_val):
		if self.val < min_val or self.val > max_val:
			return False

		left_is_BST = True
		if self.l is not None:
			left_is_BST = self.l.checkBST(min_val, self.val)

			if left_is_BST is False:
				return False

		right_is_BST = True
		if self.r is not None:
			right_is_BST = self.r.checkBST(self.val, max_val)

			if right_is_BST is False:
				return False

		return True

	

if __name__ == '__main__':
	root = TreeNode(5)

	root.checkBST(-sys.maxint -1, sys.maxint)

