def maxCuttingSolution(length:int):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = list(0 for i in range(length+1))
    # products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    print(products)
    max = 0
    for i in range(4, length+1):
        max = 0
        for j in range(1, (i//2)+1):
            # print(j)
            product = products[j]*products[i-j]
            if max < product:
                max = product
            products[i] = max

    max = products[length]
    print(products)
    return max

max = maxCuttingSolution(7)  #测试多个，正常
print(max)