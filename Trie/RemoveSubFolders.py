"""
LeetCode
1233. Remove Sub-Folders from the Filesystem

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
If a folder[i] is located within another folder[j], it is called a sub-folder of it.
The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
"""

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
        
    def insert(self,word:str)->None:
        node = self.root
        for w in word:
            if w == "/":
                continue
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.end] = True
     
        
    def search(self,word:list)-> bool:
        stack = [(self.root,0)]
        while len(stack):
            node,index = stack.pop()
            if index+1 < len(word):
                if self.end in node[word[index]]:
                    return True
            if index+1 < len(word):
                stack.append((node[word[index]],index+1))
        return False
    

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        trie = Trie()
        folder2 = []
        for i,path in enumerate(folder):
            newPath  = path.replace("/"," ").split()
            folder2.append(newPath)
            trie.insert(newPath)
        
   
        subFolders = set()
        for i,path in enumerate(folder2):
            isSub = trie.search(path)
            if isSub:
                subFolders.add(i)
        rootFolders = []
        for i,path in enumerate(folder):
            if i not in subFolders:
                rootFolders.append(path)
                
        return rootFolders
        
        
