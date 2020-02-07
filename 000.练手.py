# # 字典的key可以是任意不可变对象，但一般用str
# d = {}
# # 添加直接 d[key]=value即可
# d['name'] = 'alice'
# d['age']= 20
# d[50] = 50
# print(d)
# del d[50]  #del 删除，del 不存在的元素会报错
# print(d)
# popitem = d.popitem()
# print(popitem)  #('age', 20),popitem一般删最后一个
# print(d)            #('age', 20)
# pop1 = d.pop('name')  # 删除key对象值，返回value；若key不存在，报错
# pop2 = d.pop('name','无该key-value存在')  #pop的第2个参数，是key不存在时返回的值，不报错。
# print(pop1)  #alice
# print(pop2)  #无该key-value存在
# print(d)   #{}  已经空了
# d.update({'gender':'female','bool':'false'}) #插入新dict入d
# print(d)
# print(d.get(80))  #不存在的键不会报错，只是返回None
# # print(d[80])    #这样就抛出异常。所以不确定key是否有，就先用in检查，要么就用get(key)
# name = d.setdefault('name','Bob') #key存在就返回value，不存在就添加key-value，value=第二参数
# print(name,d['name']) #alice alice


# d1 = {"name":'bob',"age":19}
# d2 = {"name":'carol',"age":33, "gender":'male'}
# d1.update(d2)   #后添加的覆盖前面的
# print(d1)   #{'name': 'carol', 'age': 33, 'gender': 'male'}
#
# s = set()
# # s.add([1,2,3])   #TypeError: unhashable type: 'list'   只能存不可改变类型
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(1)
# s.add(2)
# s.add(3)
# print(s)
# s.remove(3)
# # s.remove(4)  #报错，remove不存在的报错
# s.discard(2)
# s.discard(4)   #diacard不存在的不报错
# print(s)
# s = set('hello')
# print(s)  #{'e', 'h', 'l', 'o'}
# # print(s[2]) #TypeError: 'set' object does not support indexing   set不能下标操作
# print(s.pop())  # l
# print(s)    #{'e', 'o', 'h'}
# #说pop 是随即删除，其实永远删除集合第一个元素；但集合排序并不是插入顺序，
# # 所以不知道集合排序的话那就是随机删除；
#

lst = [1,2,3,4,5]
print(lst.index(3))
s = "Helloworldagain"
print(s.index('l',4))
