

# Misc
   * `x = max(y, z)`    -- max of y and z
   * `freq = Counter(wordsList)`  -> create a dictionary with with the frequency of each word
   * `sorted(freq.items(), key = lambda x: (-x[1], x[0]))`
      * sort it by freequency and in lexicographic order
   * check: https://leetcode.com/problems/top-k-frequent-words/discuss/1859025/Python
   * `bin(num)`
      * binary string of num prefixed with 0b. e.g. bin(5) = 0b101
   * `MAXInteger: sys.maxsize`
      * 9223372036854775807
   * `MIN Integer: - sys.maxsize - 1` 
      * -9223372036854775808
   * `x = a if <condition> else b`   --> ternary Operator
   * Char to Num (ASCII)
      * `n = ord('a')`  --> n = 97
      * `ch = chr(ord('a') + 1)` --> ch = 'b'
   * Touple
      * Used to store multiple items in a single variable
      * unchangeable --> cannot change, add or remove items after the tuple has been created
      * Allows duplicate
      * can contain mixed data types
      * `mytuple = ("apple", "banana", "cherry")`
      * `print mytuple[1]` --> "banana"
      * `len(mytuple)`
      * Convert tuple to list
         * `lst = list(mytuple)`
      * Convert list to tuple
         * `newtuple = tuple(lst)`
      * Iterate
         * `for x in mytuple`
      * `mytuple.count(obj)`  --> count of obj in tuple
      * `mytuple.index(obj)`  --> index of obj
   

<br>

# String 
https://www.w3schools.com/python/python_ref_string.asp
   * substring: `strobj[start:end:step]`
	   * e.g. `strObj[1:5]`
   * last character: `strObj[-1]`
   * last 5 chars: `strObj[-5:]`
   * all characters except the last 4 characters and the 1st character: `strObj[1:-4]`
   * every other character: `strObj[::2]`
   * `.find(sub, start, end)`   -> returns the lowest index of the substring if it is found; else -1

<br>


# Array: 
   * `list1 = [0]*size`   --> initialize all 0
   * `list1 = [None]*size`
   * `list1 = ['a']*size`
   * `twoDList = [ [0 for c in range(cols) ] for r in range(rows) ]`
   * `twoDList = [ [0]*cols for i in range(rows)]`
   * Copy/Deepcopy
      * ???

<br>


# List
https://www.w3schools.com/python/python_ref_list.asp
   * `lst = []`
   * `lst[index]`
   * `lst[start:end]`
   * `lst[-1]`  -> last item
   * `.append(obj)`
   * `.clear()`
   * `.copy()`    --> make a copy of list
   * `.count(obj)`  -> count of obj
   * `.index(obj)`
   * `.insert(index, obj)`
   * `.pop(index)`   -> delete at index
   * `.pop()`  -> remove last item
   * `.remove(obj)`
   * `.reverse()`
   * `.sort()`  ---> ascending order
   * `.sort(reverse=True)` --> descending order
   * Custom Sort
      * `lst = [[7,30],[5,10],[15,20]]`
      * `lst.sort(key=lambda x:x[1])`  --> sort of 2nd element of each list

<br>


# Set
https://www.w3schools.com/python/python_ref_set.asp
   * `myset = set()`
   * `myset = {1,2,3}`
   * `.add(obj)`
   * `.clear()`
   * `.copy()`
   * `.discard(obj)`  -> DOESN'T throw error if obj doesn't exist
   * `.remove(obj)`  -> throws error if obj doesn't exist
   * `.pop()`   -> remove last item. Note: set is unordered

<br>


# Dictionary/Map
https://www.w3schools.com/python/python_ref_dictionary.asp
   * `dict = {}`
   * `dict = {'a': 1, 'b': 2}`
   * `dict.update({'c': 3})`   --> this is add c or update if doesn't exists
   * `dict.pop(obj)`    --> remove the item
   * `del dict[key]`
   * `dict.clear()`
   * `dict.popitem()`   --> removed last inserted or random item
   * `dict[key] = value`
   * `if key in dict` # check if exists
   * add or update: `dict[obj] = dict.setdefault(obj, 0) + 1`
   * iterate
	   * `for key in dict`  #iterate though keys
		* `for key, val in dict.items()`  #better way
      * for x in thisdict.values()
      * for x in thisdict.keys()
   * `len(dict)`
   * `x = thisdict.keys()`  --> List of keys
   * `x = thisdict.values()`  --> list of values
   * `newdict = dict(thisdict)`  --> copy dictionary
   * Create and initiate using array as key
      * `dict = {i:[] for i in range(n)}`  --> value as empty list
      * `dict = {i:MyClass(i) for i in someList}`

<br>

## OrderedDict
   * `from collection import OrderedDict`
   * preserves the order in which the keys are inserted

<br>


# Queue

## queue.Queue
   * `from queue import Queue`
   * `qu = queue.Queue()`
   * `qu.put(obj)`
   * `qu.get()`
   * `qu.empty()`
   * `qu.size()`

## Priority Queue - Using heapq
   * `heapq.heapify(lst)`  --> Transform list x into a heap, in-place, in linear time
   * `heapq.hepppush(lst, item)`
   * `popped = heapq.heppop(lst)`
   * `popped = heapq.pushpop(lst, item)` --> first push then pop
   * `popped = heapq.heapreplace(heap, item)` --> first pop then push
   * `heapq.nlargest(n, iterable, key=None)`
   * `heapq.nsmallest(n, iterable, key=None)`

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

<br>


# Stack

## queue.LifoQueue
   * stack = LifoQueue(maxsize=3)
   * `stack.qsize()`   --> number of elements
   * `stack.put(obj)`
   * `stack.full()`     --> is Full?
   * `stack.get()`      --> get in LIFO (stack) order

<br>

## collections.deque
   * `from collections import deque`
   * `stack = deque()`
   * `stack.append(ele1)`
   * `stack.append(ele2)`
   * `stack.pop()`   --> get in LIFO (stack) order
   * `stack.popleft()` #dequeue from the Front of Queue
   * `stack.empty()` # Is Empty?
   * `print(stack)`  --> output: deque(['a', 'b', 'c'])

<br>


# Space Complexity
   * sorting: Nlog(N)
   * heap: log(N)

### TODO/Add  
touple details  
deepcopy 2/3D array  
