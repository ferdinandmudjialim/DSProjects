# Ferdinand Mudjialim, Partner: Nick Parisi
from math import inf
import queue


def djikstra_shortest_paths(vertices, adj_list, weights, start):
    # Returns the weight of the shortest path from start to each other vertex in vertices.
    # The result should be returned as a dictionary.
    # If no path exists from start to another vertex, then the weight is inf
    # The weight of a path from any vertex to itself is 0.
    S = {}
    Q = queue.PriorityQueue()
    for vert in vertices:
        S[vert] = inf
    S[start] = 0
    Q.put((0, start))
    # queue with Q.put(key)
    # dequeue with Q.get()
    # use Q.empty() to check if the heap is empty
    while not Q.empty():
        u = Q.get()[1]
        for v in adj_list[u]:
            if S[v] > S[u] + weights[u][v]:
                S[v] = S[u] + weights[u][v]
                Q.put((S[v], v))
    return S


class Tree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None


def huffman_codes(chars, freqs):
    # Returns the codeword for each character in chars
    # The result should be a dictionary of characters to codewords.
    # TODO: implement
    S = {}
    for c in chars:
        S[c] = '-'
    Q = queue.PriorityQueue()
    # queue with Q.put(key)
    # dequeue with Q.get()
    # use Q.empty() to check if the heap is empty

    # Construct the Huffman Tree
    for letter in freqs:
        Q.put((freqs[letter], Tree(freqs[letter], letter)))
    while Q.qsize() != 1:
        N1 = Q.get()  # Format: (frequency, Tree) <---tuple
        N2 = Q.get()
        T = Tree(N1[0] + N2[0], '')
        T.left = N1[1]
        T.right = N2[1]
        Q.put((N1[0] + N2[0], T))
    # Traverse the Huffman Tree to get encodings
    hTree = Q.get()[1]

    def traverse(tree, encoding=''):
        if tree.left:
            traverse(tree.left, encoding+'0')
        if tree.right:
            traverse(tree.right, encoding+'1')
        if tree.value != '':
            S[tree.value] = encoding

    traverse(hTree)
    return S


if __name__ == '__main__':
    vertices = [ 'a', 'b', 'c', 'd', 'e', 'f' ]
    adj_list = {
        'a': [ 'b', 'c', 'e' ],
        'b': [ 'c', 'd' ],
        'c': [ 'd' ],
        'd': [ 'f' ],
        'e': [ 'f' ],
        'f': []
    }
    weights = {
        'a': { 'b': 2, 'c': 6, 'e': 4 },
        'b': { 'c': 3, 'd': 2 },
        'c': { 'd': 0 },
        'd': { 'f': 2 },
        'e': { 'f': 4 },
        'f': {}
    }
    results = {
        'a': { 'a': 0, 'b': 2, 'c': 5, 'd': 4, 'e': 4, 'f': 6 },
        'b': { 'a': inf, 'b': 0, 'c': 3, 'd': 2, 'e': inf, 'f': 4 },
        'c': { 'a': inf, 'b': inf, 'c': 0, 'd': 0, 'e': inf, 'f': 2 },
        'd': { 'a': inf, 'b': inf, 'c': inf, 'd': 0, 'e': inf, 'f': 2 },
        'e': { 'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': 0, 'f': 4 },
        'f': { 'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': inf, 'f': 0 }
    }
    for vert in vertices:
        paths = djikstra_shortest_paths(vertices, adj_list, weights, vert)
        for target in vertices:
            if paths[target] != results[vert][target]:
                print('expected', vert, '->', target, 'to equal', results[vert][target], 'received', paths[target])
    chars = [ 'a', 'b', 'c', 'd', 'e', 'f' ]
    freqs = {
        'a': 18,
        'b': 22,
        'c': 15,
        'd': 13,
        'e': 20,
        'f': 12
    }
    results = {
        'a': '111', 'b': '01', 'c': '110', 'd': '101', 'e': '00', 'f': '100'
    }
    codes = huffman_codes(chars, freqs)
    for c in chars:
        if codes[c] != results[c]:
            print('expected codeword of', c, 'to be', results[c], 'received', codes[c])
    print('Done!')
