#不可变数据类型直接 = 赋值，可变，或者说引用类型，就递归deepcopy，dict的话特殊，专门dictcopy
def deepcopy(data):
    listdata = []
    if isinstance(data,int) or isinstance(data,float) or isinstance(data,str) or isinstance(data,bool):
        return data
    if data:
        for item in data:
            # 如果是dict型，调用字典复制函数
            if isinstance(item,dict):
                dictData = dictcopy(item)
                listdata.append(dictData)
            #     list和tuple，递归本身
            elif isinstance(item,list) or isinstance(item,tuple):
                tmpData = deepcopy(item)
                listdata.append(tmpData)
            #     不可变的基本类型，直接赋值即可
            else :
                listdata.append(item)
    # 长为1或0，要么空要么基础数据
    else:
        return data
    return listdata

def dictcopy(data):
    dict1 = {}
    # 复制逻辑和deepcopy一致，非dict就用deepcopy，dict就dictcopy
    for key,value in data.items():
        # 如果值是字典，那就字典复制函数
        if isinstance(value,dict):
            tmpdict = dictcopy(value)
            dict1[key] = tmpdict
        else:
            value = deepcopy(value)
            dict1[key] = value
    return dict1


alice = [
        'name',
        18,
        True,
        ['piano', 'fishing', 100],
        {'class':1,'grade':'6'}
    ]
print(alice)
bob = deepcopy(alice)   #深拷贝，不会被alice的变化改变
a2 = alice  #引用类型，会跟着alice变
alice[2] = 99
print(a2)
print(bob)


