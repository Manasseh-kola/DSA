"""
Write a function that takes in a list of nonempty strings and returns a list of all the special strings found in the input list.
A string is said to be special if it's exactly made up of at least two instances of other strings in the input list of strings.
In order for a string to be special, just containing two instances of other strings isn't sufficient; the string must be exactly
made up of those other strings. For example, in the list ["a", "b", "abc"] , the string "abc" isn't special, even though it contains
"a" and "b" , because "c" isn't a string in the list.
Note that strings can be repeated to form a special string; for instance, in the list ["a", "aaa"], the string "aaa" is a
special string because it's made up of three repeated instances of "a" .

Also note that you can't use language-built-in string-matching methods.

Sample Input
strings = [
 "foobarbaz",
 "foo",
 "bar",
 "foobarfoo",
 "baz",
 "foobaz",
 "foofoofoo",
 "foobazar",
]

"""

class Trie:
	def __init__(self):
		self.root = {}
		self.end = "*"
		
	def insert(self,word : str) -> None:
      node = self.root
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node[self.end] = True
		
def specialStrings(strings):
    trie = Trie()
    specialString = []
    for s in strings:
      trie.insert(s)

    index = [1]

    for s in strings:
      if search(trie.root,0,s,trie,0) >=2:
        specialString.append(s)

    return specialString
		
def search(node,index,word,trie,count):
    if word[index] not in node:
      return -len(word)

    if index == len(word)-1:
      if trie.end in node[word[index]]:
        count +=1
      return count

    if trie.end in node[word[index]]:
      count +=1
      count2 = search(trie.root,index+1,word,trie,0)
      if count2 > 0:
        count+=count2
        return count

    return search(node[word[index]],index+1,word,trie,0)

	
	

	
    
