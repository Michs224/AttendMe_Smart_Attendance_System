from pathlib import Path
import cv2
import os

from tkinter import RIDGE, Frame, Label, StringVar, Tk,messagebox, ttk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter.font import Font
import mysql.connector
from datetime import datetime



def to_images(str):
    return Path(__file__).resolve().parent /"Images/frame_2" / str

def Student_Details(root):
    # window = root
    Entry_font=Font(family="Bahnschrift SemiLight",size=16)
    
    root.geometry("2560x1600")
    root.configure(bg = "#FDFFE8")
    root.title("LibraLink: Student Details")

    canvas = Canvas(root,bg = "#FDFFE8",height = 1600,width = 2560,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0) 
    
    canvas.create_text(
        700.0,
        95.0,
        anchor="nw",
        text="STUDENT MANAGEMENT SYSTEM",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 90 * -1)
    )
    
    canvas.create_text(
        1110.0,
        340.0,
        anchor="nw",
        text="Student Details",
        fill="#EF16A5",
        font=("Bahnschrift SemiBold SemiConden", 55 * -1)
    )
    
    canvas.create_text(
        151.0,
        473.0,
        anchor="nw",
        text="Current Course Information",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 30 * -1)
    )
    canvas.create_text(
        211.0,
        686.0,
        anchor="nw",
        text="Year",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 25 * -1)
    )
    canvas.create_text(
        732.0,
        589.0,
        anchor="nw",
        text="Course",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 25 * -1)
    )

    canvas.create_text(
        732.0,
        688.0,
        anchor="nw",
        text="Semester",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 25 * -1)
    )

    canvas.create_text(
        211.0,
        589.0,
        anchor="nw",
        text="Department",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiCondenr", 25 * -1)
    )

    canvas.create_text(
        151.0,
        800.0,
        anchor="nw",
        text="Class Student Information",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 30 * -1)
    )
    
    canvas.create_text(
        676.0,
        1104.0,
        anchor="nw",
        text="Date Of Birth             :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiCondenr", 26 * -1)
    )

    canvas.create_text(
        676.0,
        1188.0,
        anchor="nw",
        text="Phone Number         :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1)
    )

    canvas.create_text(
        676.0,
        928.8466796875,
        anchor="nw",
        text="Student Name           :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1)
    )

    canvas.create_text(
        172.0,
        1188.0,
        anchor="nw",
        text="Email                    :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1)
    )

    canvas.create_text(
        676.0, 
        1019.0,
        anchor="nw",
        text="Address                     :",
        fill="#000000", 
        font=("Bahnschrift SemiBold SemiConden", 26 * -1))

    canvas.create_text(
        172.0,
        931.0,
        anchor="nw",
        text="Student ID             :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1))

    canvas.create_text(
        172.0,
        1017.0,
        anchor="nw",
        text="Class Division       :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1))
    
    canvas.create_text(172.0,1104.0,
        anchor="nw",
        text="Gender                  :",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 26 * -1))
    
    canvas.create_text(
        1328.0,
        485.0,
        anchor="nw",
        text="Search System",
        fill="#000000",
        font=("Bahnschrift SemiBold SemiConden", 35 * -1))

    
    # Variables
    var_dep=StringVar()
    var_course=StringVar()
    var_year=StringVar()
    var_semester=StringVar()
    var_std_id=StringVar()
    var_std_name=StringVar()
    var_classdiv=StringVar()
    var_gender=StringVar()
    var_dob=StringVar()
    var_email=StringVar()
    var_phone=StringVar()
    var_address=StringVar()
    
    
    # ComboBox
        
    # Department
    dep_combo = ttk.Combobox(root,textvariable=var_dep,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly",style="Custom.TCombobox")
    dep_combo["values"]=("Select Department","School of Computer Science",
                        "School of Information Systems",
                        "School of Design",
                        "Faculty of Engineering","BINUS Business School")
    dep_combo.current(0)
    canvas.create_window(510.5, 608.0, window=dep_combo, width=300, height=40)
    
    # Course
    course_combo = ttk.Combobox(root,textvariable=var_course,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    course_combo["values"]=("Select Course","Computer Science",
                        "Information System",
                        "Design Communication Visual",
                        "Industrial Engineering","Digital Business")
    course_combo.current(0)
    canvas.create_window(994.5,608.0, window=course_combo, width=300, height=40)
    
    
    # Semester
    semester_combo = ttk.Combobox(root,textvariable=var_semester,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    semester_combo["values"]=("Select Semester",1,2,3,4,5,6,7,8,9,10)
    semester_combo.current(0)
    canvas.create_window(994.5,701.0, window=semester_combo, width=300, height=40)
    
    # Year
    year_combo = ttk.Combobox(root,textvariable=var_year,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    year_combo["values"]=("Select Year",
                        "2020/2021",
                        "2021/2022",
                        "2022/2023",
                        "2023/2024",
                        "2024/2025",
                        "2025/2026",
                        "2026/2027")
    year_combo.current(0)
    canvas.create_window(510.5,701.0, window=year_combo, width=300, height=40)   
    
    
    # Entry Image
    entry_image = PhotoImage(file=to_images("entry_1.png"))
    
    
    # Inputan 
    entry_bg_1 = canvas.create_image(509.0,951.0,image=entry_image)
    entry_std_id = Entry(root, textvariable=var_std_id,bd=0,bg="#FDFFE8",fg="#000716",highlightthickness=0, font=Entry_font)
    entry_std_id.place(x=384.0,y=930.0,width=250.0,height=40.0)

    entry_bg_2 = canvas.create_image(1053.0,951.0,image=entry_image)
    entry_std_name = Entry(root,textvariable=var_std_name,bd=0,bg="#FDFFE8",fg="#000716", highlightthickness=0,font=Entry_font)
    entry_std_name.place(x=928.0, y=930.0, width=250.0, height=40.0)

    # entry_bg_3 = canvas.create_image(509.0,1119.0,image=entry_image)
    # entry_gender = Entry(root,textvariable=var_gender,bd=0,bg="#FDFFE8",fg="#000716",highlightthickness=0, font=Entry_font)
    # entry_gender.place(x=384.0, y=1099.0, width=250.0, height=40.0)

    gender_combo = ttk.Combobox(root,textvariable=var_gender,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    gender_combo["values"]=("Male","Female","Other")
    gender_combo.current(0)
    canvas.create_window(509.0,1125.0, window=gender_combo, width=250, height=40.)
    
    
    # entry_bg_4 = canvas.create_image(509.0,1036.0,image=entry_image)
    # entry_class = Entry(root,textvariable=var_classdiv,bd=0,bg="#FDFFE8",fg="#000716",highlightthickness=0,font=Entry_font)
    # entry_class.place( x=384.0, y=1015.0,width=250.0, height=40.0)
    
    classdiv_combo = ttk.Combobox(root,textvariable=var_classdiv,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    classdiv_combo["values"]=("Select Class Division","LA","LB","LC","LD","LE")
    classdiv_combo.current(0)
    canvas.create_window(509.0,1037.0, window=classdiv_combo, width=250, height=40.)
    
    entry_bg_5 = canvas.create_image(1053.0,1119.0,image=entry_image)
    entry_dob = Entry(root,bd=0,textvariable=var_dob,bg="#FDFFE8",fg="#000716",highlightthickness=0,font=Entry_font )
    entry_dob.place(x=928.0,y=1099.0,width=250.0,height=39.0)

    entry_bg_6 = canvas.create_image( 1053.0,1205.0,image=entry_image)
    entry_phone = Entry(root,bd=0, textvariable=var_phone,bg="#FDFFE8",fg="#000716",highlightthickness=0,font=Entry_font)
    entry_phone.place(x=928.0,y=1185.0,width=250.0, height=39.0)

    entry_bg_7 = canvas.create_image(509.0,1205.0,image=entry_image)
    entry_email = Entry(root,bd=0,textvariable=var_email,bg="#FDFFE8",fg="#000716",highlightthickness=0, font=Entry_font)
    entry_email.place(x=384.0,y=1185.0,width=250.0,height=39.0)

    entry_bg_8 = canvas.create_image(1053.0,1035.0,image=entry_image) 
    entry_addr = Entry(root,textvariable=var_address,bd=0,bg="#FDFFE8",fg="#000716",highlightthickness=0,font=Entry_font)
    entry_addr.place( x=928.0,y=1015.0,width=250.0,height=39.0)

    style = ttk.Style()
    style.configure("Custom.TRadiobutton", background="#FDFFE8",font=("Bahnschrift SemiCondensed", 16))


    # Radio Button
    var_radio1=StringVar()
    radiobutton_1 =ttk.Radiobutton(root, variable=var_radio1,text="Take Photo Sample", value="Yes",style="Custom.TRadiobutton")
    radiobutton_1.place(x=170.0,y=1260.0)
    radiobutton_2=ttk.Radiobutton(root,variable=var_radio1,text="No Photo Sample",value="None",style="Custom.TRadiobutton")
    radiobutton_2.place(x=450.0,y=1260.0)
    
    
    
    
    # ====================== Function-Functions ==================
    
    import os
    import platform
    import winsound
    
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
    
    def is_valid_date(date):
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return True
        except ValueError:
            return False
    def is_valid_phone(phone):
        if phone[0] == "6" and phone[1] == "2":
            return True
        else:
            return False
        
    def AddData():
        global __error
        # if not str(var_std_id.get()).isdigit():
        #         show_custom_error("Error, Due to : 4025 (23000): CONSTRAINT 'Check_StudentID' failed for 'libralink_attendance_db'.'students'")
        if var_dep.get()=="Select Department" or var_course.get()=="Select Course" or var_year.get()=="Select Year" or var_semester.get()=="Select Semester" or var_std_id.get()=="" or var_std_name.get()=="" or var_classdiv.get()=="":
            show_custom_error("All fields are required!")
        elif var_dob.get() not in["None",""] and not is_valid_date(var_dob.get()):
            show_custom_error("Date of Birth must be in YYYY-MM-DD format!")
        elif not is_valid_phone(var_phone.get()):
            show_custom_error('Phone number must start with "62"')            
        else:
            try:
                if str(var_std_id.get()).isdigit():
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="libralink_attendance_db")
                    my_cursor=conn.cursor()
                    
                    Listadded1=[]
                    Listadded2=[]
                    
                    Listadded1.append("Department")
                    Listadded2.append(var_dep.get())
                    
                    Listadded1.append("Course")
                    Listadded2.append(var_course.get())
                    
                    Listadded1.append("Year")
                    Listadded2.append(var_year.get())
                    
                    Listadded1.append("Semester")
                    Listadded2.append(var_semester.get())
                    
                    Listadded1.append("StudentID")
                    Listadded2.append(var_std_id.get())
                
                    Listadded1.append("StudentName")
                    Listadded2.append(var_std_name.get())
                    
                    Listadded1.append("ClassDivision")
                    Listadded2.append(var_classdiv.get())
                    
                    Listadded1.append("Gender")
                    Listadded2.append(var_gender.get())
                        
                    if var_dob.get()!="" and var_dob.get()!="None":
                        Listadded1.append("DateOfBirth")
                        Listadded2.append(var_dob.get())
                        
                    if var_email.get()!="" and var_email.get()!="None":
                        Listadded1.append("Email")
                        Listadded2.append(var_email.get())
                        
                    if var_phone.get()!="" and var_phone.get()!="None":
                        Listadded1.append("PhoneNumber")
                        Listadded2.append(var_phone.get())
                        
                    if var_address.get()!="" and var_address.get()!="None":
                        Listadded1.append("Address")
                        Listadded2.append(var_address.get())
                        
                    if var_radio1.get()!="" and var_radio1.get()!="None":
                        Listadded1.append("PhotoSample")
                        Listadded2.append(var_radio1.get())
                    
                    # bisa gini 
                    
                    # str1=""
                    # str2=""
                    # # # print(Listadded1[0])
                    # # # print(Listadded2[0])

                    # for item1,item2 in zip(Listadded1,Listadded2):
                    #     str1 += item1 + ','
                    #     if item2.isdigit() and item2!=var_std_id.get():
                    #         str2 += f"{int(item2)},"
                    #     elif isinstance(item2,str):
                    #         str2+=  f"'{item2}',"

                    # # Menghapus tanda koma terakhir
                    # str1 = str1.rstrip(',')
                    # str2 = str2.rstrip(',')
                    
                    # print(str1)
                    # print(str2)
                    
                    
                    # Atau bisa gini juga, tapi pakai placeholder sama Listadded2 bukan cuma str2
                    column_names = ','.join(Listadded1)
                    print(column_names)
                    placeholders = ','.join(['%s' for _ in Listadded2])
                    query = f"INSERT INTO Students ({column_names}) VALUES({placeholders})"
                    # print(query,Listadded2)
                    # print()
                    my_cursor.execute(query,Listadded2)
                    # print(column_names, placeholders,Listadded2)
                    # else:
                    #     my_cursor.execute("INSERT INTO Students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    #         var_dep.get(),
                    #         var_course.get(),
                    #         var_year.get(),
                    #         var_semester.get(),
                    #         var_std_id.get(),
                    #         var_std_name.get(),
                    #         var_classdiv.get(),
                    #         var_gender.get(),                
                    #         var_dob.get(),
                    #         var_email.get(),
                    #         var_phone.get(),
                    #         var_address.get(),
                    #         var_radio1.get()
                    #     ))
                    conn.commit()
                    fetchData()
                    conn.close()
                    show_custom_success("Data has been successfully added!")
                else:
                    show_custom_error("Error, Due to : 4025 (23000): CONSTRAINT 'Check_StudentID' failed for 'libralink_attendance_db'.'students'")
            except Exception as es:
                # global __error
                __error=f"Error, Due to : {str(es)}"
                show_custom_error(__error) 
    
    # ============== Fetch Data ==========================
    def fetchData():
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="libralink_attendance_db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM Students")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            student_table.delete(*student_table.get_children())
            for i in data:
                student_table.insert("","end",values=i)
            conn.commit()
        conn.close()
        
    # ============== Get Cursor ====================
    def getCursor(event=""):
        cursor_focus=student_table.focus()
        content=student_table.item(cursor_focus)
        data=content["values"]
        
        var_dep.set(data[0])
        var_course.set(data[1])
        var_year.set(data[2])
        var_semester.set(data[3])
        var_std_id.set(data[4])
        var_std_name.set(data[5])
        var_classdiv.set(data[6])
        var_gender.set(data[7])
        var_dob.set(data[8])
        var_email.set(data[9])
        var_phone.set(data[10])
        var_address.set(data[11])
        var_radio1.set(data[12])


    # ============== Update ====================
    def askConfirmation(message):
        # Suara buat ask
        os_name = platform.system()
        if os_name == "Windows":
            winsound.MessageBeep(winsound.MB_ICONASTERISK) 
        elif os_name == "Darwin":  # Alias untuk macOS
            os.system('osascript -e "beep"')
        elif os_name == "Linux":
            os.system('spd-say "success"')

        # Window baru
        confirmation_window = Toplevel()
        confirmation_window.title("Success Message")
        confirmation_window.geometry("400x215")
        confirmation_window.config(bg='#c9eff2')
        confirmation_window.resizable(False, False)

        # Biar gak bisa interact ke window lain, harus klik di success dahulu
        confirmation_window.grab_set()

        # Frame buat konten
        frame = Frame(confirmation_window, bg='#c9eff2')
        frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Label buat pesan sukses
        Label(frame, text="Confirmation!", font=("Bahnschrift SemiCondensed", 25, 'bold'), bg='#c9eff2', fg='#006400').pack(pady=(10, 0))
        Label(frame, text=message, font=("Bahnschrift SemiCondensed", 16), bg='#c9eff2', fg='#333333').pack(pady=5)

        # Label untuk button
        button_frame = Frame(frame, bg='#c9eff2')
        button_frame.pack(pady=10)
        

        def if_yes():
            confirmation_window.destroy()
            if message=="Do you want to update this student data?":
                perform_update()
            elif message=="Do you want to delete this student data?":
                perform_delete()
        def if_no():
            confirmation_window.destroy()


        Button(button_frame, text="Sure", command=if_yes, font=("Bahnschrift SemiCondensed", 16), bg='#006400', fg='white', bd=0).pack(side="left",padx=15,pady=10, ipadx=5,ipady=3)
        Button(button_frame, text="No", command=if_no, font=("Bahnschrift SemiCondensed", 16), bg='#006400', fg='white', bd=0).pack(side="right",padx=15,pady=10, ipadx=13,ipady=3)
       
    
    
    def updateData():
        if not str(var_std_id.get()).isdigit():
            show_custom_error("Error, Due to : 4025 (23000): CONSTRAINT 'Check_StudentID' failed for 'libralink_attendance_db'.'students'")
        elif var_dep.get()=="Select Department" or var_course.get()=="Select Course" or var_year.get()=="Select Year" or var_semester.get()=="Select Semester" or var_std_id.get()=="" or var_std_name.get()=="" or var_classdiv.get()=="":
            show_custom_error("All fields are required!")
        elif var_dob.get() not in["None",""] and not is_valid_date(var_dob.get()):
            show_custom_error("Date of Birth must be in YYYY-MM-DD format!")
        elif not is_valid_phone(var_phone.get()):
            show_custom_error('Phone number must start with "62"')
        else:
            askConfirmation("Do you want to update this student data?")
            
    def perform_update():
        global __error
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="libralink_attendance_db")
            my_cursor=conn.cursor()
            
            Listadded1=[]
            Listadded2=[]
            
            Listadded1.append("Department")
            Listadded2.append(var_dep.get())
            
            Listadded1.append("Course")
            Listadded2.append(var_course.get())
            
            Listadded1.append("Year")
            Listadded2.append(var_year.get())
            
            Listadded1.append("Semester")
            Listadded2.append(var_semester.get())
            
            # Listadded1.append("StudentID")
            # Listadded2.append(var_std_id.get())
            # std_id=var_std_id.get()
        
            Listadded1.append("StudentName")
            Listadded2.append(var_std_name.get())
            
            Listadded1.append("ClassDivision")
            Listadded2.append(var_classdiv.get())
            
            Listadded1.append("Gender")
            Listadded2.append(var_gender.get())
                
            if var_dob.get()!="" and var_dob.get()!="None":
                Listadded1.append("DateOfBirth")
                Listadded2.append(var_dob.get())
                
            if var_email.get()!="" and var_email.get()!="None":
                Listadded1.append("Email")
                Listadded2.append(var_email.get())
                
            if var_phone.get()!="" and var_phone.get()!="None":
                Listadded1.append("PhoneNumber")
                Listadded2.append(var_phone.get())
                
            if var_address.get()!="" and var_address.get()!="None":
                Listadded1.append("Address")
                Listadded2.append(var_address.get())
                
            if var_radio1.get()!="" and var_radio1.get()!="None":
                Listadded1.append("PhotoSample")
                Listadded2.append(var_radio1.get())
            student_id=var_std_id.get()
            print(Listadded1)
            print(Listadded2)
            # print(var_std_id.get())    
            Listadded3 = []
            for i, j in zip(Listadded1, Listadded2):
                # Kalau j int
                if j.isdigit() and j!=var_phone.get():
                    j = int(j)
                # Kalau j string
                elif isinstance(j, str):
                    j = f"'{j}'"
                Listadded3.append(f"{i}={j}")
            query = f"UPDATE Students SET {','.join(Listadded3)} WHERE StudentID='{student_id}'"
            print(query)
            my_cursor.execute(query)
            conn.commit()
            fetchData()
            conn.close()
            show_custom_success("Data has been successfully updated!")
        except Exception as es:
            __error=f"Error, Due to : {str(es)}"
            show_custom_error(__error)
    
    
    # ========== Delete ==============
    def deleteData():
        global __error
        if var_std_id.get()=="":
            show_custom_error("Student ID is required!")
        elif not str(var_std_id.get()).isdigit():
            show_custom_error("Error, Due to : 4025 (23000): CONSTRAINT 'Check_StudentID' failed for 'libralink_attendance_db'.'students'")
        else:
            try:
                askConfirmation("Do you want to delete this student data?")
            except Exception as es:
                __error=f"Error, Due to : {str(es)}"
                show_custom_error(__error)
                 
    def perform_delete():
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="libralink_attendance_db")
        my_cursor=conn.cursor()
        query="DELETE FROM Students WHERE StudentID="+var_std_id.get()
        # print(query)
        my_cursor.execute(query)       
        conn.commit()
        fetchData()
        conn.close()
        show_custom_success("Data has been successfully deleted!")


        
        
    # ============ Reset =============
    def resetData():
        var_dep.set("Select Department")
        var_course.set("Select Course")
        var_year.set("Select Year")
        var_semester.set("Select Semester")
        var_std_id.set("")
        var_std_name.set("")
        var_classdiv.set("Select Class Division")
        var_gender.set("Male")
        var_dob.set("")
        var_email.set("")
        var_phone.set("")
        var_address.set("")
        var_radio1.set("")
        
        
        
    # ========== Generate dataset/take photo sample ==========
    def generateDataset():
        # print(var_std_id.get())
        if var_radio1.get() =="Yes":
            global __error
            if not str(var_std_id.get()).isdigit():
                show_custom_error("Error, Due to : 4025 (23000): CONSTRAINT 'Check_StudentID' failed for 'libralink_attendance_db'.'students'")
            elif var_dep.get()=="Select Department" or var_course.get()=="Select Course" or var_year.get()=="Select Year" or var_semester.get()=="Select Semester" or var_std_id.get()=="" or var_std_name.get()=="" or var_classdiv.get()=="":
                show_custom_error("All fields are required!")
            elif var_dob.get() not in["None",""] and not is_valid_date(var_dob.get()):
                show_custom_error("Date of Birth must be in YYYY-MM-DD format!") 
            elif not is_valid_phone(var_phone.get()):
                show_custom_error('Phone number must start with "62"')   
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="libralink_attendance_db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("SELECT * FROM Students")                  
                    myresult=my_cursor.fetchall()
                    id=0
                    # print(var_std_id.get()) 
                    for x in myresult:
                        id+=1
                    if id==0:
                        show_custom_error("No Students Data!")
                        return
                    # print(var_std_id.get())    
                    Listadded1=[]
                    Listadded2=[]
                    
                    Listadded1.append("Department")
                    Listadded2.append(var_dep.get())
                    
                    Listadded1.append("Course")
                    Listadded2.append(var_course.get())
                    
                    Listadded1.append("Year")
                    Listadded2.append(var_year.get())
                    
                    Listadded1.append("Semester")
                    Listadded2.append(var_semester.get())
                    
                    # Listadded1.append("StudentID")
                    # Listadded2.append(var_std_id.get())
                
                    Listadded1.append("StudentName")
                    Listadded2.append(var_std_name.get())
                    
                    Listadded1.append("ClassDivision")
                    Listadded2.append(var_classdiv.get())
                    
                    Listadded1.append("Gender")
                    Listadded2.append(var_gender.get())
                        
                    if var_dob.get()!="" and var_dob.get()!="None":
                            Listadded1.append("DateOfBirth")
                            Listadded2.append(var_dob.get())
                            
                    if var_email.get()!="" and var_email.get()!="None":
                        Listadded1.append("Email")
                        Listadded2.append(var_email.get())
                        
                    if var_phone.get()!="" and var_phone.get()!="None":
                        Listadded1.append("PhoneNumber")
                        Listadded2.append(var_phone.get())
                        
                    if var_address.get()!="" and var_address.get()!="None":
                        Listadded1.append("Address")
                        Listadded2.append(var_address.get())
                        
                    if var_radio1.get()!="" and var_radio1.get()!="None":
                        Listadded1.append("PhotoSample")
                        Listadded2.append(var_radio1.get())
                    # print(var_radio1.get())
                    student_id=var_std_id.get()
                    # print(Listadded1,Listadded2)
                    Listadded3 = []
                    for i, j in zip(Listadded1, Listadded2):
                        # Kalau j int
                        if j.isdigit():
                            j = int(j)
                        # Kalau j string
                        elif isinstance(j, str):
                            j = f"'{j}'"
                        Listadded3.append(f"{i}={j}")
                    # print(Listadded3)
                    query = f"UPDATE Students SET {', '.join(Listadded3)} WHERE StudentID='{student_id}'"
                    my_cursor.execute(query)
                    conn.commit()
                    fetchData()
                    resetData()
                    conn.close()
                    
                    
                    
                    # ========= Load data on face frontals from opencv =========
                    
                    face_classifier=cv2.CascadeClassifier("./Haarcascade/haarcascade_frontalface_default.xml")
                    
                    def faceCropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        # Scaling factor=1.3
                        # Minimum Neighbor=5
                        for x,y,w,h in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                        
                    if not os.path.exists("Photo Data/"+"StudentID_"+student_id):
                        os.makedirs("Photo Data/"+"StudentID_"+student_id)
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if faceCropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(faceCropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            # student_id=var_std_id.get()
                            # file_name_path = f"Photo Data/{student_id}_{img_id}.jpg"
                            file_name_path="Photo Data/"+"StudentID_"+student_id+"/"+student_id+"_"+str(img_id)+".jpg"
                            # print(file_name_path)
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            cv2.imshow("Cropped Face",face)
                        
                        if cv2.waitKey(1)==13 or int(img_id)==500:
                            break
                    cap.release()
                    cv2.destroyAllWindows()               
                    show_custom_success("Dataset has been successfully generated!")
                except Exception as es:
                    __error=f"Error, Due to : {str(es)}"
                    show_custom_error(__error)
        else:
            show_custom_error('"Take Photo Sample" must be filled!')
              
                
                    
                    
                    
                    
    # Button
    button_image_1 = PhotoImage(file=to_images("button_1.png"))
    button_add = Button(root,image=button_image_1,borderwidth=3,highlightthickness=0, command=AddData, relief="flat")
    button_add.place(x=167.0, y=1305.0, width=228.0, height=50.0)

    button_image_2 = PhotoImage(file=to_images("button_2.png"))
    button_takePhoto = Button(root,image=button_image_2, borderwidth=3,highlightthickness=0, command=generateDataset, relief="flat")
    button_takePhoto.place(x=167.0,y=1373.0, width=486.0,  height=50.0)

    button_image_3 = PhotoImage(file=to_images("button_3.png"))
    button_updatePhoto = Button(root,image=button_image_3,borderwidth=3,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
    button_updatePhoto.place(x=689.0,y=1373.0,width=486.0, height=50.0 )

    button_image_4 = PhotoImage(file=to_images("button_4.png"))
    button_updateData = Button(root, image=button_image_4,borderwidth=3, highlightthickness=0, command=updateData, relief="flat")
    button_updateData.place(x=425.0, y=1305.0, width=228.0,  height=50.0)

    button_image_5 = PhotoImage(file=to_images("button_5.png"))
    button_delete = Button(root, image=button_image_5,  borderwidth=3,  highlightthickness=0,  command=deleteData,  relief="flat")
    button_delete.place(x=689.0,y=1305.0, width=228.0,  height=50.0)

    button_image_6 = PhotoImage( file=to_images("button_6.png"))
    button_reset = Button(root,  image=button_image_6, borderwidth=3, highlightthickness=0, command=resetData,  relief="flat")
    button_reset.place(x=947.0, y=1305.0, width=228.0,  height=50.0)



    # Line Line Border
    
    # Logo
    image_image_logo = PhotoImage(file=to_images("image_logo.png"))
    image_3 = canvas.create_image(2351.0,  170.0,image=image_image_logo)
    
    canvas.create_rectangle( 2121.0,  34.0,  2129.0, 242.0, fill="#EF16A5",outline="")

    
    canvas.create_rectangle(76.0,373.0,81.0,1523.0,fill="#000000",outline="")

    canvas.create_rectangle(78.0,373.0,1030.0,379.0,fill="#000000",outline="")

    canvas.create_rectangle(76.0,1527.0,1252.0,1523.0,fill="#000000",outline="")

    canvas.create_rectangle(1248.0,415.0,1252.0,1527.0,fill="#000000",outline="")

    
    canvas.create_rectangle(141.0,842.0,143.0,1455.0,fill="#000000",outline="")

    canvas.create_rectangle(141.0,1452.0,1205.0,1457.0,fill="#000000",outline="")

    canvas.create_rectangle(1204.0,826.0,1206.0,1455.0,fill="#000000",outline="")

    canvas.create_rectangle(523.0,825.0,1206.0,827.0,fill="#000000",outline="")
    

    canvas.create_rectangle(140.0,513.0,143.0,757.0,fill="#F017A6",outline="")

    canvas.create_rectangle(142.0,755.0,1206.0,757.0,fill="#F017A6",outline="")

    canvas.create_rectangle(1204.0,498.0,1206.0,757.0,fill="#F017A6",outline="")

    canvas.create_rectangle(538.0,497.0,1205.0,500.0,fill="#F017A6",outline="")
    

    canvas.create_rectangle(1278.0,416.0,1282.0,1526.0,fill="#000000",outline="")

    canvas.create_rectangle(1278.0,1524.0,2501.0,1528.0,fill="#000000",outline="")

    canvas.create_rectangle(2495.0, 380.0,2501.0, 1527.0,fill="#000000",outline="")

    canvas.create_rectangle(1527.0,376.0,2501.0,382.0,fill="#000000",outline="")

    
    
    canvas.create_rectangle(1301.0,504.0,1303.0,656.0,fill="#25B0FF",outline="")

    canvas.create_rectangle(1302.0,654.0,2475.0,656.0,fill="#25B0FF",outline="")

    canvas.create_rectangle(1301.0,504.0,1316.0,506.0,fill="#25B0FF",outline="")

    canvas.create_rectangle(2472.0,507.0,2475.0,656.0,fill="#25B0FF",outline="")

    canvas.create_rectangle(1577.0,505.0,2475.0,507.0,fill="#25B0FF",outline="")



    # ----------------- Search System --------------------
    
    # Search Combo
    search_combo = ttk.Combobox(root,font=Font(family="Bahnschrift SemiCondensed",size=16),state="readonly")
    search_combo["values"]=("Select","Student ID","Phone Number")
    search_combo.current(0)
    canvas.create_window(1610.0,590.0, window=search_combo, width=270, height=45)
    
    
    entry_image_9 = PhotoImage(file=to_images("entry_9.png"))
    entry_bg_9 = canvas.create_image(1904.5,591.0,image=entry_image_9)
    entry_search = Entry(root,bd=0,bg="#FDFFE8",fg="#000716",highlightthickness=0,font=Entry_font)
    entry_search.place(x=1780.0,y=571.0,width=250.0,height=40.0)
    
    canvas.create_text(1315.0,  573.0, anchor="nw",  text="Search by :", fill="#000000",   font=("Bahnschrift SemiBold SemiConden", 30 * -1))

    image_image_1 = PhotoImage(file=to_images("image_1.png"))
    image_1 = canvas.create_image(  2150.0, 589.0,  image=image_image_1)
    canvas.tag_bind(image_1, '<Enter>', lambda event, img=image_1 :on_image_enter(img))
    canvas.tag_bind(image_1, '<Leave>', lambda event, img=image_1 :on_image_leave(img))
    canvas.tag_bind(image_1, '<Button-1>', lambda event, img=image_1: on_image_click(img))   


    image_image_2 = PhotoImage(file=to_images("image_2.png"))
    image_2 = canvas.create_image(2337.0,  589.0, image=image_image_2)
    canvas.tag_bind(image_2, '<Enter>', lambda event, img=image_2 :on_image_enter(img))
    canvas.tag_bind(image_2, '<Leave>', lambda event, img=image_2 :on_image_leave(img))
    canvas.tag_bind(image_2, '<Button-1>', lambda event, img=image_2: on_image_click(img))      
    
    
    # Function buat animasi
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
        # if image==image_4:
        #     animate_image(image, 3, 8, -3, -8)
        #     new_window=Toplevel(root)
        #     LibraLink(new_window)
        # elif image==image_10:
        #     animate_image(image, 3, 8, -3, -8)
        #     new_window=Toplevel(root)
        #     from TakeAttendanceStudents import Take_Attendance_Students
            # Take_Attendance_Students(new_window)
        # else:
        animate_image(image, 2, 5, -2, -5)  # Animasi

    def on_image_enter(image):
        zoom_in_image(image)
        canvas.config(cursor="hand2")
        # canvas.update()
        
    def on_image_leave(image):
        zoom_out_image(image)
        canvas.config(cursor="")
        # canvas.update()
            
    # ------ Table Frame -------
    table_frame=Frame(root,bd=2,bg="#FDFFE8",relief="solid")
    table_frame.place(x=1300.0,y=680.0,width=1175,height=777)
    
    scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
    scroll_y=ttk.Scrollbar(table_frame,orient="vertical")
    
    columns=["dep","course","year","sem","stdid","name","classdiv","gender",
    "dob","email","phone","address","photo"]
    
    student_table=ttk.Treeview(table_frame,column=columns,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
    style.configure("Treeview", font=("Bahnschrift SemiLight", 14))
    style.configure("Treeview.Heading", font=("Bahnschrift SemiCondensed", 16)) 

    
    scroll_x.pack(side="bottom",fill="x")
    scroll_y.pack(side="right",fill="y")
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    student_table.heading("dep",text="Department")
    student_table.heading("course",text="Course")
    student_table.heading("year",text="Year")
    student_table.heading("sem",text="Semester")
    student_table.heading("stdid",text="Student ID")
    student_table.heading("name",text="Student Name")
    student_table.heading("classdiv",text="Class Division")
    student_table.heading("gender",text="Gender")
    student_table.heading("dob",text="DOB")
    student_table.heading("email",text="Email")
    student_table.heading("phone",text="Phone Number")
    student_table.heading("address",text="Address")
    student_table.heading("photo",text="Photo Sample Status")
    student_table["show"]="headings"
    
    for i in columns:
        student_table.column(i,minwidth=150,width=250)
    
    student_table.pack(fill="both",expand=True)
    student_table.bind("<ButtonRelease>",getCursor)
    fetchData()
       

    # root.resizable(False, False)
    # root.overrideredirect(True)
    root.mainloop()


if __name__ == "__main__":
    root=Tk()
    Student_Details(root)
    # root.mainloop()