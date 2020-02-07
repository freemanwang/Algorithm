list = [2,3,1,0,2,5,3]
import random
def getDup(list):
    if len(list) <= 1 or list == None:
        print('输入数据中不可能有重复数字')
        return
    list.sort()
   # print(list)  # 调试

    d = dict()
    multi = dict()

    for i in list:
        d.setdefault(i, 0)

   # print(d)  # 调试

    i = 0
    for i in list:
        key = i
        if key in d:
            d[key] += 1

    # print(d)    #调试

    for t in d.items():
        if t[1] > 1:
           # print(t)
            tmp = {t[0]: t[1]}  # 重复数字字典
            multi.update(tmp)  # 添加进字典

   # print(multi)  # 调试 {2: 2, 3: 2}  结果如预期
    if len(multi) >= 1:
        key = random.sample(multi.keys(), 1)
        #print(key,type(key[0]))
        times = multi.get(key[0])
        print(f'随机给出重复元素{key[0]}，出现了{times}次')
    else:
        ans = None
        print('没有重复的数字')

getDup(list)

l2 = [2,3,5,4,3,2,6,7]
getDup(l2)

l3 = [1,2,3,4,5,6]
getDup(l3)

l4 = []
getDup(l4)