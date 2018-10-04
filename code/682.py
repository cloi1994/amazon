class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        v = []
        
        for op in ops:
            if op == '+':
                if len(v) >= 2:
                    v.append(v[-1] + v[-2])
            elif op == 'D':
                if v != []:
                    v.append(2 * v[-1])
            elif op == 'C':
                if v != []:
                    v.pop()
            else:
                v.append(int(op))
                
        return sum(v)
