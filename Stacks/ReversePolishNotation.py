"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, 
and there will not be any division by zero operation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
    
        stack = []
        for token in tokens:
            if token not in operations :
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                lastNum = operations[token](a,b)
                stack.append(lastNum) 
        return stack[0]
       
  
    
