"""
Write a MinMaxStack class for a Min Max Stack. The class should support:
Pushing and popping values on and off the stack.
Peeking at the value at the top of the stack.
Getting both the minimum and the maximum values in the stack at any given point in time.

All class methods, when considered independently, should run in constant time and with constant space.

Sample Usage
// All operations below are performe
MinMaxStack(): - // instantiate a M
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5
"""

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
        self.stack = []
        self.minMax = []
    def peek(self):
        return self.stack[len(self.stack)-1]
            pass

    def pop(self):
        self.minMax.pop()
        return self.stack.pop()
            pass

    def push(self, number):
        self.stack.append(number)
        newMinMax = {"min":number,"max":number}
        if len(self.minMax):
          latestMinMax = self.minMax[len(self.minMax)-1]
          newMinMax["min"] = min(number,latestMinMax["min"])
          newMinMax["max"] = max(number,latestMinMax["max"])
        self.minMax.append(newMinMax)
            pass

    def getMin(self):
        return self.minMax[len(self.minMax)-1]["min"]
            pass

    def getMax(self):
        return self.minMax[len(self.minMax)-1]["max"]
            pass
