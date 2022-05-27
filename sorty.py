import pygame  
import time
import random

grey = (155, 155, 155)
Red = (255,0,0) 
Blue = (0,0,255)  
empty = (50,50,50)
black = (0,0,0)  
white = (255,255,255)  

# lst = []

# for i in range(1,51):
#     lst.append(i)
    
# lst = [21,42,19,4,24,16,23,7,1,6,5,34,27,18,50,43,21,52,47,39,25,46,13,12,34,20,10,9,4,35,5,8,23]

lst = []
for i in range(70):
    lst.append(random.randint(1,70))

pygame.init()  
screen = pygame.display.set_mode((800, 700))  
done = False  

def insertionSort(arr):
     
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
  
  
c = 0

while not done:  
    
    pygame.draw.rect(screen, black, [0, 0, 800, 700])
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    color = white
    x = 30
    y = 700
    
    if c==0:
        for i in range(1, len(lst)):
            pygame.draw.rect(screen, black, [0, 0, 800, 700])
            time.sleep(0.1)
        
            key = lst[i]
            j = i-1
        
            while j >= 0 and key < lst[j] :
                pygame.draw.rect(screen, black, [0, 0, 800, 700])
                lst[j + 1] = lst[j]
                j -= 1
                for m in range(len(lst)):
                    for n in range(lst[m]):
                        if m == i or m == j:
                            pygame.draw.rect(screen, Red, [x+(10*m), y-(10*n), 10, 10]) 
                        else:
                            pygame.draw.rect(screen, color, [x+(10*m), y-(10*n), 10, 10]) 
                pygame.display.update() 
            lst[j + 1] = key
            pygame.display.update() 
            
            
        c+=1
    else:
        for m in range(len(lst)):
            for n in range(lst[m]):
                pygame.draw.rect(screen, color, [x+(10*m), y-(10*n), 10, 10]) 
              
    # pygame.display.update()       
    pygame.display.flip()  
