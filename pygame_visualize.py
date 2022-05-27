import pygame  
import sys
import math

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            special_colors = {len(arr)-i:GREEN}
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            special_colors[j] = RED
            special_colors[j+1] = RED
            yield special_colors
            # draw_loop(arr,index,special_colors)
    # yield {0:GREEN}
    yield {1:GREEN}
    yield {0:GREEN}
    # draw_loop(arr,index,{0:GREEN})


white = (255,255,255)  
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# lst = []

# for i in range(1,51):
#     lst.append(i)
WIDTH = 1280
HEIGHT = 720
PADDING_LEFT = 50
PADDING_RIGHT = 50
PADDING_TOP = 20
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
arr = [21,42,19,4,24,16,23,7,1,6,5,34,27,18,50,43,21,52,47,39,25,46,13,12,34,20,10,9,4,35,5,8,23]
    
lst = [21,42,19,4,24,16,23,7,1,6,5,34,27,18,50,43,21,52,47,39,25,46,13,12,34,20,10,9,4,35,5,8,23]
scale_factor =  (HEIGHT-PADDING_TOP)/max(lst) 
scale_factor = math.floor(scale_factor)
pygame.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
done = False  
# def insertionSort(arr):
     
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
 
#         key = arr[i]
 
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i-1
#         while j >= 0 and key < arr[j] :
#                 arr[j + 1] = arr[j]
#                 j -= 1

#         arr[j + 1] = key
fpsClock = pygame.time.Clock()
while not done:  
    # Make entire screen black

    color = white
    x = 30
    y = 600
    for index,special_colors in enumerate(bubble_sort(lst)):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
        screen.fill((0,0,0))    
        for i in range(len(lst)):
            x_diff = (WIDTH - PADDING_RIGHT-PADDING_LEFT)/len(lst)
            x_start = PADDING_LEFT + x_diff * i
            x_end = x_start + x_diff
            x_end = math.floor(x_end)
            pygame.draw.rect(screen, special_colors.get(i,white), (x_start,  HEIGHT - lst[i] * scale_factor, x_end-x_start,lst[i] * scale_factor))
            # draw.rectangle((x_start,  HEIGHT, x_end, 
            #                             HEIGHT - arr[i] * scale_factor), fill = special_colors.get(i,"white"))
        pygame.display.flip()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True 
        if done:
            break
                
        fpsClock.tick(60)
        # if index >520:

        #     # wait 1/60th of a second
        #     time.sleep(1)

    done = True
