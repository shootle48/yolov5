import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import torch
import numpy as np
import os

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


model_path = os.path.join('runs', 'train', 'exp2', 'weights', 'best.pt')

root = Tk()
root.title("พี่หนุ่ม สแกนเนอร์")
root.bind("<Escape>", lambda e: root.quit())
root.geometry("640x640")

model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)



root.mainloop()