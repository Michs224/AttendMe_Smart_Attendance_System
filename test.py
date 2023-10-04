import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle  # Import ttkthemes

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Percantik GUI Tkinter")

        # Buat ttkthemes style
        self.style = ThemedStyle(root)
        self.style.set_theme(theme_name="equilux")  # Ganti tema sesuai keinginan Anda

        # Tambahkan tombol dengan tampilan yang didefinisikan oleh tema
        self.button = ttk.Button(root, text="Tombol dengan Gaya", command=self.say_hello)
        self.button.pack(pady=20)

    def say_hello(self):
        print("Hello, World!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
