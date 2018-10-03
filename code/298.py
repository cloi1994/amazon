class Solution:

    def longestConsecutive(root):
        if not root: 
          return 0
        self.res = 0
        dfs(root, root.val, 0)
        return res
    
    void dfs(root, int prevVal, int curLen):
        if not root:
          return;
        if root.val == prevVal + 1:
          curLen += 1
        else 
          curLen = 1
          
        self.res = max(self.res, out);
        dfs(root.left, root.val, out, res)
        dfs(root.right, root.val, out, res)
