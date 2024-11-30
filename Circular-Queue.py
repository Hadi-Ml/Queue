class Queue :
    Front = Rear = -1
    def __init__(self,value):
        self.value = value
        self.Array = [0] * self.value
        self.Reverse = [0] * self.value

    def EnQueue(self, item):
        if self.Front != (self.Rear + 1) % self.value : # Checking Queue is Full
            if self.Rear == self.value - 1 :
                self.Rear = 0
                self.Array[self.Rear] = item
                print("Front is:", self.Front, "and", "Rear is:", self.Rear)
                return self.Array
            else :
                self.Array[self.Rear+1] = item
                self.Rear += 1
                print("Front is:", self.Front, "and", "Rear is:", self.Rear)
                return self.Array
        else :
            return "Queue is full!"


    def DeQueue(self):
        if self.Rear != self.Front : # Checking Queue is Empty
            if self.Front == self.value - 1 :
                self.Front = -1
            else :
                self.Array[self.Front+1] = 0
                self.Front += 1
                print("Front is:", self.Front , "and" ,"Rear is:", self.Rear )
                return self.Array

        else :
            return "Queue is empty"


    def Peek(self):
        return self.Array[self.Front+1]


    def ReverseQueue(self):
        self.Counter = 0
        for i in range(self.Rear,self.Front,-1):
            self.Reverse[self.Counter] = self.Array[i]
            self.Counter += 1
        return self.Reverse


    def IsEmpty(self):
        if self.Front == self.Rear :
            return True
        else :
            return False


    def IsFull(self):
        if self.Front != (self.Rear + 1) % self.value :
            return True
        else :
            return False


#-----------------------------------------------------------------------------------------------------------------------


size = int(input())

q = Queue(size)

print("\n")

print(q.EnQueue(40),"\n")
print(q.EnQueue(50),"\n")
print(q.EnQueue(30),"\n")
print(q.EnQueue(80),"\n")

print(q.ReverseQueue(),"\n")


print(q.DeQueue(),"\n")
print(q.DeQueue(),"\n")

print(q.EnQueue(20),"\n")
print(q.EnQueue(100),"\n")
