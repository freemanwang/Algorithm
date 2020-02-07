class Queue(object):
    def __init__(self):
        self.queue = []
    def inQueue(self,data):
        self.queue.append(data)
    def outQueue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        else:
            return False
    def printQueue(self):
        if len(self.queue) > 0:
            for t in self.queue:
                print(t,end = '  ')
        else:
            return False
    def inFromSeq(self, seq):
        if not (isinstance(seq,list) or isinstance(seq,tuple)):
            print('error arguements!')
            return False
        for t in seq:
            self.inQueue(t)


que = Queue()
tup = (1,2,3,4,5,6)
que.inFromSeq(tup)
# que.printQueue()
que.inQueue('hello')
que.printQueue()
out = que.outQueue()
print(out) #ok的