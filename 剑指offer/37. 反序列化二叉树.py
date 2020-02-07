from BinaryTree import Node,printTree
class Solution:
    def __init__(self):
        self.index = 0

    def deSerialize(self, s:str, ):
        if not s:
            return
        s = s.split(',')
        print(s)
        return self.deSerializeCore(s)

    def deSerializeCore(self, s:list):
        if s[self.index] == '$':
            self.index += 1
            return None
        node = Node(s[self.index])
        self.index += 1
        node.left = self.deSerializeCore(s)
        node.right = self.deSerializeCore(s)
        return node





s = "1,2,4,$,$,$,3,5,$,$,6,$,$"
c = Solution()
root = c.deSerialize(s)
printTree(root)
print(root.val)
