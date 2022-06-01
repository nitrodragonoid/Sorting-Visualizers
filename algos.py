WHITE = (255, 255, 255)
RED = (255, 0, 0)

# BLUE = (173, 216, 230)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

RECORD = True
WIDTH, HEIGHT = 1280, 720
PADDING_LEFT, PADDING_RIGHT = 50, 50
PADDING_TOP = 20
MAX_FPS, VIDEO_FPS = 120, 60

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

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            special_colors = {i-1:GREEN}
            if arr[j] < arr[min_index]:
                min_index = j
            special_colors[j] = RED
            # special_colors[min_index] = RED
            yield special_colors
        yield {i-1: GREEN, i : YELLOW, min_index : YELLOW}
        arr[i], arr[min_index] = arr[min_index], arr[i]
    yield {len(arr)-1: GREEN}

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            special_colors = {i-1:GREEN}
            arr[j], arr[j-1] = arr[j-1], arr[j]
            special_colors[j], special_colors[j-1] = RED, RED
            j -= 1
            yield special_colors
        
    yield {len(arr)-1: GREEN}
    
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
            yield{}
    yield{}
            
        
from itertools import permutations
import random

def bogo_sort(arr):
    s = sorted(arr)
    while True:
        random.shuffle(arr)
        if arr == s:
            yield {i:GREEN for i in range(len(arr))}
            break
        else:
            yield {}
            
    # arr_copy = arr.copy()
    # for a in permutations(arr_copy):
    #     for i,val in enumerate(a):
    #         arr[i] = val
    #     flag = True
    #     for i in range(0,len(arr)-1):
    #         if arr[i] >arr[i+1]:
    #             flag = False
    #             break
    #     if flag == True:
    #         yield {i:GREEN for i in range(len(arr))}
    #         break
    #     else:
    #         yield {}

def merge_sort(arr):
    yield from _merge_sort(arr, 0, len(arr)-1)

def _merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        yield from _merge_sort(arr, start, mid)
        yield from _merge_sort(arr, mid+1, end)
        yield from merge(arr, start, mid, end)

def merge(arr,start,mid, end):
    yield {}
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    i = 0
    j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            yield {start: GREEN, end: GREEN,mid: BLUE,k:GREEN}
            i += 1
        else:
            arr[k] = right[j]
            yield {start: GREEN, end: GREEN,mid: BLUE,k:GREEN}
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        yield {start: GREEN, end: GREEN,mid: BLUE,k:GREEN}
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        yield {start: GREEN, end: GREEN,mid: BLUE,k:GREEN}
        j += 1
        k += 1
    for i in range(start, end+1):
        yield {i:GREEN for i in range(start,i+1)}

def QuickSort(arr):
    yield from _QuickSort(arr, 0, len(arr)-1)
def _QuickSort(arr, start, end):
    if start < end:
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield {i:GREEN,j:GREEN,start: RED, end:RED}
                i += 1
        arr[i], arr[end] = arr[end], arr[i]
        mid = i
        yield {i:GREEN,mid: BLUE,end:RED,start:RED}
        yield from _QuickSort(arr, start, mid-1)
        yield from _QuickSort(arr, mid+1, end)
        special_cols = {mid: BLUE,start:RED,end:RED}

        yield special_cols
        for i in range(start, end+1):
            if i == mid:
                continue
            special_cols[i] = GREEN
            yield special_cols

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        yield {i:GREEN}



# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        yield from countingSort(array, place)
        place *= 10
