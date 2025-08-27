from collections import deque, defaultdict

class Solution:
    def findOrder(self, words):  # Added self
        graph = defaultdict(set)
        indegree = defaultdict(int)

        # Initialize indegree for all characters
        for w in words:
            for c in w:
                indegree[c] = 0

        # Build graph
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in graph[x]:
                        graph[x].add(y)
                        indegree[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""

        # Topological sort
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""

# Usage
words = ["baa", "abcd", "abca", "cab", "cad"]
s = Solution()
print(s.findOrder(words))  # Output: "bdac"