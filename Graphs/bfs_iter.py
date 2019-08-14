# BFS from Ian Riley pseudocode
def bfs(G, u, S): 
	if S is None: 
		S = set()
		Q0 = []  # two empty queues 
		Q1 = []  # can use one, but this differentiates layers
		Q0.insert(0, u)  # u is the root, queue
		while Q0: 
			while Q0:
				u = Q0.pop()
				for v in G[u]: 
					if v in S: 
						continue
					Q1.insert(0, v)  # queue v
					S.add(v)
				Q0 = Q1
				Q1 = []

if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG
	myset = set()
	bfs(myDAG, 'G', myset)
	print(myset)