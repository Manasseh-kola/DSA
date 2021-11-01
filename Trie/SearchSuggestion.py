"""
LeetCode
1268. Search Suggestions System

Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""

class Trie:
    def __init__(self):
        self.root = {"suggest":[]}
        self.end = "*"
    def insert(self,word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {"suggest":[]}
            node = node[w]
            node["suggest"].append(word)
        node[self.end] = True
        
    def search(self,word:str) -> list:
        results = [[] for i in word]
        

        stack = [(self.root,0)]
        while len(stack):
            node,index = stack.pop()
            if index >= len(word):
                return results
            if word[index] in node:
                nextNode = node[word[index]]
                results[index] = nextNode["suggest"][0:3]
                stack.append((node[word[index]],index+1))
            else:
                break
        return results

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        suggestions = []
        
        return trie.search(searchWord)
            
        
