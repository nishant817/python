|| [Misc](catchall.md) | [Collections](collections.md) | [Queue/Stack](queue.md) ||

# array: 
   * `list1 = [0]*size`   --> initialize all 0
   * `list1 = [None]*size`
   * `list1 = ['a']*size`
   * `twoDList = [ [0 for c in range(cols) ] for r in range(rows) ]`
   * `twoDList = [ [0]*cols for i in range(rows)]`

-----------------------------

# List
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

-----------------------------
# Set
   * `myset = set()`
   * `myset = {1,2,3}`
   * `.add(obj)`
   * `.clear()`
   * `.copy()`
   * `.discard(obj)`  -> DOESN'T throw error if obj doesn't exist
   * `.remove(obj)`  -> throws error if obj doesn't exist
   * `.pop()`   -> remove last item. Note: set is unordered

-----------------------------

# Dictionary/Map
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

## OrderedDict
   * `from collection import OrderedDict`
   * preserves the order in which the keys are inserted
