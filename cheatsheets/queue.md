|| [Misc](catchall.md) | [Collections](collections.md) | [Queue/Stack](queue.md) ||

# Queue

## queue.Queue
   * `from queue import Queue`
   * `qu = queue.Queue()`
   * `qu.put(obj)`
   * `qu.get()`
   * `qu.empty()`
   * `qu.size()`

## Priority Queue - MIN Heap (Ascending order)
   * `from queue import PriorityQueue`
   * `pq = queue.PriorityQueue()`
   * `pq.put(obj)`    --> O(logn)
   * `pq.get()`          ---> O(logn)
   * `pq.empty()`
   * `pq.qsize()`

## PriorityQueue - MAX Heap (Descending order) 
(i.e. output max first)
   * `from queue import PriorityQueue`
   * `pq = queue.PriorityQueue()`
   * `pq.put((-obj, obj))`  -- pq.put((-priority, obj))
      * First item of Tuple is priority and 2nd is actual obj
      * Basically reversing the priority by using nagative of obj
   * `pq.get()[1]`  -- Get the item/obj
   * `pq.get()`     -- returns (-priority, obj)

------------------------------
------------------------------

# Stack

## queue.LifoQueue
   * stack = LifoQueue(maxsize=3)
   * `stack.qsize()`   --> number of elements
   * `stack.put(obj)`
   * `stack.full()`     --> is Full?
   * `stack.get()`      --> get in LIFO (stack) order

## collections.deque
   * `from collections import deque`
   * `stack = deque()`
   * `stack.append(ele1)`
   * `stack.append(ele2)`
   * `stack.pop()`   --> get in LIFO (stack) order
   * `stack.popleft()` #dequeue from the Front of Queue
   * `stack.empty()` # Is Empty?
   * `print(stack)`  --> output: deque(['a', 'b', 'c'])