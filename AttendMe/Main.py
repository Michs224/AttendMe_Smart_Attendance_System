from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from ttkthemes import ThemedStyle

class Smart_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("AttendMe")
        
        txt_label = Label(self.root, text="Welcome to AttendMe!", font=("Georgia", 30,"bold"), fg="brown")
        txt_label.place(x=150, y=50)

        img=Image.open("D:/Michh/Python/Projects/AttendMe/Images/tg.png")
        img=img.resize((300,150),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(relx=1, rely=0.02, anchor="ne")
        f_lbl.place(x=-50,y=0,width=300,height=150)

        # Image 1
        img1 = Image.open("D:/Michh/Python/Projects/AttendMe/Images/kisspng-student-group-student-society.png")
        img1 = img1.resize((250, 125), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=100, y=200, width=250, height=125)

if __name__=="__main__":
    root=Tk()
    # root.overrideredirect(True)
    obj=Smart_Attendance_System(root)
    root.mainloop()