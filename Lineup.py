# Mehdi Torabi DS_pr1
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size 
        self.Q = [0] * max_size 
        self.num = 0
        self.first = 0
    

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise IndexError("Queue overflow")
        
        self.Q[(self.num + self.first) % self.max_size] = item 
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        
        item = self.Q[self.first]
        self.Q[self.first] = 0
        self.first = (self.first + 1) % self.max_size 
        self.num -= 1
        return item
    
    def front(self):
        if self.is_empty():
            raise Exception("Queue empty") 
        return self.Q[self.first]

    def is_empty(self): 
        return self.num == 0

    def size(self): 

        return self.num
        

    def is_full(self):
        return self.num >= self.max_size
    
    def index(self, ind):
        
        if 0 <= ind <= self.size():
            return self.Q[ind]
        else:
            print('index is out of the range')
def main():
        
    q = Queue(int(input('please enter your queue Length: '))) 
    q.enqueue("ra'na") 
    q.enqueue("vez") 
    q.enqueue("Arya") 
    print("queue size is: ",q.size())
    print(q.dequeue(), "left the queue") 
    print("front of queue is:",q.front()) 
    q.enqueue("milda") 

    ind = int(input('enter your item you want: '))
    print(q.index(ind))
    

if __name__ == '__main__':
    main()