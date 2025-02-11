import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import os
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
# ตรวจสอบ path ของโมเดล
model_path = os.path.join('runs', 'train', 'exp2', 'weights', 'best.pt')

if not os.path.exists(model_path):
    print(f"Error: File not found at {model_path}")
else:
    # โหลดโมเดล YOLOv5
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

    # ฟังก์ชันสำหรับการนำเข้าไฟล์ภาพ
    def browse_image():
        global img_path, img_label
        img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if img_path:
            img = Image.open(img_path)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            img_label.config(image=img_tk)
            img_label.image = img_tk

    # ฟังก์ชันสำหรับตรวจจับวัตถุ
    def detect_objects():
        global img_path, img_label
        if img_path:
            # โหลดภาพและทำการตรวจจับ
            results = model(img_path)
            results.save(save_dir='runs/detect/exp')  # บันทึกผลลัพธ์ในไดเรกทอรีที่กำหนด

            # แสดงผลลัพธ์
            output_img = Image.open('runs/detect/exp/2.jpg')  # โหลดภาพผลลัพธ์
            output_img = output_img.resize((300, 300), Image.ANTIALIAS)
            output_img_tk = ImageTk.PhotoImage(output_img)
            img_label.config(image=output_img_tk)
            img_label.image = output_img_tk

    # สร้าง GUI
    root = tk.Tk()
    root.title("Object Detection with YOLOv5")

    # ส่วนนำเข้าไฟล์ภาพ
    browse_button = tk.Button(root, text="Browse Image", command=browse_image)
    browse_button.pack(pady=10)

    # ส่วนแสดงภาพ
    img_label = tk.Label(root)
    img_label.pack()

    # ปุ่มตรวจจับวัตถุ
    detect_button = tk.Button(root, text="Detect Objects", command=detect_objects)
    detect_button.pack(pady=10)

    # รัน GUI
    root.mainloop()