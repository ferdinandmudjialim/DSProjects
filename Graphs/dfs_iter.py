def dfs(G, s, S): 
	if S is None: 
		S = set()
	Stack = []
	Stack.append(s)
	while Stack: 
		u = Stack[-1]  # peek Stack
		S.add(u)

		# if all neighbors already visited, then pop the Stack
		# if not, then choose next u not already visited
		flag = False
		for v in G[u]:
			if v not in S:
				flag = True
				u = v
				break
		if flag:  # found unvisited neighbor
			Stack.append(u)
		else:  # all already visited
			Stack.pop()
	return S


if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG
	myset = set()
	dfs(myDAG, 'G', myset)
	print(myset)
