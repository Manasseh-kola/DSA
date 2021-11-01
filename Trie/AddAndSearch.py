"""
LeetCode
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
  WordDictionary() Initializes the object.
  void addWord(word) Adds word to the data structure, it can be matched later.
  bool search(word) Returns true if there is any string in the data structure that matches
  word or false otherwise. word may contain dots '.' where dots can be matched with any letter
  
  
Input
  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
  Output
  [null,null,null,null,false,true,true,true]

Explanation
  WordDictionary wordDictionary = new WordDictionary();
  wordDictionary.addWord("bad");
  wordDictionary.addWord("dad");
  wordDictionary.addWord("mad");
  wordDictionary.search("pad"); // return False
  wordDictionary.search("bad"); // return True
  wordDictionary.search(".ad"); // return True
  wordDictionary.search("b.."); // return True
"""

class WordDictionary:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.end] = True

    def search(self, word: str) -> bool:
   
        queue = deque([(self.root,0)])
        if word[0] not in self.root and word[0] != ".":
            return False
  
        while len(queue):
            node,i = queue.popleft()
            if i+1> len(word):
                continue
            w = word[i]

            if w == ".":
                for an in node:
                    if node[an] !=True:
                        if i == len(word)-1:
                            if self.end in node[an]:
                                return True
                        queue.append((node[an],i+1))
            if w in node:
                if self.end in node[w] and i == len(word)-1:
                    return True
                queue.append((node[w],i+1))
                
        return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

