import pygame
import tkinter as tk
import os
import xml.etree.ElementTree as ET
import imageio
os.environ["IMAGEIO_FFMPEG_EXE"] = "/path/to/ffmpeg"


class App:
    def __init__(self, root, video_name):
        self.root = root
        # App title
        self.root.title("Learn Language with Youtube Videos")
        # Load video
        self.video_path = os.path.join("videos", video_name + ".mp4")
        self.subtitle_path = os.path.join("videos", video_name + ".xml")

        # Video player
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack()

        self.create_video_player()

    def create_video_player(self):
        self.video = imageio.get_reader(self.video_path)
        self.video_screen = tk.Label(self.video_frame)
        self.video_screen.pack()

        self.play_video()

    def play_video(self):
        for frame in self.video.iter_data():
            image = tk.PhotoImage(data=frame)
            self.video_screen.configure(image=image)
            self.video_screen.image = image
            self.root.update()


if __name__ == "__main__":
    video_name = "Balance ton quoi"

    root = tk.Tk()
    app = App(root, video_name)
    root.mainloop()
