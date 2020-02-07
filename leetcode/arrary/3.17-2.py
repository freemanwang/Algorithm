class Solution:
    def letterCombinations(self, digits):
        letter = []
        for x in digits:
            if x=='2':
                letter.append(['a','b','c'])
            elif x=='3':
                letter.append(['d','e','f'])
            elif x=='4':
                letter.append(['g','h','i'])
            elif x=='5':
                letter.append(['j','k','l'])
            elif x=='6':
                letter.append(['m','n','o'])
            elif x=='7':
                letter.append(['p','q','r','s'])
            elif x=='8':
                letter.append(['t','u','v'])
            else:
                letter.append(['w','x','y','z'])
        for i in range(1, len(letter)):
            print(letter)
            temp = letter[0][:]
            for x in temp:
                for y in letter[i]:
                    letter[0].append(str(x+y))
                del letter[0][0]
        if digits == "":
            return []
        else:
            return letter[0]

c = Solution()
t = '234'
arr = c.letterCombinations(t)
print(len(arr),arr)