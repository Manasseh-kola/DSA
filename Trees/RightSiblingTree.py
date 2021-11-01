"""
Write a function that takes in a Binary Tree, transforms it into a Right Sibling Tree, and returns its root. A Right Sibling Tree is obtained by making
every node in a Binary Tree have its right property point to its right sibling instead of its right child. A node's right sibling is the
node immediately to its right on the same level or None / null if there is no node immediately to its right.

Note that once the transformation is complete, some nodes might no longer have a node pointing to them. For example, in the sample output below, the node with value
10 no longer has any inbound pointers and is effectively unreachable. The transformation should be done in place, meaning that the original data structure
should be mutated (no new structure should be created). Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null 

Sample Input
tree =    1
      /      \
     2        3
    / \       / \
   4   5     6   7
  / \   \   /   / \
  8 9   10 11  12 13
          /
         14
         
 Sample Output
   1
 /
 2-------------3
 /            /
 4-----5-----6-----7
 /          /     /
8---9 10-11 12-13 
         /
        14

"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    nodes = []
    queue = [(root,0)]

    while len(queue):
      currentNode,level = queue.pop(0)
      if level <= len(nodes)-1:
        nodes[level].append(currentNode)
      else:
        nodes.append([currentNode])
      if currentNode is not None:
        queue.append((currentNode.left,level+1))
        queue.append((currentNode.right,level+1))

    for i in range(len(nodes)):
      currentLevel = nodes[i]
      for j in range(len(currentLevel)):
        currentNode = currentLevel[j]
        if currentNode is not None:
          if j == len(currentLevel)-1:
            currentNode.right = None
          else:
            currentNode.right = currentLevel[j+1]	
    return root


