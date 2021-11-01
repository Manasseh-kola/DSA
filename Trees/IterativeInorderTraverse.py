"""
Write a function that takes in a Binary Tree (where nodes have an additional pointer to
their parent node) and traverses it iteratively using the in-order tree-traversal technique;
the traversal should specifically not use recursion. As the tree is being traversed, a
callback function passed in as an argument to the main function should be called on each node (i.e., callback(currentNode)).
Each BinaryTree node has an integer value , a parent node, a left child node, and a right child node. Children nodes can either be BinaryTree nodes
themselves or None / null .

"""
def iterativeInOrderTraversal(tree, callback):

    stack =  [(tree,False,False)]

    while len(stack):
      currentInfo = stack[-1]
      currentNode,traversedLeft,traversedRight = currentInfo
      if currentNode is None:
        stack.pop()
      elif traversedLeft and traversedRight:
        stack.pop()
      elif not traversedLeft:
        nextNode = currentNode.left
        stack[-1] = (currentNode,True,traversedRight)
        stack.append((nextNode,False,False))
      elif not traversedRight:
        callback(currentNode)
        nextNode = currentNode.right
        stack[-1] = (currentNode,traversedLeft,True)
        stack.append((nextNode,False,False))
