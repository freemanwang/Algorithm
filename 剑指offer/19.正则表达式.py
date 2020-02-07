import re
string = 'I am angry! I am happy!'
pattern = 'am'
res = re.match(pattern,string,re.I)
print(res)