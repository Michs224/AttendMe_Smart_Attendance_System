from io import BytesIO
import os
from pathlib import Path
import pickle
import platform

from tkinter import Frame, Image, Label, Scrollbar, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, ttk
from tkinter.font import Font
import winsound

from PIL import Image as PILImage, ImageTk
import numpy as np
import requests


def relative_to_assets(str):
    return Path(__file__).resolve().parent /"Images/recommender_book_frame" / str

def RecommmenderBook(root):
    # root = Tk()
    root.geometry("1920x1080")
    root.configure(bg = "#FDFFE8")
    root.title("LibraLink: Recommender Book")

    Entry_font=Font(family="Bahnschrift SemiLight",size=20)

    canvas = Canvas(root,bg = "#FDFFE8",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    
    
    model = pickle.load(open(str(Path(__file__).resolve().parent / "Recommender Book/model.pkl"), "rb"))
    book_names = pickle.load(open(str(Path(__file__).resolve().parent / "Recommender Book/bookNames.pkl"), "rb"))
    final_rating = pickle.load(open(str(Path(__file__).resolve().parent / "Recommender Book/finalRating.pkl"), "rb"))
    book_pivot = pickle.load(open(str(Path(__file__).resolve().parent / "Recommender Book/bookPivot.pkl"), "rb"))

    
    image_image_1 = PhotoImage(file=relative_to_assets("image_logo.png"))
    image_1 = canvas.create_image(1694.0, 150.0,image=image_image_1)

    canvas.create_rectangle(1499.0,40.0,1509.0,200.0,fill="#EF16A5",outline="")

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(960.0,373.0,image=image_image_2)

    canvas.create_text(721.0,89.0,anchor="nw",text="BOOK RECOMMENDER",fill="#000000",font=("Bahnschrift SemiBold SemiConden", 70 * -1))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(941.0,373.5,image=entry_image_1,)
    # entry_1 = Entry(root,bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=Entry_font)
    # entry_1.place(x=702.0,y=420.0,width=993.0,height=53.0)
    
    style = ttk.Style()
    style.configure("Transparent.TCombobox",borderwidth=0, fieldbackground="#FDFFE8",background="#FDFFE8",arrowsize=0) 
    
    selected_book_var = StringVar()
    book_combo = ttk.Combobox(root,textvariable=selected_book_var,font=Font(family="Bahnschrift SemiCondensed",size=20),state="readonly",style="Transparent.TCombobox")
    # print(book_names)
    books=["Select Title"]+list(book_names)
    book_combo["values"]=tuple(books)
    book_combo.current(0)
    canvas.create_window(941.0, 373.5, window=book_combo, width=948.0, height=63.0)
    

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(1594.0,375.0,image=image_image_3)
    canvas.tag_bind(image_3, '<Enter>', lambda event, img=image_3 :on_image_enter(img))
    canvas.tag_bind(image_3, '<Leave>', lambda event, img=image_3:on_image_leave(img))
    canvas.tag_bind(image_3, '<Button-1>', lambda event, img=image_3: on_image_click(img))

    canvas.create_text(194.0,350.0,anchor="nw",text="Enter Book Title",fill="#000000",font=("Bahnschrift SemiBold SemiConden", 35 * -1))
    
    # canvas.create_rectangle(97.0,586.0,2462.0,684.0,fill="#EFE715",outline="")
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(960.0,485.0,image=image_image_4)
    
    # canvas.create_rectangle(97.0,684.0,2462.0,1480.0,fill="#FFFFFF",outline="")

    canvas.create_text(765.0,458.0,anchor="nw",text="Book Recommendations:",fill="#000000",font=("Bahnschrift SemiBold SemiConden", 40 * -1))

    
    # table_canvas = Canvas(root, bg="#FDFFE8", highlightthickness=0)
    # table_canvas.place(x=94.0, y=680.0, width=2371.0, height=777)   
    
    
    # --------------------- Function Animasi ---------------------
    
    def animate_image(image_item, x1, y1, x2, y2):
        canvas.move(image_item, x1, y1)
        canvas.after(1)
        canvas.update()
        
        canvas.move(image_item, x2, y2)
        canvas.after(100)
        canvas.update()
            
    def zoom_in_image(image_item):
        canvas.move(image_item,2,5)
        canvas.update()
        
    def zoom_out_image(image_item):
        canvas.move(image_item,-2,-5)
        canvas.update()

    def on_image_click(image):
        animate_image(image, 2, 5, -2, -5)
        show_recommendations()

    def on_image_enter(image):
        zoom_in_image(image)
        canvas.config(cursor="hand2")
        # canvas.update()
        
    def on_image_leave(image):
        zoom_out_image(image)
        canvas.config(cursor="")
        # canvas.update()
    
    
    
    # ------------------------ Recommender Book ------------------------
    
        
    def show_custom_error(message):
        # Suara buat error
        os_name = platform.system()
        if os_name == "Windows":
            winsound.MessageBeep(winsound.MB_ICONHAND)
        elif os_name == "Darwin":  # Alias untuk macOS
            os.system('osascript -e "beep 2"')
        elif os_name == "Linux":
            try:
                os.system('beep')
            except:
                os.system('spd-say "beep"')
                
        # Window baru
        error_window = Toplevel()
        error_window.title("Error Message")
        error_window.geometry("400x215")
        error_window.config(bg='#f99c99')
        # error_window.resizable(False,False)

        # Biar gak bisa interact ke window lain, harus klik di error dahulu
        error_window.grab_set()

        # Frame buat konten
        frame = Frame(error_window, bg='#f99c99')
        frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Label buat pesan error
        Label(frame, text="Error!", font=("Bahnschrift SemiCondensed", 25, 'bold'), bg='#f99c99', fg='#d00000').pack(pady=(10, 0))
        
        if message=="All fields are required!":
            Label(frame, text=message, font=("Bahnschrift SemiCondensed", 20), bg='#f99c99', fg='#333333').pack(pady=10)
        elif message=="Date of Birth must be in YYYY-MM-DD format!":
            Label(frame, text=message, font=("Bahnschrift SemiCondensed", 16), bg='#f99c99', fg='#333333').pack(pady=10)
        else:
            Label(frame, text=message, font=("Bahnschrift SemiCondensed", 16), bg='#f99c99', fg='#333333').pack(pady=10)
                
        ok_button = Button(frame, text="OK", command=error_window.destroy, font=("Bahnschrift SemiCondensed", 14), bg='#d00000', fg='white', bd=0)
        ok_button.pack(pady=10,ipadx=10)
    

    def show_recommendations():
        selected_book = selected_book_var.get()
        if selected_book and selected_book != "Select Title":
            recommended_books_info, poster_url = recommend_book(selected_book)
            book_info = list(zip(recommended_books_info, poster_url))
            display_book_images(book_info)
        else:
            show_custom_error("Please select a book first.")
            


    scroll_frame = Frame(root)
    scroll_frame.place(x=93.0, y=520.0, width=1734.0, height=480)

    scrollbar_x = Scrollbar(scroll_frame, orient="horizontal")
    scrollbar_x.pack(side="bottom", fill="x")

    book_canvas = Canvas(scroll_frame, bg="#FDFFE8", xscrollcommand=scrollbar_x.set,
                        highlightthickness=3, highlightbackground="black")
    book_canvas.pack(side="left", fill="both", expand=True)
    scrollbar_x.config(command=book_canvas.xview)


    image_references = []

    # Function display book images and details
    def display_book_images(book_info):
        nonlocal image_references
        image_references.clear()  # Clear previous references
        for widget in book_canvas.winfo_children():
            widget.destroy()

        x_offset = 50
        for i, ((book, rack_code), url) in enumerate(book_info):
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                response = requests.get(url, headers=headers,timeout=10)
                response.raise_for_status() 
                if response.status_code == 200:
                    img_data = BytesIO(response.content)
                    img = PILImage.open(img_data)
                    img = img.resize((150, 250), PILImage.LANCZOS)
                    tk_img = ImageTk.PhotoImage(img)

                    frame = Frame(book_canvas, bg="#FDFFE8", bd=10, relief="raised")
                    label_img = Label(frame, image=tk_img, bg="white")
                    label_img.image = tk_img
                    label_img.pack()

                    label_title = Label(frame, text=book, font=("Bahnschrift SemiLight", 16), bg="#FDFFE8", wraplength=250)
                    label_title.pack()

                    label_rack = Label(frame, text=f"Shelf: {rack_code.capitalize()}", font=("Bahnschrift SemiLight", 14), bg="#FDFFE8")
                    label_rack.pack()

                    book_canvas.create_window(x_offset, 40, anchor="nw", window=frame)
                    x_offset += 300  # Space each book

                    image_references.append(tk_img)
                else:
                    print(f"Failed to download image from {url}: HTTP Status Code {response.status_code}")
            except requests.HTTPError as e:
                print(f"Error loading image from {url}: {e}")
            except Exception as e:
                print(f"Error loading image from {url}: {e}")

        book_canvas.config(scrollregion=(0, 0, x_offset, 500))


    
    def fetch_rack_code(book_name):
        rack_code = final_rating.loc[final_rating['Book-Title'] == book_name, 'Storage-Rack'].values
        if len(rack_code) > 0:
            return rack_code[0]
        else:
            return ''

    def fetch_poster(suggestion):
        book_name = []
        ids_index = []
        poster_url = []

        for book_id in suggestion:
            book_name.append(book_pivot.index[book_id])

        for name in book_name[0]:
            ids = np.where(final_rating['Book-Title'] == name)[0][0]
            ids_index.append(ids)

        for idx in ids_index:
            url = final_rating.iloc[idx]['Image-URL-L']
            poster_url.append(url)

        return poster_url

    def recommend_book(book_name):
        books_list = []
        book_id = np.where(book_pivot.index == book_name)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=11)

        poster_url = fetch_poster(suggestion)

        recommended_books_info = []
        for i in range(len(suggestion[0])):
            suggested_book = book_pivot.index[suggestion[0][i]]
            if suggested_book != book_name:
                rack_code = fetch_rack_code(suggested_book)
                recommended_books_info.append((suggested_book, rack_code))
                if len(recommended_books_info) == 10:
                    break

        poster_url = [poster_url[i] for i in range(len(poster_url)) if book_pivot.index[suggestion[0][i]] in [book[0] for book in recommended_books_info]]

        return recommended_books_info, poster_url
    
       
    root.mainloop()

if __name__ == "__main__":
    root=Tk()
    RecommmenderBook(root)
    