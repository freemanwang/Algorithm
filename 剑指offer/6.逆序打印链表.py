from Chain import *
list = [1,2,3,4,5]
chain = createChain(list)
#print(chain,type(chain))
#print(chain.head,type(chain.head))
# chain.printList()

# @decoration
def reversePrint(chain):
    if chain:
        start = chain.head
        stack = [start]
    else:
        return
    while start.next != None:
        start = start.next
        stack.append(start)
    print('开始倒序打印链表数据')
    while len(stack) != 0:
        node = stack.pop()
        print(node.data,end = '  ')
    print('\n倒序链表打印完毕')
    return

# reversePrint(chain) #5  4  3  2  1
# lst = [12, 34, 567, 'abc', 'defg', 'hello']
# chain.initFromSeq(lst)
# reversePrint(chain)

#递归实现
# def reversePrintRecur(chain):
#     if not chain:
#         return
#     if chain.head == None:
#         return
#     start = chain.head
#     print('开始递归逆序打印')
#     def recur(head:Node):
#         if head.next != None:
#             recur(head.next)
#         print(head.data, end = ' | ')
#     recur(start)
#     print('打印结束')
#     return


# reversePrintRecur(chain)


