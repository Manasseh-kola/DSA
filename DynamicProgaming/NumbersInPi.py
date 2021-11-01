"""
Given a string representation of the first n digits of Pi and a list of positive integers (all in string format), write a function that returns
the smallest number of spaces that can be added to the n digits of Pi such that all resulting numbers are found in the list of
integers.Note that a single number can appear multiple times in the resulting numbers. For example, if Pi is "3141" and the numbers
are ["1", "3", "4"] , the number "1" is allowed to appear twice in the list of resulting numbers after three spaces are
added: "3 | 1 | 4 | 1" . If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function should return -1 .

Sample Input
pi = "3141592653589793238462643383279
numbers = ["314159265358979323846", "26433", "8",  "3279", "314159265", "35897932384626433832", "79"]

Sample Ouput

2 // "314159265 | 35897932384626433832 | 79


"""

def numbersInPi(pi, numbers):
    piSet = set(numbers)
    setLength = {len(num) for num in numbers}
    spaces = minSpaces(piSet,pi,0,len(pi),setLength,{})

    return -1 if spaces == float("inf") else spaces
	
def minSpaces(piSet,pi,start,end,setLength,memo):
    if start == len(pi):
      return -1

    if start in memo:
      return memo[start]

    minChild = float("inf")
    for i in range(start,end):
      currLength = i-start+1
      if currLength not in setLength:
        continue
      currString = pi[start:i+1]
      if currString in piSet:
        child = minSpaces(piSet,pi,i+1,end,setLength,memo)
        minChild = min(minChild,child+1)
    memo[start] = minChild
    return minChild
