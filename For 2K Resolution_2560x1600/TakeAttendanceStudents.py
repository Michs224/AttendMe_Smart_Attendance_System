from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from Main import LibraLink
from FaceRecognition_CNN import Face_Recognition
from RecommenderBook import RecommmenderBook


def to_images(str):
    return Path(__file__).resolve().parent /"Images/frame_3" / str

def Take_Attendance_Students(root):
    
    root.geometry("2560x1600")
    root.configure(bg = "#FEFFF2")
    root.title("LibraLink: Take Attendance Students")


    canvas = Canvas(root,bg = "#FEFFF2",height = 1600,width = 2560,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)

    image_image_1 = PhotoImage(file=to_images("image_logo.png"))
    image_1 = canvas.create_image(2351.0,170.0,image=image_image_1)

    image_image_2 = PhotoImage(file=to_images("image_2.png"))
    image_2 = canvas.create_image(2010.0,944.0,image=image_image_2)

    canvas.create_rectangle(2121.0,34.0,2129.0,242.0,fill="#EF16A5",outline="")

    canvas.create_text(1462.0,95.0,anchor="nw",text="DASHBOARD",fill="#000000",font=("RobotoRoman Bold", 90 * -1))

    image_image_3 = PhotoImage(file=to_images("image_3.png"))
    image_3 = canvas.create_image(700.0,244.91162109375,image=image_image_3)



    image_image_4 = PhotoImage(file=to_images("image_4.png"))
    image_4 = canvas.create_image(1227.0,138.0,image=image_image_4)
    canvas.tag_bind(image_4, '<Enter>', lambda event, img=image_4 :on_image_enter(img))
    canvas.tag_bind(image_4, '<Leave>', lambda event, img=image_4 :on_image_leave(img))
    canvas.tag_bind(image_4, '<Button-1>', lambda event, img=image_4: on_image_click(img))

    image_image_5 = PhotoImage(file=to_images("image_5.png"))
    image_5 = canvas.create_image(419.0,799.0,image=image_image_5)
    canvas.tag_bind(image_5, '<Enter>', lambda event, img=image_5 :on_image_enter(img))
    canvas.tag_bind(image_5, '<Leave>', lambda event, img=image_5 :on_image_leave(img))
    canvas.tag_bind(image_5, '<Button-1>', lambda event, img=image_5: on_image_click(img))


    image_image_6 = PhotoImage(file=to_images("image_6.png"))
    image_6 = canvas.create_image(753.0,1310.0,image=image_image_6)
    canvas.tag_bind(image_6, '<Enter>', lambda event, img=image_6 :on_image_enter(img))
    canvas.tag_bind(image_6, '<Leave>', lambda event, img=image_6 :on_image_leave(img))
    canvas.tag_bind(image_6, '<Button-1>', lambda event, img=image_6: on_image_click(img))


    image_image_7 = PhotoImage(file=to_images("image_7.png"))
    image_7 = canvas.create_image(1090.0,799.0,image=image_image_7)
    canvas.tag_bind(image_7, '<Enter>', lambda event, img=image_7 :on_image_enter(img))
    canvas.tag_bind(image_7, '<Leave>', lambda event, img=image_7 :on_image_leave(img))
    canvas.tag_bind(image_7, '<Button-1>', lambda event, img=image_7: on_image_click(img))   


    def animate_image(image_item, x1, y1, x2, y2):
        canvas.move(image_item, x1, y1)
        canvas.after(1)
        canvas.update()
        
        canvas.move(image_item, x2, y2)
        canvas.after(100)
        canvas.update()
            
    def zoom_in_image(image_item):
        canvas.move(image_item,3,8)
        canvas.update()
        
    def zoom_out_image(image_item):
        canvas.move(image_item,-3,-8)
        canvas.update()

    def on_image_click(image):
        if image==image_4:
            animate_image(image, 3, 8, -3, -8)
            new_window=Toplevel(root)
            LibraLink(new_window)
            root.withdraw()
            new_window.protocol("WM_DELETE_WINDOW", lambda: on_new_window_close(image,new_window))
        elif image==image_5:
            animate_image(image, 3, 8, -3, -8)
            Face_Recognition()
        elif image==image_6:
            root.destroy()   
        elif image==image_7:
            animate_image(image, 3, 8, -3, -8)
            new_window=Toplevel(root)
            RecommmenderBook(new_window)
            root.withdraw()
            new_window.protocol("WM_DELETE_WINDOW", lambda: on_new_window_close(image,new_window))
            # open_streamlit_app()           
        else:
            animate_image(image, 3, 8, -3, -8)  # Animasi
            
    def open_streamlit_app():
        subprocess.Popen([r"C:\Users\micha\Anaconda3\envs\EnvLibraLink\Scripts\streamlit.exe", "run", str(Path(__file__).resolve().parent / "Recommender Book" / "app.py")])
        # Ke Directory streamlit.exe dari environtment kalian, lalu pastiin app.py tetap di folder Recommender Book yang satu folder dengan TakeAttendanceStudent.py

          
    def on_new_window_close(self, image,new_window):
        if image==image_4:
            new_window.destroy()
        else:
            new_window.destroy()
            root.deiconify()
            
    def on_image_enter(image):
        zoom_in_image(image)
        canvas.config(cursor="hand2")
        # canvas.update()
        
    def on_image_leave(image):
        zoom_out_image(image)
        canvas.config(cursor="")
        # canvas.update()
    
    # root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    root=Tk()
    Take_Attendance_Students(root)
    # App.mainloop()