class Direction:
	left, right = range(2)

class TreeNode:

	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None
		self.n = None

	
def levelTraversal(root):

	queue = []
	queue.append(root)
	next_level_queue = []
	tra = []
	prev = None
	dir = Direction.left

	while True:
		if len(queue) == 0:
			break

		temp = queue.pop(0)

		if prev is not None:
			if dir is Direction.left:
				temp.n = prev
			else:
				prev.n = temp

		if temp.l is not None:
			next_level_queue.append(temp.l)

		if temp.r is not None:
			next_level_queue.append(temp.r)

		prev = temp

		if len(queue) == 0:
			#print tra
			tra = []
			queue = next_level_queue[:]
			next_level_queue = []

			if dir is Direction.left:
				dir = Direction.right
			else:
				dir = Direction.left


if __name__ == "__main__":

	root = TreeNode(1)
	root.l = TreeNode(2)
	root.r = TreeNode(3)
	root.l.l = TreeNode(4)
	root.l.r = TreeNode(5)
	root.r.l = TreeNode(6)
	root.r.r = TreeNode(7)

	levelTraversal(root)

	print root.l.val ,  root.l.n.val
	print root.r.r.val, root.r.r.n.val , root.r.r.n.n.val , root.r.r.n.n.n.val 

















