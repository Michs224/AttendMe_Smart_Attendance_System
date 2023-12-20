from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import os
from StudentDetails import Student_Details
# from TakeAttendanceStudents import Take_Attendance_Students
from HelpDesk import Help_Desk
import cv2

class LibraLink:
    
    def __init__(self,root):
        self.window=root
        # self.window=Tk()
        self.window.geometry("2560x1600+0+0")
        self.window.title("Libra Link: Smart Attendance System with Book Recommender")
        self.window.configure(bg = "#FDFFE8")
        self.window.overrideredirect(True)

        self.canvas = Canvas(
            self.window,
            bg = "#FDFFE8",
            height = 1600,
            width = 2560,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        
        # Image 1
        self.image_image_1 = PhotoImage(file=self.to_images("image_1.png"))
        self.image_1 = self.canvas.create_image(433.0,723.0,image=self.image_image_1)

        self.canvas.tag_bind(self.image_1, '<Enter>', lambda event, img=self.image_1 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_1, '<Leave>', lambda event, img=self.image_1 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_1, '<Button-1>', lambda event, img=self.image_1: self.on_image_click(img))

        # Image 2 Photo Data Button
        self.image_image_2 = PhotoImage(file=self.to_images("image_3.png"))
        self.image_2 = self.canvas.create_image(1091.0,723.0,image=self.image_image_2)
        
        self.canvas.tag_bind(self.image_2, '<Enter>', lambda event, img=self.image_2 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_2, '<Leave>', lambda event, img=self.image_2 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_2, '<Button-1>', lambda event, img=self.image_2: self.on_image_click(img))
        
        # Image 3
        self.image_image_3 = PhotoImage(file=self.to_images("image_4.png"))
        self.image_3 = self.canvas.create_image(1749.0,720.0,image=self.image_image_3)
        
        self.canvas.tag_bind(self.image_3, '<Enter>', lambda event, img=self.image_3 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_3, '<Leave>', lambda event, img=self.image_3 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_3, '<Button-1>', lambda event, img=self.image_3: self.on_image_click(img))

        # Image 4
        self.image_image_4 = PhotoImage(file=self.to_images("image_6.png"))
        self.image_4 = self.canvas.create_image(433.0,1272.0,image=self.image_image_4)
        self.canvas.tag_bind(self.image_4, '<Enter>', lambda event, img=self.image_4 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_4, '<Leave>', lambda event, img=self.image_4 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_4, '<Button-1>', lambda event, img=self.image_4: self.on_image_click(img))
        
        # Image 5
        self.image_image_5 = PhotoImage(file=self.to_images("image_2.png"))
        self.image_5 = self.canvas.create_image(1091.0,1272.0,image=self.image_image_5)
        self.canvas.tag_bind(self.image_5, '<Enter>', lambda event, img=self.image_5 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_5, '<Leave>', lambda event, img=self.image_5 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_5, '<Button-1>', lambda event, img=self.image_5: self.on_image_click(img))

        # Image 6 exit button
        self.image_image_6 = PhotoImage(file=self.to_images("image_7.png"))
        self.image_6 = self.canvas.create_image(1749.0,1272.0,image=self.image_image_6)
        self.canvas.tag_bind(self.image_6, '<Enter>', lambda event, img=self.image_6 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_6, '<Leave>', lambda event, img=self.image_6 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_6, '<Button-1>', lambda event, img=self.image_6: self.on_image_click(img))

        # Image 7
        self.image_image_7 = PhotoImage(file=self.to_images("image_5.png"))
        self.image_7 = self.canvas.create_image(2258.404296875,996.0,image=self.image_image_7)
        
        self.canvas.tag_bind(self.image_7, '<Enter>', lambda event, img=self.image_7 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_7, '<Leave>', lambda event, img=self.image_7 :self.on_image_leave(img))
        self.canvas.tag_bind(self.image_7, '<Button-1>', lambda event, img=self.image_7: self.on_image_click(img))

        # Image 8
        self.image_image_8 = PhotoImage(file=self.to_images("image_logo.png"))
        image_8 = self.canvas.create_image(2351.0,170.0,image=self.image_image_8)

        # Line sebelah logo
        self.canvas.create_rectangle(2121.0,34.0,2129.0,242.0,fill="#EF16A5",outline="")

        # Text Dashboard
        self.canvas.create_text(1462.0,95.0,anchor="nw",text="DASHBOARD",fill="#000000",font=("RobotoRoman Bold", 90 * -1))

        # Image 9
        self.image_image_9 = PhotoImage(file=self.to_images("image_9.png"))
        image_9 = self.canvas.create_image(700.0,245.0,image=self.image_image_9)
        
        # Image 10
        self.image_image_10=PhotoImage(file=self.to_images("image_10.png"))
        self.image_10=self.canvas.create_image(1227.0,144.0,image=self.image_image_10)
        self.canvas.tag_bind(self.image_10, '<Enter>', lambda event, img=self.image_10 :self.on_image_enter(img))
        self.canvas.tag_bind(self.image_10, '<Leave>', lambda event, img=self.image_10:self.on_image_leave(img))
        self.canvas.tag_bind(self.image_10, '<Button-1>', lambda event, img=self.image_10: self.on_image_click(img))
        

    def animate_image(self,image_item, x1, y1, x2, y2):
        self.canvas.move(image_item, x1, y1)
        self.canvas.after(1)  # Jeda gerak (ms)
        self.canvas.update()
        
        self.canvas.move(image_item, x2, y2)
        self.canvas.after(100)
        self.canvas.update()
            
    def zoom_in_image(self,image_item):
        self.canvas.move(image_item,3,8)
        self.canvas.update()
        
    def zoom_out_image(self,image_item):
        self.canvas.move(image_item,-3,-8)
        self.canvas.update()

    def on_image_click(self,image):
        if image==self.image_1:
            self.animate_image(image, 3, 8, -3, -8)
            self.window.withdraw()
            new_window = Toplevel(self.window)
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_new_window_close(image,new_window))
            Student_Details(new_window)
        elif image==self.image_2:
            self.animate_image(image, 3, 8, -3, -8)
            self.open_photodata()
        elif image==self.image_3:
            self.animate_image(image, 3, 8, -3, -8)
            self.open_attendancedata()
        elif image==self.image_4:
            self.animate_image(image, 3, 8, -3, -8)
            from TrainCNN import TrainData
            TrainData()
        elif image==self.image_5:
            self.animate_image(image, 3, 8, -3, -8)
            self.open_bookdata()
        elif image==self.image_6:
            self.animate_image(image, 3, 8, -3, -8)
            self.window.destroy()
        elif image==self.image_7:
            self.animate_image(image, 3, 8, -3, -8)
            self.window.withdraw()
            new_window = Toplevel(self.window)
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_new_window_close(image,new_window))
            Help_Desk(new_window)  
        elif image==self.image_10:
            from TakeAttendanceStudents import Take_Attendance_Students
            self.animate_image(image, 3, 8, -3, -8)
            self.window.withdraw()
            new_window = Toplevel(self.window)
            Take_Attendance_Students(new_window)
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_new_window_close(image,new_window))
            # from TakeAttendanceStudents import Take_Attendance_Students
            # Take_Attendance_Students(new_window)
                     
        else:
            self.animate_image(image, 3, 8, -3, -8)  # Animasi
    def on_new_window_close(self, image,new_window):
        if image==self.image_10:
            new_window.destroy()
        else:
            new_window.destroy()
            self.window.deiconify()
        
    def on_image_enter(self,image):
        self.zoom_in_image(image)
        self.canvas.config(cursor="hand2")
        # self.canvas.update()
        
    def on_image_leave(self,image):
        self.zoom_out_image(image)
        self.canvas.config(cursor="")
        # self.canvas.update()

    def open_photodata(self):
        os.startfile("Photo Data")
        
    def open_attendancedata(self):
        os.startfile("AttendanceData")
    
    def open_bookdata(self):
        os.startfile("Recommender Book\Books")
        
    def to_images(self,str):
        return Path(__file__).resolve().parent /"Images/frame_1" / str

if __name__=="__main__":
    root=Tk()
    App=LibraLink(root)
    # App.window.overrideredirect(True)
    App.window.mainloop()    