from queue import Queue
from typing import List
import sys
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        rcount = len(rowCosts)
        ccount = len(colCosts)
        
        mincost = [[sys.maxsize for c in range(ccount)] for r in range(rcount)]
        checked = [[0 for c in range(ccount)] for r in range(rcount)]
        mincost[startPos[0]][startPos[1]] = 0
        qu = Queue()        
        qu.put(startPos)
        
        while not qu.empty():
            pos = qu.get()
            row = pos[0]
            col = pos[1]
            if checked[row][col] == 1:
                continue
                
            checked[row][col] = 1
                
            if row-1 >= 0:
                qu.put([row-1, col])
                mincost[row-1][col] = min(mincost[row-1][col], (mincost[row][col] + rowCosts[row-1]))
                
            if row+1 < rcount:
                qu.put([row+1, col])
                mincost[row+1][col] = min(mincost[row+1][col], (mincost[row][col] + rowCosts[row+1]))
                
            if col-1 >= 0:
                qu.put([row, col-1])
                mincost[row][col-1] = min(mincost[row][col-1], (mincost[row][col] + colCosts[col-1]))
                
            if col+1 < ccount:
                qu.put([row, col+1])
                mincost[row][col+1] = min(mincost[row][col+1], (mincost[row][col] + colCosts[col+1]))
                
        return mincost[homePos[0]][homePos[1]]
                                          
print(Solution().minCost([1,0], [2,3], [5,4,3], [8,2,6,7]))
            
    