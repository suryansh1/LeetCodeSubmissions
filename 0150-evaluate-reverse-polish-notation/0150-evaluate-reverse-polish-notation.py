from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1 : return int(tokens[0])

        stack = deque()

        operators = set(['+', '-', '*', '/'])
        
        for token in tokens :

            if token not in operators : 

                stack.append(token)
                continue
            
            operand2 = stack.pop()

            operand1 = stack.pop()

            # Evaluate operand1 'token' operand2

            # if token == '/' : token = '//'

            expr = str(operand1) + ' ' + str(token) + ' ' + str(operand2)

            stack.append(int(eval(expr)))

        return stack.pop()


            
