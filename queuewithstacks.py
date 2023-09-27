# 3 LINE SOLUTION EXPLAINING THE CODE
# LINE 1 : Created 2 stacks , stack1 for pushing , stack2 for popping
# LINE 2: Appended using stack1 , 0(1) operation , popped stack1 to append stack 2 FIFO amortized 0(1)
# LINE 3: For peek , if stack2 look at top element , else front element of stack 1 , both stacks need to be empty
class MyQueue :

  def __init__(self) -> None:
    self.stack_1 = []
    self.stack_2 = []
    self.front = None

  def push(self,x:int):  
    if not self.stack_1 :
      self.front = x
    self.stack_1.append(x)



  def pop(self):
    if not self.stack_2:
      while self.stack_1:
        self.stack_2.append(self.stack_1.pop())
    
    ans = self.stack_2.pop()
    return ans

  def peek(self):
    if self.stack_2 :
      return self.stack_2[-1]
    
    return self.front

  def empty(self):
    if not self.stack_2 and not self.stack_1:
      return True
    else :
      return False 



myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
popped_Value = myQueue.pop()
print("popped value is", popped_Value)
peek_Value = myQueue.peek()
print("peeked Value is", peek_Value)

