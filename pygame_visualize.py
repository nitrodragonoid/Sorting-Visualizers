
import pygame
import pygame.image
# import multithreading
import threading
from algos import *
import sys
import math
import cv2


def thread_function(screen, index):
    pygame.image.save(screen, f"imgs/{str(index).zfill(5)}.png")

lst = [21, 42, 19, 4, 24, 16, 23, 7, 3, 6, 5, 34, 27, 18, 50, 43,
       21, 52, 47, 39, 25, 46, 13, 12, 34, 20, 10, 9, 4, 35, 5, 8, 23]
# create lst of 256 random numbers from 23 to 100
import random
lst = [random.randint(5, 40) for _ in range(256)] 
# lst = [3,1,4,5,6,6]
scale_factor = (HEIGHT-PADDING_TOP)/max(lst)
scale_factor = math.floor(scale_factor)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

if RECORD:
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("pygame.mp4", fourcc, VIDEO_FPS, (WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()

while not done:
    for index, special_colors in enumerate(radixSort(lst)):
        screen.fill((0, 0, 0))
        for i in range(len(lst)):
            x_diff = (WIDTH - PADDING_RIGHT-PADDING_LEFT)/len(lst)
            x_start = PADDING_LEFT + x_diff * i
            x_end = x_start + x_diff
            x_end = math.floor(x_end)
            pygame.draw.rect(screen, special_colors.get(
                i, WHITE), (x_start,  HEIGHT - lst[i] * scale_factor, x_end-x_start, lst[i] * scale_factor))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if done:
            break
        fpsClock.tick(MAX_FPS)
        if RECORD:
            x = threading.Thread(target=thread_function,
                                 args=(screen.copy(), index))
            x.start()
    done = True

if RECORD:
    import os
    # os.mkdir("imgs")
    if not os.path.exists("imgs"):
        os.mkdir("imgs")
    else:
        for file_name in os.listdir("imgs"):
            os.remove(os.path.join("imgs",file_name))

    for thread in threading.enumerate():
        if thread is not threading.currentThread():
            thread.join()
    for i in range(index+1):
        img = cv2.imread(f"imgs/{str(i).zfill(5)}.png")
        out.write(img)
    out.release()
