'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
'''

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        # for i in range(len(self.queue1)-1):
        while len(self.queue1) > 1:
            a = self.queue1.popleft()
            self.queue2.append(a)
        popped_val = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_val

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_value = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_value
        

    def empty(self) -> bool:
        return (len(self.queue1) == 0)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()