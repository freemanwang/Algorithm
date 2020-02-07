string = 'I am a student.'
lst1 = string.split(' ')
start = 0
end = len(lst1)-1
while start < end:
    lst1[start], lst1[end] = lst1[end], lst1[start]
    end -= 1
    start += 1

#     注意，list拼接成str时， 语法是   "拼接符".join(list),和js的arr.join('拼接符') 完全不一样
str1 = ' '.join(lst1)
print(str1)