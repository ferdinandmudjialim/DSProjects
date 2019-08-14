def dfs(G, u, S): 
	if S is None: 
		S = set()
	S.add(u) 
	for v in G[u]: 
		if v in S: 
			continue
		dfs(G, v, S)

if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG
	myset = set()
	dfs(myDAG, 'F', myset)
	print(myset)