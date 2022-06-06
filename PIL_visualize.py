from PIL import Image,ImageDraw
import math
from algos import *
import shutil
import os

output_name = "final.mp4"
arr = [21,42,19,4,24,16,23,7,1,6,5,34,27,18,50,43,21,52,47,39,25,46,13,12,34,20,10,9,4,35,5,8,23]
scale_factor =  (HEIGHT-PADDING_TOP)/max(arr) 
img_names = []
# Draw rectangles on image
def draw_loop(arr,image_num,special_colors,img_names):
    image = Image.new('RGB', (WIDTH, HEIGHT), color = 'black')
    draw = ImageDraw.Draw(image)
    for i in range(len(arr)):
        x_diff = (WIDTH - PADDING_RIGHT-PADDING_LEFT)/len(arr)
        x_start = PADDING_LEFT + x_diff * i
        x_end = x_start + x_diff
        draw.rectangle((x_start,  HEIGHT, x_end, 
                                    HEIGHT - arr[i] * scale_factor), fill = special_colors.get(i,"white"))
    
    image.save(f"imgs/{str(image_num).zfill(5)}.png")
    
    # uncomment for 2 frames
    image.save(f"imgs/{str(image_num).zfill(5)}1.png")
    
    # uncomment for 3 frames
    image.save(f"imgs/{str(image_num).zfill(5)}2.png")
    
    # uncomment for 4 frames
    image.save(f"imgs/{str(image_num).zfill(5)}3.png")
    
    # uncomment for 5 frames
    image.save(f"imgs/{str(image_num).zfill(5)}4.png")

    # draw_loop(arr,index,{0:GREEN})


os.mkdir("imgs")
if not os.path.exists("imgs"):
    os.mkdir("imgs")
else:
    for file_name in os.listdir("imgs"):
        os.remove(os.path.join("imgs",file_name))
import cv2
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("PIL_Visualize.mp4", fourcc, VIDEO_FPS, ( WIDTH, HEIGHT))

for index,special_colors in enumerate(radixSort(arr)):
    draw_loop(arr,index,special_colors,img_names)
    img = cv2.imread(f"imgs/{str(index).zfill(5)}.png")
    out.write(img)
    
    # uncomment for 2 frames
    img = cv2.imread(f"imgs/{str(index).zfill(5)}1.png")
    out.write(img)
    
    # uncomment for 3 frames
    img = cv2.imread(f"imgs/{str(index).zfill(5)}2.png")
    out.write(img)
    
    # uncomment for 4 frames
    img = cv2.imread(f"imgs/{str(index).zfill(5)}3.png")
    out.write(img)
    
    # uncomment for 5 frames
    img = cv2.imread(f"imgs/{str(index).zfill(5)}4.png")
    out.write(img)
    
out.release()


#Adding Audio
import moviepy.editor as mpe
my_clip = mpe.VideoFileClip('PIL_Visualize.mp4')
audio_background = mpe.AudioFileClip('audio.mp3') # ADD THE AUDIO FILE YOU WANT TO ADD HERE
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile(output_name)


#Deleting the extra files
shutil.rmtree("imgs")
os.remove('PIL_Visualize.mp4')

#process comeplete
print("Done")
