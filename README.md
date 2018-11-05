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


73 Set Matrix Zeroes
8 String to Integer (atoi)
396 Rotate Function
646 Maximum Length of Pair Chain
640 Solve the Equation

## Memo

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|4	Median of Two Sorted Arrays | [py](code/4.py) | left = 0, right = n1 (no - 1) <br> cut1 = left + (right - left) // 2 <br> cut2 = (n1+n2) / 2 - cut1
|534 Design TinyURL || code2long <br> long2code <br> 5 random alpha|
|146	LRU Cache |[py](code/146.py) | Hash + DLL
|460 LFU Cache |------|-----|----------
|13	Roman to Integer |[py](code/13.py) | minus if num[cur-1] < num[cur]
|12 Integer to Roman | | Greedy while (num >= val[i]): <br> nums[i] -= val[i] <br> res+= str[i]
|48 Rotate Image |[py](code/48.py)| Reverse First <br> for ... i = 0, for ... j = i+1 swap
|297 Serialize and Deserialize Binary Tree || save inorder <br> None = #
|5 Longest Palindromic Substring |[cpp](code/5.cpp)| (i,i) , (i+1,i) expand from center | dp[i, j] = 1  if i == j <br> s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]) <br> aba <br> a,0 - c,2 - b = 0+1,2-1
|516 Longest Palindromic Subsequence |[cpp](code/516.cpp)| dp[i][i] = 1 <br> if (s[i] == s[j]): dp[i][j] = dp[i + 1][j - 1] + 2 <br> else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
|23 Merge k Sorted Lists |[py](code/23.py)| Divide and Conquer <br> if left >= right: return lists[left]| PQ with head
|517 Super Washing Machines |------|-------
|121 Best Time to Buy and Sell Stock || create gain array <br> do maxiumum subarray  
|122 Best Time to Buy and Sell Stock II || if p[i+1] > p[i] : res += p[i+1] - p[i] 
|139 Word Break |[py](code/139.py)| dp[i] = postion can break
|151 Reverse Words in a String ||  while j >= 0 and s[j] == ' ': <br> while j >= 0 and s[j] != ' ':
|459 Repeated Substring Pattern || if n%i and connected substirng == original <br> return true
|532 K-diff Pairs in an Array || hm <br> if if k == 0 -> if hm[key] >= 2 : cnt +=1  <br> else: if key - k in hm: cnt+1|
|75 Sort Colors || A[cur] = 0：swap(A[cur++],A[left++]) <br> A[cur] = 1: cur ++
|211 Add and Search Word - Data structure design || c != '#' and self.searchWord(word[i+1:],p[c])
|269 Alien Dictionary || indegree, BFS degree(0)
|863 All Nodes Distance K in Binary Tree || build graph hm[parent] = child, hm[child] = parent
|224 Basic Calculator || num,sign,res <br> if '(' push(res),push(sign)
|227 Basic Calculator II | [cpp](code/227.cpp| op='+',res = 0, curRes = 0, num = 0 | if (c == '+' || c == '-' || i == n - 1): <br>  res += curRes <br> curRes = 0
|150 Evaluate Reverse Polish Notation || stack.append(), isOp: pop 2 times
|322 coin change || dp[i] = min(dp[i], dp[i - coins[j]] + 1)
|55 Jump Game || reach = max(reach, i + nums[i]) 
|10 Regular Expression Matching || if p[j] == s[i]: dp[i][j] = dp[i-1][j-1] <br> p[j] == '.': dp[i][j] = dp[i-1][j-1] | if p[j] == '*': <br> if p[j-1] != p[i] and p[j-1] != '.':  dp[i][j] = dp[i][j-2] <br> if p[j-1] == s[i] or p[j-1] == '.': dp[i][j] =  dp[i-1][j] (multiple a) | dp[i][j-2] (empty a)

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
|414 Third Maximum Number || v = [-inf,-inf,-inf]
|89 Gray Code || int inc = 1 <br> greySeq[j]+inc <br> inc <<= 1
|791 Custom Sort String || Store the order of char in a hashtable <br> Sort the string based on the order
|661 Image Smoother || check all dir cnt/all
|645 Set Mismatch || if i not in d = missing <br> if d[i] == 2 = repeat
|622 Design Circular Queue || array| rear = (front + size) % capacity <br> front = (front + 1) % capacity
|295 Find Median from Data Stream |[cpp](code/295.cpp)| small pq, larget pq
|198 House Robber || max(num[i] + dp[i - 2], dp[i - 1]) | search two times with head no tail or no head tail
|79 Largest Number || to_string(a) + to_string(b) > to_string(b) + to_string(a)

## Two Pointer

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|1	Two Sum |[py](code/1.py) | HashMap , Sorted Two Pointer
|11	Container With Most Water |[py](code/11.py) | if left < right : left++ <br> elif right < left: right-- 
|42 Trapping Rain Water |[py](code/42.py)| arr : 1 2 3 <br> left : 1 2 3 <br> right : 3 3 3  | if height[i] < height[j]: left ++ <br> else right--
|15 3Sum || sorted, for i, while j < k
|454 4Sum II || hashmap = A+B, 2 for loop C+D similar to 2Sum
|287 Find the Duplicate Number ||slow = 0, fast = 0, t = 0 | slow = nums[slow], fast = nums[nums[fast]]
|325 Maximum Size Subarray Sum Equals k | |  best = max(best,i - dic[summ-k])

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
|658 Find K Closest Elements |[cpp](code/658.cpp)| if (x - arr[mid] > arr[mid + k] - x) left = mid + 1 <br> else: right = mid | right = len(arr) - l , last valid start point

## Binary Tree
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|298	Binary Tree Longest Consecutive Sequence |[py](code/298.py) | if root.val == expect: <br> curLen+1 <br> else: <br> curLen = 1 <br> dfs(root.left,expect+1,curLen) <br> | max on self means seq
|236 Lowest Common Ancestor of a Binary Tree |[py](code/236.py)| p dict, q dict and set | if p or q: return <br> if left and right: return root
|235 Lowest Common Ancestor of a Binary Search Tree || search the tree base on p.val q.val <br> move left or right base on condition
|98 Validate Binary Search Tree || pass limit on child nodes
|315 Count of Smaller Numbers After Self || Longest Increasing Subsequence (reverse) , size = len(tail)
|617 Merge Two Binary Trees || if not t1: return t2
|663 Equal Tree Partition || get sum of each node <br> total / 2.0 in seen
|545 Boundary of Binary Tree || leftBoundary,rightBoundary,leaves
|662 Maximum Width of Binary Tree || left : right * 2 <br> right: right * 2 + 1 <br> idx - level[h] + 1
|124 Binary Tree Maximum Path Sum || left = max(helper(node., res), 0) <br> right = max(helper(node.right, res), 0) <br> max(res,left + right + root.val)
|105 Construct Binary Tree from Preorder and Inorder Traversal || pLeft + i - iLeft
|543 Diameter of Binary Tree | | self.diameter = max(self.diameter,left+right)
|652 Find Duplicate Subtrees || post order + hashmap
|114 Flatten Binary Tree to Linked List || post order, set right to prev
|285 Inorder Successor in BST || Iterative inorder
|230 Kth Smallest Element in a BST || k-- | second minmium, first, second = max 

## BFS
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|675 Cut Off Trees for Golf Event |[py](code/675.py) | PQ + BFS
|127 Word Ladder |[py](code/127.py)| BFS to replace each word <br> remove word when seen
|785 Is Graph Bipartite |[cpp](code/785.py) | init color, if negibor is same color return false <br> else set negibor to diff color 
|
## DFS
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|200 Number of Islands | [py](code/200.py) | For each position <br> dfs 4 directions <br> change 0 to 1 | 
|529 Minesweeper || dfs count num of near mine <br> if 0: search 4 way <else> stop and mark num
|508 Most Frequent Subtree Sum || post order + hash
|606 Construct String from Binary Tree| | preorder <br> catch : str(t.val) + '(' + self.tree2str(t.left)  + ')'
|733 Flood Fill || dfs on same color replace to new
|261 Graph Valid Tree || dfs with parent | if parent continue, find cycle and len(visited) == n  
  
## Backtacking
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|17 Letter Combinations of a Phone Number |  | for ele in dict[index] | 
|282 Expression Add Operators |[py](code/282.py)| for i in range(idx,len(num)): <br> val = num[idx:i+1] | string partition <br> abc -> a -> b -> c <br> a -> bc <br> ab -> c <br> abc
|40 Combination Sum II | |dfs(i+1) <br> if i != start && num[i] == num[i - 1]: continue 
|377 Combination Sum IV || for n in nums: summ += self.dfs(nums,target-n,dp) <br> dp[target] = summ <br>  target is the identity of current status | return 0 or 1 
|47 Permutations II|[py](code/529.py)|if i > 0 and nums[i-1] == nums[i] and not visited[i-1] == 0: continue
|78 Subsets || same as combination

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
|739 Daily Temperatures | | Descending Stack <br> while (!st.empty() && temperatures[i] > temperatures[st.top()]) | t = s.pop(0)<br>res[t] = i - t

## Greedy
| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|252 Meeting Rooms | | sort, check false
|253 Meeting Rooms II || sort, pq ,if (!q.empty() && q.top() <= a.start) q.pop()
|56 Merge Intervals || res[-1].end >= intervals[i].start <br> res[-1].end = max(res[-1].end,intervals[i].end)
|57 Insert Interval |[py](code/57.py)| insert to newInterval.start < intervals[i].start, then do merge intervals
