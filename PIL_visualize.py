from PIL import Image,ImageDraw
import math
WIDTH = 1920
HEIGHT = 1080
PADDING_LEFT = 50
PADDING_RIGHT = 50
PADDING_TOP = 20
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
arr = [21,42,19,4,24,16,23,7,1,6,5,34,27,18,50,43,21,52,47,39,25,46,13,12,34,20,10,9,4,35,5,8,23]
scale_factor =  (HEIGHT-PADDING_TOP)/max(arr) 

# Draw rectangles on image
def draw_loop(arr,index,special_colors):
    image = Image.new('RGB', (WIDTH, HEIGHT), color = 'black')
    draw = ImageDraw.Draw(image)
    for i in range(len(arr)):
        x_diff = (WIDTH - PADDING_RIGHT-PADDING_LEFT)/len(arr)
        x_start = PADDING_LEFT + x_diff * i
        x_end = x_start + x_diff
        draw.rectangle((x_start,  HEIGHT, x_end, 
                                    HEIGHT - arr[i] * scale_factor), fill = special_colors.get(i,"white"))
    
    image.save(f"imgs/{str(index).zfill(5)}.png")

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
    yield special_colors
    yield {1:GREEN}
    yield {0:GREEN}
    # draw_loop(arr,index,{0:GREEN})
import os
os.mkdir("imgs")
for index,special_colors in enumerate(bubble_sort(arr)):
    draw_loop(arr,index,special_colors)
