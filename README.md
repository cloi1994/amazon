

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



## Memo

| Title  | Solution  | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|4	Median of Two Sorted Arrays | [py](https://github.com/cloi1994/amazon/blob/master/code/4.py) | left = 0, right = n1 (no - 1) <br> cut1 = left + (right - left) // 2 <br> cut2 = (n1+n2) / 2 - cut1
|146	LRU Cache |[py](https://github.com/cloi1994/amazon/blob/master/code/146.py) | Hash + DLL
|13	Roman to Integer |[py](https://github.com/cloi1994/amazon/blob/master/code/13.py) | minus if num[cur-1] < num[cur]
 
## Stack


| Title  | Solution | S1 | S2
|-------------|:-----:| :-----: | :-----: |
|20	Valid Parentheses | | push if '(' <br> pop if ')' | counter++ if '(' <br> counter-- if '('
