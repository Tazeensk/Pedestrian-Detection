import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import cv2
from Model import Detector
import numpy as np

def detect_pedestrians():
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.endswith('.mp4'):
            detect_pedestrians_video(file_path)
        else:
            detect_pedestrians_image(file_path)

def detect_pedestrians_image(file_path):
    image = cv2.imread(file_path)
    detected_image = Detector(image)
    cv2.imshow('Detected Pedestrians', detected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_pedestrians_video(file_path):
    cap = cv2.VideoCapture(file_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected_frame = Detector(frame)
        cv2.imshow('Detected Pedestrians', detected_frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

top = tk.Tk()
top.geometry('800x600')
top.title("Pedestrian Detection")
top.configure(background="#ADD8E6")

label1 = Label(top, background="#ADD8E6", font=("arial", 15, "bold"))
sign_image = Label(top)

def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((128, 128))
    image = np.array(image)
    image = np.array([image])/255
    pred = Detector(image)
    return pred

def show_Detect_button(file_path):
    detected_image = Detect(file_path)
    cv2.imshow('Detected Pedestrians', detected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text="")
        show_Detect_button(file_path)
    except Exception as e:
        print(e)

upload = Button(top, text="Upload an Image or Video", command=detect_pedestrians, padx=10, pady=5)
upload.configure(background="#000080", foreground="white", font=("arial", 10, 'bold'))
upload.pack(side='bottom', pady=50)
sign_image.pack(side="bottom", expand=True)
label1.pack(side='bottom', expand=True)
heading = Label(top, text="Pedestrian Detection", pady=20, font=("arial", 20, "bold"))
heading.configure(background="#ADD8E6", foreground="#000080")
heading.pack()
top.mainloop()
