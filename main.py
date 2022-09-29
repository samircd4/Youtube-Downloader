from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil



def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# Download function
def download_file():
    get_link = link_feild.get()
    user_path = path_label.cget('text')
    screen.title('Downloading...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    user_path = path_label.cget("text")
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')

screen = Tk()
title = screen.title('Youtube Downloader.   I made it for Nabin Bro! ((~_~))')
canvas = Canvas(screen, width=500, height=550)
screen.iconbitmap("you.ico")
canvas.pack()

logo_img = PhotoImage(file='sam.png')
logo_img = logo_img.subsample(2,2)
canvas.create_image(250,80, image=logo_img)
# Link feild
link_feild = Entry(screen, width=50, font=('Arial',10))
link_label = Label(screen, width=50, text='Paste your download link', font=('Arial',15))
# Add to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_feild)

# Select path for saving the file
path_label = Label(screen, width=50, text='Select destination folder to download file', font=('Arial',15))
select_btn = Button(screen,width=10, text='Select', font=('Arial',15), command=select_path)
canvas.create_window(250,270, window=path_label)
canvas.create_window(250,310, window=select_btn)
# Download button
dwnd = PhotoImage(file="R.png")
download_btn = Button(screen, image=dwnd, borderwidth=0, command=download_file, font=('roboto',15))
canvas.create_window(250,450, window=download_btn)


screen.mainloop()