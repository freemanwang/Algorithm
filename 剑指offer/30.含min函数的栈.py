class Stack:
    def __init__(self):
        self.min = 99999
        self.mstack = []
        self.stack = []

    def push(self, num):
        self.stack.append(num)
        if num < self.min:
            self.min = num
            # print(self.min)
        self.mstack.append(self.min)

    def pop(self):
        self.mstack.pop()
        return self.stack.pop()

    def getMin(self):
        lastIndex = len(self.mstack) - 1
        return self.mstack[lastIndex]


st = Stack()
st.push(3)
st.push(4)
st.push(2)
st.push(1)
print(st.mstack)
print(st.stack)
print(st.pop())
print(st.pop())
print(st.getMin())
print(st.mstack)
print(st.stack)