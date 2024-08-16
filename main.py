import cv2
import numpy as np
import glob
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image


#start interfata grafica
root = Tk()
root.title("Aplicatie examen")
my_img= ImageTk.PhotoImage(Image.open("Resources/itsoft.jpg"))
my_label= Label(image=my_img)
my_label.pack()

def popout():
     messagebox.showerror("ERROR MESSAGE","Ati introdus altceva inafara de numele unei imagini")


#Accesare fisiere
def open():
     global pozamea
     root.filename = filedialog.askopenfilename(initialdir="C:/Users/manma/PycharmProjects/openCvproject/Resources",title="Select a file", filetypes=(("png files","*.png"),("all files","*.*")))
     my_label = Label(root,text=root.filename).pack()
     pozamea= ImageTk.PhotoImage(Image.open(root.filename))
     pozamea_label=Label(image=pozamea).pack()
butonOpen= Button(root,text="Open Resources", command=open).pack()


def open2():
     global pozamea2
     root.filename = filedialog.askopenfilename(initialdir="C:/Users/manma/PycharmProjects/openCvproject/Templates",title="Select a file", filetypes=(("png files","*.png"),("all files","*.*")))
     my_label2 = Label(root,text=root.filename).pack()
     pozamea2= ImageTk.PhotoImage(Image.open(root.filename),width=50)
     pozamea2_label=Label(image=pozamea2).pack()
butonOpen2= Button(root,text="Open Templates Folder", command=open2).pack()


#terminare accesare fisiere



#functia pentru procesare imagine si buton

buttonAfisareMesaj= Button(root,text="Scrie in casuta de mai jos numele imaginei din Resources",state=DISABLED).pack()

e = Entry(root, width=50)
e.pack()
def myClick():
     myvar = e.get()
     myLabel= Label(root,text="Ati vizualizat poza " + myvar)
     template_data = []  # template  gri
     template_file = glob.glob('Templates/*')
     for poze in template_file:
           image = cv2.imread(poze, 0)
           template_data.append(image)

     path = "Resources/"
     path = path+ myvar

     myImage = cv2.imread(path)
     try:
          img_gray = cv2.cvtColor(myImage, cv2.COLOR_BGR2GRAY)
     except :
       popout()
     for tmp in template_data:
          w, h = tmp.shape[::-1]
          res = cv2.matchTemplate(img_gray, tmp, cv2.TM_CCOEFF_NORMED)
          threshold = 0.9
          loc = np.where(res >= threshold)
          for pt in zip(loc[1], loc[0]):
               cv2.circle(myImage, ((pt[0] + int(w / 2)), (pt[1] + int(h / 2))), int(h / 2), (0, 200, 0),  1)
     cv2.imshow('myImage',myImage)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     myLabel.pack()

myButton=Button(root,text="Apasa pentru gasirea template-ului in poza originala",command=myClick)

myButton.pack()
#sfarsit functie pentru procesare si buton


button_exit = Button(root,text="Exit program", command=root.quit)
button_exit.pack()



root.mainloop()
#end interfara grafica