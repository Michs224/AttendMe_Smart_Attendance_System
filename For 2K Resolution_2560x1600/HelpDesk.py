from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def relative_to_assets(str):
    return Path(__file__).resolve().parent /"Images/helpdesk_frame" / str


def Help_Desk(root):
    
    # window = Tk()
    root.geometry("2560x1600")
    root.title("Libralink: Help Desk")
    root.configure(bg = "#FEFFF2")

    canvas = Canvas(root,bg = "#FEFFF2",height = 1600,width = 2560,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_logo.png"))
    image_1 = canvas.create_image(2351.0,170.0,image=image_image_1)

    canvas.create_rectangle(2121.0,34.0,2129.0,242.0,fill="#EF16A5",outline="")

    canvas.create_text(1462.0,95.0,anchor="nw",text="HELP DESK",fill="#000000",font=("RobotoRoman Bold", 100 * -1))

    image_image_2 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_2 = canvas.create_image(1980.569580078125,974.0101623535156,image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_3 = canvas.create_image(350.0,1157.0,image=image_image_3)

    canvas.create_text(185.0,398.0,anchor="nw",text="Please contact us",fill="#000000",font=("Ruluko", 100 * -1))

    canvas.create_text(206.0,212.0,anchor="nw",text="Need Help ?",fill="#000000",font=("Ruluko", 120 * -1))

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(726.0,1405.0,image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_5 = canvas.create_image(726.0,1173.0,image=image_image_5)

    image_image_6 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_6 = canvas.create_image(714.0,941.0,image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_7 = canvas.create_image(708.0,709.0,image=image_image_7)


    canvas.create_text(765.0,647.0,anchor="nw",text="(Developer)",fill="#000000",font=("Bahnschrift SemiCondensed", 40 * -1))
    canvas.create_text(768.0,872.0,anchor="nw",text="(Developer)",fill="#000000",font=("Bahnschrift SemiCondensed", 40 * -1))
    canvas.create_text(788.0,1107.0,anchor="nw",text="(Designer)",fill="#000000",font=("Bahnschrift SemiCondensed", 40 * -1))
    canvas.create_text(550.0,1342.0,anchor="nw",text="(Designer)",fill="#000000",font=("Bahnschrift SemiCondensed", 40 * -1))

    # root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    root=Tk()
    Help_Desk(root)
    # App.mainloop()
