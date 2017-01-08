class TreeNode:

	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None

	def path(self, val, cur_path):

		temp_cur_path = cur_path[:]
		if self.val == val:
			temp_cur_path.append(val)
			return temp_cur_path

		if self.l is not None:
			temp_cur_path.append(self.val)
			ret_path = self.l.path(val, temp_cur_path)

			if ret_path is not None:
				return ret_path
			temp_cur_path.pop()

		if self.r is not None:
			temp_cur_path.append(self.val)
			ret_path = self.r.path(val, temp_cur_path)
			if ret_path is not None:
				return ret_path
			temp_cur_path.pop()

		return None

	@staticmethod
	def LCA(path1, path2):
		if path1 is None or path2 is None:
			return None

		len_path_1 = len(path1)
		len_path_2 = len(path2)

		new_len_path_1 = min(len_path_1, len_path_2)
		new_len_path_2 = min(len_path_1, len_path_2)

		new_path1 = path1[:new_len_path_1]
		new_path2 = path2[:new_len_path_2]

		idx = new_len_path_1 - 1
		
		while idx >= 0:
			if new_path1[idx] == new_path2[idx]:
				return new_path1[idx]
			idx -= 1

		return None


if __name__ == '__main__':

	root = TreeNode(1)
	root.l = TreeNode(2)
	root.r = TreeNode(3)
	root.l.l = TreeNode(4)
	root.l.r = TreeNode(5)
	root.r.l = TreeNode(6)
	root.r.r = TreeNode(7)

	print TreeNode.LCA(root.path(6,[]), root.path(7, [])) 
