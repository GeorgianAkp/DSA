import ctypes

class dynamicArray :

    def __init__(self):
        self.n = 0 
        self.capacity = 1 
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __get_item__(self,k):
        if 0 > k or k >= self.n :
            raise IndexError("Index out of bounds")
        return self.arr[k]

    def append(self,num):
        if self.n == self.capacity :
            self._resize(2*self.capacity)      #doubled the capacity on capacity and size are matching 

        self.arr[self.n] = num
        self.n += 1  
        return self.arr

    def _resize(self,new_cap):
        '''
        1. Create a new Array temp with new_cap size 
        2. Store all elements of arr in temp 
        3. Reset the capacity 
        '''
        temp = self.make_array(new_cap)
        for num in range(self.n):
            temp[num] = self.arr[num]
        self.arr = temp 
        self.capacity = new_cap

    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()
    
    def print_array(self):
        for num in self.arr :
            print(num)

array = dynamicArray()
array.append(1)
array.append(2)
array.print_array() 

