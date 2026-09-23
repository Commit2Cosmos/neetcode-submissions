class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix_stack) == 0:
            self.prefix_stack.append(val)
        else:
            self.prefix_stack.append(min(val, self.prefix_stack[-1]))

        return

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_stack[-1]
