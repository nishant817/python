|| [Misc](cheatsheets/catchall.md) | [Collections](cheatsheets/collections.md) | [Queue/Stack](cheatsheets/queue.md) ||

## Misc
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
      * - 9223372036854775808
   * `x = a if <condition> else b`   --> ternary Operator

## String
   * substring: `strobj[start:end:step]`
	   * e.g. `strObj[1:5]`
   * last character: `strObj[-1]`
   * last 5 chars: `strObj[-5:]`
   * all characters except the last 4 characters and the 1st character: `strObj[1:-4]`
   * every other character: `strObj[::2]`
   * `.find(sub, start, end)`   -> returns the lowest index of the substring if it is found; else -1

