
class MaxHeap:
    def buildMaxHeap(self, lst:list):
        if not lst:
            return
        self.heapSize = len(lst)
        self.heap = lst
        self.heap.insert(0,0) #堆下标从 1 开始记，用 0 占位
        for i in range(self.heapSize // 2, 0, -1):
            self.maxHeapify(i)


    def maxHeapify(self, i:int):
        l = self.left(i)
        r = self.right(i)
        if l < self.heapSize and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i

        if r < self.heapSize and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def heapMaxNum(self):
        return self.heap[1]

    def heapExtractMax(self):
        if self.heapSize < 1:
            print('堆为空')
            return
        max = self.heap[1]
        self.heap[1] = self.heap[self.heapSize-1]
        del self.heap[self.heapSize-1]
        self.maxHeapify(1)
        self.heapSize -= 1
        return max

    def heapIncreaseKey(self, i:int, key:int):
        if key < self.heap[i]:
            print('新key比原key还小，错误')
            return
        self.heap[i] = key
        while i > 1 and self.heap[self.parrent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parrent(i)] = self.heap[self.parrent(i)], self.heap[i]
            i = self.parrent(i)

    def heapInsert(self, key):
        self.heapSize += 1
        self.heap[self.heapSize - 1] = float('-inf')
        self.heapIncreaseKey(self.heapSize-1, key)

    def heapDelete(self, i):
        if i < 1 or i > self.heapSize-1:
            print('删除下标有误')
            return False

        if i < self.heapSize // 2:  # i 是 非叶子节点
            # 这个 while 是为了获取以 i 为 根 的子树的最大下标
            largest = 0

            while largest < self.heapSize :
                if self.left(i) >= self.heapSize:
                    break
                if self.left(i) < self.heapSize:
                    l1 = self.left(i)
                if self.right(i) < self.heapSize:
                    r1 = self.right(i)
                if self.left(l1) < self.heapSize:
                    largest = l1
                if self.left(r1) < self.heapSize:
                    largest = r1


            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            del self.heap[largest]
            self.heapSize -= 1
            self.maxHeapify(i)
        else:  # i 是 叶子节点
            for j in range(i, self.heapSize-1):
                self.heap[j] = self.heap[j+1]
            del self.heap[self.heapSize-1]
            self.heapSize -= 1





    def parrent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

lst = [16,10,8,9,14,4,2,1,7,3]
h = MaxHeap()
h.buildMaxHeap(lst)
max1 = h.heapExtractMax()
max2 = h.heapExtractMax()
max3 = h.heapMaxNum()
print(max1,max2,max3,'siez=',h.heapSize)
print(h.heap)

h.heapInsert(5)
print(h.heap)
h.heapIncreaseKey(2,20)
print(h.heap,len(h.heap))
h.heapDelete(2)
print(h.heap,len(h.heap))
# print(h.getMaxSub(2))
