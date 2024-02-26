from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from Main import LibraLink
from FaceRecognition_CNN import Face_Recognition
from RecommenderBook import RecommmenderBook


def to_images(str):
    return Path(__file__).resolve().parent /"Images/frame_3" / str

def Take_Attendance_Students(root):
    
    root.geometry("1920x1080")
    root.configure(bg = "#FEFFF2")
    root.title("LibraLink: Take Attendance Students")


    canvas = Canvas(root,bg = "#FEFFF2",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)

    image_image_1 = PhotoImage(file=to_images("image_logo.png"))
    image_1 = canvas.create_image(1694.0,150.0,image=image_image_1)

    image_image_2 = PhotoImage(file=to_images("image_2.png"))
    image_2 = canvas.create_image(1423.0,516.0,image=image_image_2)

    canvas.create_rectangle(1499.0,40.0,1509.0,200.0,fill="#EF16A5",outline="")

    canvas.create_text(950.0,83.0,anchor="nw",text="DASHBOARD",fill="#000000",font=("RobotoRoman Bold", 60 * -1))

    image_image_3 = PhotoImage(file=to_images("image_3.png"))
    image_3 = canvas.create_image(424.0,118.0,image=image_image_3)



    image_image_4 = PhotoImage(file=to_images("image_4.png"))
    image_4 = canvas.create_image(719.0,62.0,image=image_image_4)
    canvas.tag_bind(image_4, '<Enter>', lambda event, img=image_4 :on_image_enter(img))
    canvas.tag_bind(image_4, '<Leave>', lambda event, img=image_4 :on_image_leave(img))
    canvas.tag_bind(image_4, '<Button-1>', lambda event, img=image_4: on_image_click(img))

    image_image_5 = PhotoImage(file=to_images("image_5.png"))
    image_5 = canvas.create_image(319.0,493.0,image=image_image_5)
    canvas.tag_bind(image_5, '<Enter>', lambda event, img=image_5 :on_image_enter(img))
    canvas.tag_bind(image_5, '<Leave>', lambda event, img=image_5 :on_image_leave(img))
    canvas.tag_bind(image_5, '<Button-1>', lambda event, img=image_5: on_image_click(img))


    image_image_6 = PhotoImage(file=to_images("image_6.png"))
    image_6 = canvas.create_image(540.0,815.0,image=image_image_6)
    canvas.tag_bind(image_6, '<Enter>', lambda event, img=image_6 :on_image_enter(img))
    canvas.tag_bind(image_6, '<Leave>', lambda event, img=image_6 :on_image_leave(img))
    canvas.tag_bind(image_6, '<Button-1>', lambda event, img=image_6: on_image_click(img))


    image_image_7 = PhotoImage(file=to_images("image_7.png"))
    image_7 = canvas.create_image(773.0,493.0,image=image_image_7)
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