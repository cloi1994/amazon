# Table of Contents
1. [Memo](#memo)
2. [Easy](#easy)
3. [Binary Search](#binary-search)
4. [Binary Tree](#binary-tree)
5. [BFS](#bfs)
6. [DFS](#dfs)
7. [Stack](#stack)
8. [Backtacking](#backtacking)
9. [Linked List](#linked-list)


682 Baseball Game

## Memo

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|4	Median of Two Sorted Arrays | [py](code/4.py) | left = 0, right = n1 (no - 1) <br> cut1 = left + (right - left) // 2 <br> cut2 = (n1+n2) / 2 - cut1
|534 Design TinyURL || code2long <br> long2code <br> 5 random alpha|
|146	LRU Cache |[py](code/146.py) | Hash + DLL
|460 LFU Cache |------|-----|----------
|13	Roman to Integer |[py](code/13.py) | minus if num[cur-1] < num[cur]
|48 Rotate Image |[py](code/48.py)| Reverse First <br> for ... i = 0, for ... j = i+1 swap
|297 Serialize and Deserialize Binary Tree || save inorder <br> None = #
|5 Longest Palindromic Substring |[cpp](code/5.cpp)| (i,i) , (i+1,i) expand from center | dp[i, j] = 1  if i == j <br> s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]) <br> aba <br> a,0 - c,2 - b = 0+1,2-1
|516 Longest Palindromic Subsequence |[cpp](code/516.cpp)| dp[i][i] = 1 <br> if (s[i] == s[j]): dp[i][j] = dp[i + 1][j - 1] + 2 <br> else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
|23 Merge k Sorted Lists |[py](code/23.py)| Divide and Conquer <br> if left >= right: return lists[left]| PQ with head
|517 Super Washing Machines |------|-------
|121 Best Time to Buy and Sell Stock || create gain array <br> do maxiumum subarray  
|122 Best Time to Buy and Sell Stock II || if p[i+1] > p[i] : res += p[i+1] - p[i] 
|139 Word Break |[py](code/139.py)| dp[i] = postion can break

## Easy

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|2	Add Two Numbers | | while L1 or L2 or carry
|7	Reverse Integer |[py](code/7.py) | res = 10 * res + x % 10
|9	Palindrome Number | [py](code/9.py)| res = 10 * res + x % 10	
|168 Excel Sheet Column Title | [py](code/168.py)| 10 to 26	
|171 Excel Sheet Column Number | [py](code/171.py)| 26 to 10	
|238 Product of Array Except Self || 1 a1 a1a2 <br> a2a3 a1a3 a1a2
|380 Insert Delete GetRandom O(1) || HashMap -> index <br> swap last with delete ele
|155 Min Stack || Normal Stack + Min Stack
|49 Group Anagrams || list to string as key | sort each string as key
|242 Valid Anagram || Hash counting if same


## Two Pointer

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|1	Two Sum |[py](code/1.py) | HashMap , Sorted Two Pointer
|11	Container With Most Water |[py](code/11.py) | if left < right : left++ <br> elif right < left: right-- 
|42 Trapping Rain Water |[py](code/42.py)| arr : 1 2 3 <br> left : 1 2 3 <br> right : 3 3 3  | if height[i] < height[j]: left ++ <br> else right--

## Sliding Window
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|3	Longest Substring Without Repeating Characters | [py](code/3.py)| before put a ele in set <br> clear all char ahead that and delete that ele.
|239 Sliding Window Maximum | [py](code/239.py) | Silding Windows + Heap <br> add tail remove head
|215 Kth Largest Element in an Array || MaxHeap | if 2th Largest, iterate twice
|438 Find All Anagrams in a String| [py](code/438.py) | Silding Windows <br> add tail remove head


## Binary Search

| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|35	Search Insert Position | [py](code/35.py)|  while i < j : <br> j = mid
|350 Intersection of Two Arrays II | | sorted num1 and binary search num1 <br> del num1 visited | if all sorted <br> binary search largest one
|33 Search in Rotated Sorted Array |[py](code/33.py) | left half sorted : if nums[mid] >= nums[i]: <br> else: right half sorted or one element left | i++ if dup
|153 Find Minimum in Rotated Sorted Array |[py](code/153.py)| if nums[mid] > nums[j]: i = mid + 1 <br >else: j = mid | i++ if dup
|162 Find Peak Element|[py](code/162.py) |if nums[mid] < nums[mid+1]:i = mid + 1 <br> else: j = mid
|300 Longest Increasing Subsequence |[py](code/300.py)| (1) if x is larger than all tails, append it, increase the size by 1 <br> (2) if tails[i-1] < x <= tails[i], update tails[i]
|354 Russian Doll Envelopes|| (1) Sort the array. Ascend on width and descend on height if width are same. <br> (2) Find the longest increasing subsequence based on height
|240 Search a 2D Matrix II || start from left-bottom <br> if (matrix[x][y] > target) --x <br> else if (matrix[x][y] < target) ++y

## Binary Tree
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|298	Binary Tree Longest Consecutive Sequence |[py](code/298.py) | if root.val == expect: <br> curLen+1 <br> else: <br> curLen = 1 <br> dfs(root.left,expect+1,curLen) <br>
|236 Lowest Common Ancestor of a Binary Tree |[py](code/236.py)| p dict, q dict and set | if p or q: return <br> if left and right: return root
|235 Lowest Common Ancestor of a Binary Search Tree || search the tree base on p.val q.val <br> move left or right base on condition
|98 Validate Binary Search Tree || pass limit on child nodes
|315 Count of Smaller Numbers After Self || (1) Sort the array to BST. <br> (2) Find the depth of left subtree or Node contain leftsubtree count

## BFS
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|675 Cut Off Trees for Golf Event |[py](code/675.py) | PQ + BFS
|127 Word Ladder |[py](code/127.py)| BFS to replace each word <br> remove word when seen

## DFS
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|200 Number of Islands | [py](code/200.py) | For each position <br> dfs 4 directions <br> change 0 to 1 | 
|377 Combination Sum IV || for n in nums: summ += self.dfs(nums,target-n,dp) <br> dp[target] = summ | return 0 or 1
|529 Minesweeper || dfs count num of near mine <br> if 0: search 4 way <else> stop and mark num

## Backtacking
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|17 Letter Combinations of a Phone Number |  | for ele in dict[index] | 
|282 Expression Add Operators |[py](code/282.py)| for i in range(idx,len(num)): <br> val = num[idx:i+1] | string partition <br> abc -> a -> b -> c <br> a -> bc <br> ab -> c <br> abc
|40 Combination Sum II | |dfs(i+1) <br> if i != start && num[i] == num[i - 1]: continue 
|47 Permutations II|[py](code/529.py)|if i > 0 and nums[i-1] == nums[i] and not visited[i-1] == 0: continue

## Linked List
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|138 Copy List with Random Pointer | [py](code/138.py) | newHead -> newCur -> None <br> hm[cur] = newCur | S1-> N_S1 -> S2 -> N_S2
|206 Reverse Linked List || prev = None, nextCur = cur.next 
|234 Palindrome Linked List || stack, if not fast.next == odd | reverse second half list
|160 Intersection of Two Linked Lists || find length different | while a != b , if a = null: a = bHead else b = aHead
|141 Linked List Cycle || slow and fast, if meet again has cycle | slow = head, if meet again <br> slow = entry point

## Stack
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|20	Valid Parentheses | | push if '(' <br> pop if ')' | counter++ if '(' <br> counter-- if '('
|682 Baseball Game | | follow rules


