class Stack:
  def __init__(self):
      self._items = []

  def is_empty(self):
      return not bool(self._items)

  def push(self, item):
      self._items.append(item)

  def pop(self):
      return self._items.pop()

  def peek(self):
      return self._items[-1]

  def size(self):
      return len(self._items)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))


#output
#3.0
