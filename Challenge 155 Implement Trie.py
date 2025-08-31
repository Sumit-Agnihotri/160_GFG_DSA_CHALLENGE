query = [[1, "abcd"], [1, "abc"], [1, "bcd"], [2, "bc"], [3, "bc"], [2, "abc"]]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isend = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isend

    def isPrefix(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

s = Trie()
for q in query:
    if q[0] == 1:
        s.insert(q[1])
    elif q[0] == 2:
        print(s.search(q[1]))
    else:
        print(s.isPrefix(q[1]))