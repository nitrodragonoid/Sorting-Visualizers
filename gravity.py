class Node:
    def __init__(self, val = None):
        self.val = val;
        self.next = None;
        
class abacus:
    def __init__(self,arr):
        highest = max(arr)
        self.head = list()
        for i in highest:
            self.head.append(None)
            
        for element in arr:
            for n in range(element):
                if self.head[n] == None:
                    self.head[n] = Node()
                else:
                    self.head[n].next = Node()
                    
    def sort(self):
        pass
                    
                    
                    
    
            
def pigeonhole_sort(arr):
    min_el = min(arr)
    max_el = max(arr)
    
    num_of_holes = max_el - min_el + 1
    pigeon_holes = [0] * num_of_holes
    
    for el in arr:
        pigeon_holes[el - min_el] += 1
        
    c = 0
    for i in range(num_of_holes):
        while pigeon_holes[i] > 0:
            pigeon_holes[i] -= 1
            arr[c] = i + min_el
            c+=1
    
    # print(sorted_arr)
    # arr = sorted_arr
    
    # print(arr)
        
              
 
a = [8, 3, 2, 7, 4, 6, 8]
 
print(a)
pigeonhole_sort(a)
print(a)
         
