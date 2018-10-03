class Solution:

    def longestConsecutive(root):
        if not root: 
          return 0
        self.res = 0
        dfs(root, root.val, 0)
        return res
    
    void dfs(root, prevVal, curLen):
        if not root:
          return;
        if root.val == prevVal + 1:
          curLen += 1
        else 
          curLen = 1
          
        self.res = max(self.res, curLen);
        dfs(root.left, root.val, curLen)
        dfs(root.right, root.val, curLen)
