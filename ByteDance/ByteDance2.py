#给一个网址，www.baidu.com,输出com.baidu.www
str1 = 'www.baidu.com'
arr = str1.split('.')
arr.reverse()
print(arr)
out = '.'.join(arr)
print(out)