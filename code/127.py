class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        if not wordList:
            return 0
        
        aplha = 'abcdefghijklmnopqrstuvwxyz'
        
        q = [beginWord]
        
        wordList = set(wordList)
        
        step = 0

        
        while q != []:
            
            step += 1
            
            for _ in range(len(q)):
                
                wordString = q.pop(0)
                
                word = list(wordString)
                
                for i in range(len(word)):
                    
                    for c in aplha:
                        word[i] = c
                        
                        tmp = ''.join(word)

                        if tmp == endWord:
                            return step + 1

                        if tmp not in wordList:
                            continue

                        wordList.remove(tmp)
                        q.append(tmp)
                    
                    word = list(wordString)
                
        return 0
                    
                
                
                
