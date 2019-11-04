# time: O(mn + mnlog(mn) + mn)
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distance_list = []
        used_workers = set()
        used_bikes = set()
        result = [-1] * len(workers)
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distance_list.append((distance, i, j))
        distance_list.sort()
        for _, worker_idx, bike_idx in distance_list:
            if worker_idx in used_workers or bike_idx in used_bikes:
                continue
            result[worker_idx] = bike_idx
            used_workers.add(worker_idx)
            used_bikes.add(bike_idx)
            if len(used_workers) == len(workers):
                break
        return result

# time: O(mn + mnlogn + mnlogn)
import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(bikes), len(workers)
        result = [-1] * n
        distances = [[] for _ in range(n)]
        candidates = []
        for i in range(n):
            for j in range(m):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distances[i].append((distance, j))
            distances[i].sort()
            candidates.append((distances[i][0][0], i, 0))
        heapq.heapify(candidates)

        paired_bikes = set()
        while len(paired_bikes) < n:
            distance, worker_idx, bike_pos = heapq.heappop(candidates)
            if distances[worker_idx][bike_pos][1] in paired_bikes:
                heapq.heappush(candidates, (distances[worker_idx][bike_pos + 1][0], worker_idx, bike_pos + 1))
                continue
            paired_bikes.add(distances[worker_idx][bike_pos][1])
            result[worker_idx] = distances[worker_idx][bike_pos][1]
        return result
