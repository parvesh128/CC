class ReturnType:
	oneFound, BothFound, NoneFound = range(3)


class ReturnNode:

	def __init__(self, val, returnType):
		self.val = val
		self.type = returnType

class TreeNode:

	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None

	def exists(self, val):
		if self.val == val:
			return True

		if self.l is not None:
			ret = self.l.exists(val)
			if ret:
				return True

		if self.r is not None:
			ret = self.r.exists(val)
			if ret:
				return True

		return False


	def LCASimple(self, val1, val2):

		if self.val == val1 or self.val == val2:
			return self

		left_lca = None
		if self.l is not None:
			left_lca = self.l.LCASimple(val1, val2)

		right_lca = None
		if self.r is not None:
			right_lca = self.r.LCASimple(val1, val2)

		if left_lca and right_lca:
			return self

		return left_lca if left_lca else right_lca

	def LCA(self, val1, val2):

		if self.val == val1:
			if not self.exists(val2):
				return ReturnNode(None, ReturnType.oneFound)
			else:
				return ReturnNode(self.val, ReturnType.BothFound)

		if self.val == val2:
			if not self.exists(val1):
				return ReturnNode(None, ReturnType.oneFound)
			else:
				return ReturnNode(self.val, ReturnType.BothFound)

		# find in left path
		ret_l = None
		if self.l is not None:
			ret_l = self.l.LCA(val1, val2)

			if ret_l.type == ReturnType.BothFound:
				return ret_l

		ret_r = None
		if self.r is not None:
			ret_r = self.r.LCA(val1, val2)

			if ret_r.type == ReturnType.BothFound:
				return ret_r

		if ret_l is None and ret_r is None:
			return ReturnNode(None, ReturnType.NoneFound)

		if ret_l is None:
			return ret_r

		if ret_r is None:
			return ret_l

		if ret_l.type is ReturnType.oneFound and ret_r.type is ReturnType.oneFound:
			return ReturnNode(self.val , ReturnType.BothFound)

		if ret_l.type is ReturnType.oneFound or ret_r.type is ReturnType.oneFound:
			return ReturnNode(None , ReturnType.oneFound)

		return ReturnNode(None, ReturnType.NoneFound)



if __name__ == '__main__':

	root = TreeNode(1)
	root.l = TreeNode(2)
	root.r = TreeNode(3)
	root.l.l = TreeNode(4)
	root.l.r = TreeNode(5)
	root.r.l = TreeNode(6)
	root.r.r = TreeNode(7)

	ret = root.LCASimple(4, 5)
	if ret is not None:
		print ret.val
	else:
		print "No LCA"
