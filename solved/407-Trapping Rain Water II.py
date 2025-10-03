import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 1 or len(heightMap[0]) <= 1:
            return 0

        hq = []
        ans = 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]

        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(hq, (heightMap[r][c], r, c))
                visited[r][c] = True

        for c in range(1, n - 1):
            for r in (0, m - 1):
                heapq.heappush(hq, (heightMap[r][c], r, c))
                visited[r][c] = True

        drt = ((1, 0), (0, 1), (-1, 0), (0, -1))

        while hq:
            h, r, c = heapq.heappop(hq)
            for dx, dy in drt:
                dr, dc = r + dx, c + dy

                if 0 <= dr < m and 0 <= dc < n and not visited[dr][dc]:
                    visited[dr][dc] = True
                    dh = heightMap[dr][dc]

                    if dh < h:
                        ans += h - dh

                    heapq.heappush(hq, (max(h, dh), dr, dc))

        return ans
