class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def dfs(pos, visited):
            if pos == n:
                return 0
            if (pos, tuple(visited)) in cache:
                return cache[(pos, tuple(visited))]
            result = float('inf')
            for j in range(m):
                if visited[j]:
                    continue
                result = min(result, calc_dist(workers[pos], bikes[j]) + dfs(pos + 1, visited[:j] + [1] + visited[j+1:]))
            cache[(pos, tuple(visited))] = result
            return result

        calc_dist = lambda w, b: abs(w[0] - b[0]) + abs(w[1] - b[1])
        m, n = len(bikes), len(workers)
        cache = {}
        return dfs(0, [0] * m)


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def dfs(pos, visited):
            if pos == n:
                return 0
            if (pos, visited) in cache:
                return cache[(pos, visited)]
            result = float('inf')
            for j in range(m):
                if visited & 1 << j:
                    continue
                result = min(result, calc_dist(workers[pos], bikes[j]) + dfs(pos + 1, visited | 1 << j))
            cache[(pos, visited)] = result
            return result

        calc_dist = lambda w, b: abs(w[0] - b[0]) + abs(w[1] - b[1])
        m, n = len(bikes), len(workers)
        cache = {}
        return dfs(0, 0)