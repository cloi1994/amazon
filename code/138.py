# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        hm = {}
        
        cur = head
        
        root = newCur = RandomListNode(1)
        
        while cur:
            newNode = RandomListNode(cur.label)
            newCur.next = newNode
            
            hm[cur] = newNode
            
            cur = cur.next
            newCur = newCur.next
            
        cur = head
            
        while cur:
            if cur.random != None:
                hm[cur].random = hm[cur.random]
            cur = cur.next
            
        return root.next
            
            
            
