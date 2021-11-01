"""
LeetCode
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. 
For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. 
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
"""

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
        
    def insert(self,word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.end] = word
        
    def search(self,word:str) -> str:
        stack = [(self.root,0)]
        
        while len(stack):
            node,idx = stack.pop()
            if idx == len(word)-1:
                return word
            if word[idx] not in node:
                return word
            currNode = node[word[idx]]
            if self.end in currNode:
                return currNode[self.end]
            stack.append((currNode,idx+1))
            
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        sentenceArr = sentence.split(" ")
        
        for i,word in enumerate(sentenceArr):
            if word[0] not in trie.root:
                continue
            sentenceArr[i] = trie.search(word)
            
        return " ".join(sentenceArr)
