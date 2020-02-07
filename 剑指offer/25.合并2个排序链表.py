from Chain import *
lst1 = [1,3,5,7]
lst2 = [2,4,6,8]
ch1 = createChain(lst1)
ch2 = createChain(lst2)
printChain(ch1)
printChain(ch2)
def mergeChain(node1,node2):
    '''
    按大小合并2个链，较小者在前
    :param node1: 链1的第一个数据节点
    :param node2: 链2的第一个数据节点
    :return: 合并链的第一个数据节点
    '''
    # node1,node2只要不是全非空，就返回。因为哪怕就1个空，都没什么好合并的
    if not node1:
        return node2
    if not node2:
        return node1
    # 任何一个不是节点，退出
    if not isinstance(node1, Node) or not isinstance(node2, Node):
        return
    if node1.data <= node2.data:
        mergeHead = node1
        mergeHead.next = mergeChain(node1.next, node2)
    else:
        mergeHead = node2
        mergeHead.next = mergeChain(node1, node2.next)
    print('合并完成')
    return mergeHead

mc = mergeChain(ch1.next,ch2.next)
printChain(mc)