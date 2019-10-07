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

# time: O(mn + nlogn + mn)
import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(workers), len(bikes)
        distance_list = [[] for _ in range(m)]
        used_bikes = set()
        result = [-1] * len(workers)
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distance_list[i].append((distance, i, j))
            distance_list[i].sort()

        heap = [(distance_list[i][0][0], distance_list[i][0][1], distance_list[i][0][2], 0) for i in range(m)]
        heapq.heapify(heap)
        used_workers_count = 0
        while used_workers_count < m:
            _, worker_idx, bike_idx, pos = heapq.heappop(heap)
            if bike_idx in used_bikes:
                heapq.heappush(heap, (distance_list[worker_idx][pos + 1][0], distance_list[worker_idx][pos + 1][1], distance_list[worker_idx][pos + 1][2], pos + 1))
                continue
            result[worker_idx] = bike_idx
            used_bikes.add(bike_idx)
            used_workers_count += 1
        return result
