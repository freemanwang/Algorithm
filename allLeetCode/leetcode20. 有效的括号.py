class Solution(object):
    def isValid(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        # 单数数量肯定对不上
        if len(s) % 2 ==1:
            return False
        if not s:
            return True
        s = list(s)
        tmpLst = []
        while len(s) > 0:
            tmp = s.pop()
            if tmp==')' or tmp=='}' or tmp==']':
                tmpLst.insert(0,tmp)
            elif (tmp=='(' or tmp=='{' or tmp=='[' ) and len(tmpLst) > 0:
                if tmp == '(' and tmpLst[0] == ')':
                    tmpLst.pop(0)
                    continue
                elif tmp == '{' and tmpLst[0] == '}':
                    tmpLst.pop(0)
                    continue
                elif tmp == '[' and tmpLst[0] == ']':
                    tmpLst.pop(0)
                    continue
                else:
                    return False
            else:# 弹出符号是左侧符号，且 tmpLst 为空没有可匹配的
                return False

        if len(s) == 0:
            # print('last')
            return True

    def isValid2(self, s:str):
    # 大牛代码,注意他是从左到右检索，我自己代码是从右往左检索
        stack = []
        match_map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in match_map:  #不在的话，那就是 左侧符号 (   [   {
                stack.append(c)
            # 当前符号是右侧的 )  ]  }  符号，且栈为空（无可匹配）或匹配不上
            elif not stack or match_map[c] != stack.pop():
                return False
        return not stack
c = Solution()
s = "([)]"
print(len(s))
res = c.isValid2(s)
print(res)

s1 = 'ABC'
s1 = list(s1)
print(s1.pop())