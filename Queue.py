class Queue :
    Front = Rear = -1
    def __init__(self,value):
        self.value = value
        self.Array = [0] * self.value
        self.Reverse = [0] * self.value

    def EnQueue(self, item):
        if self.Rear != self.value-1 : # Checking Queue is Full
            self.Array[self.Rear+1] = item
            self.Rear += 1
            print("Front is:", self.Front, "and", "Rear is:", self.Rear)
            return self.Array
        else :
            return "Queue is full!"


    def DeQueue(self):
        if self.Rear != self.Front : # Checking Queue is Empty
            self.Array[self.Front+1] = 0
            self.Front += 1
            print("Front is:", self.Front , "and" ,"Rear is:", self.Rear )
            return self.Array

        else :
            return "Queue is empty"

    def ReverseQueue(self):
        self.Counter = 0
        for i in range (self.Rear,-1,-1) :
            self.Reverse[self.Counter] = self.Array[i]
            self.Counter += 1
        return self.Reverse



    def Peek(self):
        return self.Array[self.Front+1]


    def IsEmpty(self):
        if self.Rear == self.Front :
            return True
        else:
            return False


    def IsFull(self):
        if self.Rear == self.item-1 :
            return True
        else:
            return False


#-----------------------------------------------------------------------------------------------------------------------


size = int(input())

q = Queue(size)

print("\n")

print(q.EnQueue(1),"\n")
print(q.EnQueue(2),"\n")
print(q.EnQueue(3),"\n")
print(q.EnQueue(4),"\n")
print(q.EnQueue(5),"\n")
print(q.EnQueue(6),"\n")

print(q.ReverseQueue(),"\n")

# print(q.EnQueue(7),"\n")
# print(q.EnQueue(8),"\n")
# print(q.EnQueue(9),"\n")
# print(q.EnQueue(10),"\n")
# print(q.EnQueue(11),"\n")
#
# print("\n")
#
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
#
#
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# print(q.DeQueue(),"\n")
# # print(q.DeQueue(),"\n")
#
# print(q.EnQueue(11),"\n")

