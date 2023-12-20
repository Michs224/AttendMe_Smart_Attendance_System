from pathlib import Path
import platform
from tkinter import Frame, Image, Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import os
import winsound
from PIL import Image
# from StudentDetails import show_custom_error,show_custom_success
import cv2
import numpy as np
import pickle

def show_custom_success(message):
    # Suara buat sukses
    os_name = platform.system()
    if os_name == "Windows":
        winsound.MessageBeep(winsound.MB_ICONASTERISK) 
    elif os_name == "Darwin":  # Alias untuk macOS
        os.system('osascript -e "beep"')
    elif os_name == "Linux":
        os.system('spd-say "success"')

    # Window baru
    success_window = Toplevel()
    success_window.title("Success Message")
    success_window.geometry("400x215")
    success_window.config(bg='#a0d995')
    success_window.resizable(False, False)

    # Biar gak bisa interact ke window lain, harus klik di success dahulu
    success_window.grab_set()

    # Frame buat konten
    frame = Frame(success_window, bg='#a0d995')
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    # Label buat pesan sukses
    Label(frame, text="Success!", font=("Bahnschrift SemiCondensed", 25, 'bold'), bg='#a0d995', fg='#006400').pack(pady=(10, 0))
    Label(frame, text=message, font=("Bahnschrift SemiCondensed", 16), bg='#a0d995', fg='#333333').pack(pady=10)

    ok_button = Button(frame, text="OK", command=success_window.destroy, font=("Bahnschrift SemiCondensed", 16), bg='#006400', fg='white', bd=0)
    ok_button.pack(pady=10, ipadx=10)
    
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
    
    
def TrainData():
    global __error
    try:
        data_dir = "Photo Data"
        data_paths = []
        nim_to_id = {}
        id_to_nim = {}
        current_id = 1

        for nim_folder in os.listdir(data_dir):
            nim_path = os.path.join(data_dir, nim_folder)
            nim = int(nim_folder.split('_')[1])
            if nim not in nim_to_id:
                nim_to_id[nim] = current_id
                id_to_nim[current_id] = nim
                current_id += 1

            for image_file in os.listdir(nim_path):
                data_paths.append((os.path.join(nim_path, image_file), nim_to_id[nim]))

        faces = []
        ids = []
        for image_path, id in data_paths:
            # img=cv2.imread(image_path)
            img = Image.open(image_path).convert('L')
            image_np = np.array(img, 'uint8')
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1)

        ids = np.array(ids)
        print(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        print(faces,ids)
        if not os.path.exists("Model"):
            os.makedirs("Model")
        clf.write("Model/Classifier.xml")
        cv2.destroyAllWindows()
        show_custom_success("Training datasets has been completed!")

        # Simpan mapping
        with open('Model/id_to_nim_mapping_lbph.pkl', 'wb') as file:
            print(id_to_nim)
            pickle.dump(id_to_nim, file)

    except Exception as es:
        __error = f"Error, Due to : {str(es)}"
        show_custom_error(__error)
    


if __name__ == "__main__":
    # root=Tk()
    App=TrainData()
    # root.mainloop()