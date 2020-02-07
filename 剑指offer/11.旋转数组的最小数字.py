#找出旋转数组中最小的数字
# def findMin(lst:list):
#     pre = 0
#     next = len(lst)-1
#     mid = pre
#     while lst[pre] >= lst[next]:
#         if (next - pre) == 1:
#             mid = next
#             break
#         mid = int((pre + next) / 2)
#         print(mid)
#         if lst[pre] <= lst[mid]:
#             pre = mid
#         elif lst[next] >= lst[mid]:
#             next = mid
#         return lst[mid]

def minNumberInRotateArray( rotateArray):
    # write code here
    if not rotateArray:
        return
    if len(rotateArray) == 0:
        return 0
    index1 = 0
    index2 = len(rotateArray)-1
    indexMid = index1
    while (rotateArray[index1]>=rotateArray[index2]):
        if (index2-index1) == 1:
            indexMid = index2
            break
        indexMid = (index1+index2)//2
        # 如果index1 index2 indexMid三者相等
        if rotateArray[index1] == rotateArray[index2] and rotateArray[indexMid] == rotateArray[index1]:
            return minValue(rotateArray,index1,index2)

        if rotateArray[indexMid] >= rotateArray[index1]:
            index1 = indexMid
        if rotateArray[indexMid] <= rotateArray[index2]:
            index2 = indexMid

    return rotateArray[indexMid]

def minValue(rotateArray,index1,index2):
    res = rotateArray[index1]
    for i in range(index1+1,index2+1):
        if res > rotateArray[i]:
            res = rotateArray[i]
    return res


lst = [3,4,5,1,2]
min = minNumberInRotateArray(lst)
print(min)