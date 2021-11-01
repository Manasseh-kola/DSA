"""
Number of ways to traverse a rectangulat grid.
Operations allowed:
  Move to the right
  Move down
"""

def numberOfWaysToTraverseGraph(width, height):
    if height ==1:
      return 1
    if height ==2:
      return width

    additionalHeight = width -2
    height = height +additionalHeight

    prev = 1
    for i in range(1,height+1):
      curr = (prev*(height-i+1))//i
      if i == width-1:
        return curr
      prev = curr
		
