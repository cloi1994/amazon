## Memo

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|4	Median of Two Sorted Arrays | [py](https://github.com/cloi1994/amazon/blob/master/code/4.py) | left = 0, right = n1 (no - 1) <br> cut1 = left + (right - left) // 2 <br> cut2 = (n1+n2) / 2 - cut1
|534 Design TinyURL || code2long <br> long2code <br> 5 random alpha|
|146	LRU Cache |[py](https://github.com/cloi1994/amazon/blob/master/code/146.py) | Hash + DLL
|13	Roman to Integer |[py](https://github.com/cloi1994/amazon/blob/master/code/13.py) | minus if num[cur-1] < num[cur]


## Easy

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|2	Add Two Numbers | | while L1 or L2 or carry
|7	Reverse Integer |[py](https://github.com/cloi1994/amazon/blob/master/code/7.py) | res = 10 * res + x % 10
|9	Palindrome Number | [py](https://github.com/cloi1994/amazon/blob/master/code/9.py)| res = 10 * res + x % 10	
|168 Excel Sheet Column Title | [py](https://github.com/cloi1994/amazon/blob/master/code/168.py)| 10 to 26	
|171 Excel Sheet Column Number | [py](https://github.com/cloi1994/amazon/blob/master/code/171.py)| 26 to 10	



## Two Pointer

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|1	Two Sum |[py](https://github.com/cloi1994/amazon/blob/master/code/1.py) | HashMap , Sorted Two Pointer
|3	Longest Substring Without Repeating Characters | [py](https://github.com/cloi1994/amazon/blob/master/code/3.py)| before put a ele in set <br> clear all char ahead that and delete that ele.
|11	Container With Most Water |[py](https://github.com/cloi1994/amazon/blob/master/code/11.py) | if left < right : left++ <br> elif right < left: right-- 


## Binary Search

| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|35	Search Insert Position | [py](https://github.com/cloi1994/amazon/blob/master/code/35.py)|  while i < j : <br> j = mid
|350 Intersection of Two Arrays II | | sorted num1 and binary search num1 <br> del num1 visited | if all sorted <br> binary search largest one
|33 Search in Rotated Sorted Array |[py](https://github.com/cloi1994/amazon/blob/master/code/33.py) | left half sorted : if nums[mid] >= nums[i]: <br> else: right half sorted or one element left
|153 Find Minimum in Rotated Sorted Array |[py](https://github.com/cloi1994/amazon/blob/master/code/153.py)| if nums[mid] > nums[j]: i = mid + 1 <br >else: j = mid
|162 Find Peak Element|[py](https://github.com/cloi1994/amazon/blob/master/code/162.py) |if nums[mid] < nums[mid+1]:i = mid + 1 <br> else: j = mid
|300 Longest Increasing Subsequence |[py](https://github.com/cloi1994/amazon/blob/master/code/300.py)| (1) if x is larger than all tails, append it, increase the size by 1 <br> (2) if tails[i-1] < x <= tails[i], update tails[i]
|354 Russian Doll Envelopes|| (1) Sort the array. Ascend on width and descend on height if width are same. <br> (2) Find the longest increasing subsequence based on height
|315 Count of Smaller Numbers After Self || (1) Sort the array to BST. <br> (2) Find the depth of left subtree or Node contain leftsubtree count

## Binary Tree
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|298	Binary Tree Longest Consecutive Sequence |[py](https://github.com/cloi1994/amazon/blob/master/code/298.py) | if root.val == expect: <br> curLen+1 <br> else: <br> curLen = 1 <br> dfs(root.left,expect+1,curLen) <br>

## BFS
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|675 Cut Off Trees for Golf Event |[py](/code/675.py) | PQ + BFS

## Stack
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|20	Valid Parentheses | | push if '(' <br> pop if ')' | counter++ if '(' <br> counter-- if '('

