import tkinter as tk
from tkinter.font import Font
from typing import Text
from PIL import Image, ImageTk
from matplotlib.pyplot import text
from pyparsing import col
import cv2
import imutils
# show webcam frame function



def show_capture_frame():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame= cap.read()
        cv2.imshow("Webcam",frame)
        key= cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()

def exitGUI():
    root.destroy()



root= tk.Tk()
# initialize title
root.title("Object Detection")


# Initialize Logo
logoIcon=Image.open('odLogo.png')
logoIcon=logoIcon.resize((250,150),Image.ANTIALIAS)
logoIcon= ImageTk.PhotoImage(logoIcon)
logoIcon_label= tk.Label(image=logoIcon,padx=10,pady=10)
logoIcon_label.grid(column=1,row=1)

# initialize Labels frame
application_Title=tk.Label(root,text="Object Detection Application",font=Font(family="Poppins",size=20,weight="bold"),fg='lightblue').grid(row=0,column=1)

description= tk.Label(root,text='Object Detection Project\nDeveloped by Lê Nguyễn Anh Khôi & Bùi Ngọc Chính\n19TGMT',font=Font(family="Poppins",size=8,weight="normal"),fg="grey",padx=10,pady=10).grid(row=2,column=1)

# buttons

openImageButton=tk.Button(root,text="Image File",bg="lightblue",width=15,height=1,font=Font(family="Poppins",size=10,weight='bold'),padx=10,pady=10).grid(row=3,column=0)
openWebcamButton=tk.Button(root,text="Open Webcam",bg="lightblue",width=15,height=1,font=Font(family="Poppins",size=10,weight='bold'),padx=10,pady=10,command=show_capture_frame).grid(row=3,column=1)
exitButton=tk.Button(root,text="Exit",bg="lightblue",width=15,height=1,font=Font(family="Poppins",size=10,weight='bold'),padx=10,pady=10,command=exitGUI).grid(row=3,column=3)



# initialize button

root.mainloop()
