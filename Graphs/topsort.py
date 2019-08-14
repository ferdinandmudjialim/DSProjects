# Induction-based topological sort
# This is based on the fact that if you take out the root of a DAG, 
# there will always be one root to replace it b/c of the directed acyclic property
def topsort(G): 
	count = dict((u, 0) for u in G)  # how many arrows coming in for each node
	for u in G: 
		for v in G[u]:
			count[v] += 1
	Q = [u for u in G if count[u] == 0]  # valid "roots" with no edges coming in
	S = []  # this is the result (eventually)
	while Q: 
		u = Q.pop()
		S.append(u)  # append the new "root"
		for v in G[u]:  # for the neighbors of the "root"
			count[v] -= 1  # destroy the edge connecting the "root" and neighbor
			if count[v] == 0:  # does a neighbor now have no incoming edges?
				Q.append(v)  # if so, that becomes the new "root" for the new DAG'
	return S

if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG

	print(topsort(myDAG))