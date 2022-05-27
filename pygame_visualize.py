import pygame
import pygame.image
# import multithreading
import threading

import sys
import math
import cv2


def thread_function(screen, index):
    pygame.image.save(screen, f"imgs/{str(index).zfill(5)}.png")


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            special_colors = {len(arr)-i: GREEN}
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            special_colors[j] = RED
            special_colors[j+1] = RED
            yield special_colors
    yield {1: GREEN}
    yield {0: GREEN}


RECORD = False
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 1280, 720
PADDING_LEFT, PADDING_RIGHT = 50, 50
PADDING_TOP = 20
MAX_FPS, VIDEO_FPS = 60, 60
lst = [21, 42, 19, 4, 24, 16, 23, 7, 1, 6, 5, 34, 27, 18, 50, 43,
       21, 52, 47, 39, 25, 46, 13, 12, 34, 20, 10, 9, 4, 35, 5, 8, 23]
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
    for index, special_colors in enumerate(bubble_sort(lst)):
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
    for thread in threading.enumerate():
        if thread is not threading.currentThread():
            thread.join()
    for i in range(index+1):
        img = cv2.imread(f"imgs/{str(i).zfill(5)}.png")
        out.write(img)
    out.release()
