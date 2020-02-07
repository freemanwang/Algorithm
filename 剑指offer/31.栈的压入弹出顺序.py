push = [1, 2, 3, 4, 5]
out1 = [4, 5, 3, 2, 1]
out2 = [4, 3, 5, 1, 2]


def isPopOrder(push, pop):
    if not push or not pop:
        return False
    if len(push) == 1 and len(pop) == 1 and push[0] != pop[0]:
        return False
    stack = []
    # 逆序，然后从后开始操作
    push.reverse()
    pop.reverse()
    # push 和 pop长>=2
    stack.append(push[len(push) - 1])
    push.pop()
    while True:
        if stack[len(stack) - 1] != pop[len(pop) - 1]:
            stack.append(push[len(push) - 1])
            push.pop()
        if stack[len(stack) - 1] == pop[len(pop) - 1]:
            stack.pop()
            pop.pop()
        # 全空则证明可以按序pop完
        if not push and not pop and not stack:
            return True
        # push已全进栈，但出栈顺序不匹配，那出栈顺序有问题
        if not push and stack[len(stack) - 1] != pop[len(pop) - 1]:
            return False


print(isPopOrder(push, out1))