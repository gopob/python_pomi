from tkinter import filedialog

import cv2
from tkinter import *
from PIL import ImageTk, Image
import numpy as np


images = []

# def save_image(src):
#


def select_image():
    global panelA, panelB, panelC, panelD
    path = filedialog.askopenfilename()


    if len(path) > 0:
        image = cv2.imread(path)
        src = image
        b, g, r = cv2.split(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


        srcTri = np.array([[0, 0], [src.shape[1] - 1, 0], [0, src.shape[0] - 1]]).astype(np.float32)
        dstTri = np.array([[0, src.shape[1] * 0.33], [src.shape[1] * 0.85, src.shape[0] * 0.25],
                           [src.shape[1] * 0.15, src.shape[0] * 0.7]]).astype(np.float32)
        warp_mat = cv2.getAffineTransform(srcTri, dstTri)
        warp_dst = cv2.warpAffine(src, warp_mat, (src.shape[1], src.shape[0]))

        image = Image.fromarray(image)
        gray = Image.fromarray(gray)
        warp_dst = Image.fromarray(warp_dst)

        image = ImageTk.PhotoImage(image)
        gray = ImageTk.PhotoImage(gray)
        warp_dst = ImageTk.PhotoImage(warp_dst)




    if panelA is None or panelB is None:

        panelA = Label(image=image, width =image.width(), height = image.height() )
        panelA.image = image
        panelA.grid(row = 3, column = 1)
        # saveA = Button(text="Select an A", command=save_image(image), width= 20, height = 3)
        # saveA.grid(row = 4, column = 1, columnspan = 2)
        panelB = Label(image=gray, width =gray.width(), height = gray.height())
        panelB.image = gray
        panelB.grid(row = 3, column = 3)
        panelC = Label(image=warp_dst, width =warp_dst.width(), height = warp_dst.height())
        panelC.image = warp_dst
        panelC.grid(row=3, column=5)


    else:
        panelA.configure(image=image)
        panelB.configure(image=gray)
        panelC.configure(image=warp_dst)

        panelA.image = image
        panelB.image = gray
        panelC.image = warp_dst



root = Tk()
panelA = None
panelB = None
panelC = None
panelD = None


btn = Button(root, text="Select an image", command=select_image, width= 20, height = 3)
btn.grid(row = 0, column = 0, columnspan = 3)


root.mainloop()