
from pathlib import Path
import platform
import time
from tkinter import Frame, Image, Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import os
import winsound
from PIL import Image
import mysql.connector

import cv2
import numpy as np
from time import strftime
from datetime import datetime
import pickle
import csv
from plyer import notification

def MarkAttendance(sid, sn, c, cd):
    now = datetime.now()
    date_file = now.strftime("%Y-%m-%d") + ".csv"
    
    # Ganti dengan path yang sesuai di mana folder attendancedata akan dibuat
    path_attendance_data = Path("AttendanceData")

    if not path_attendance_data.exists():
        path_attendance_data.mkdir()

    pathdata = path_attendance_data / date_file

    # Mengecek file ada atau nggak, jika nggak, buat file baru.
    if not pathdata.exists():
        with open(pathdata, "w", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(["StudentID", "StudentName", "Course", "ClassDivision", "Date", "Time", "Status"])

    # Menulis data ke file
    with open(pathdata, "r+", newline="\n") as f:
        myDataList = f.readlines()
        name_list = []
        for line in myDataList:
            entry = line.split(",")
            name_list.append(entry[0])

        if ((sid not in name_list) and (sn not in name_list) and (c not in name_list) and (cd not in name_list)):
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{sid},{sn},{c},{cd},{now.strftime('%Y-%m-%d')},{dtString},Present")


    

def load_nim_to_id_mapping():
    with open('Model/id_to_nim_mapping_lbph.pkl', 'rb') as file:
        mapping = pickle.load(file)
        print("Loaded mapping:", mapping)
        return mapping

def Face_Recognition():
    id_to_nim = load_nim_to_id_mapping()

    def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for x, y, w, h in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            std_id_predict = id_to_nim.get(id, "Unknown")
            # print(std_id_predict,id)
            confidence = 100 * (1 - (predict / 300))

            
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="libralink_attendance_db")

            my_cursor = conn.cursor()

            my_cursor.execute(f"SELECT StudentName FROM Students WHERE StudentID={std_id_predict}")
            sn = my_cursor.fetchone()
            sn = "+".join([str(item) for item in sn]) if sn else "N/A"
            print(sn)
            my_cursor.execute(f"SELECT StudentID FROM Students WHERE StudentID={std_id_predict}")
            sid = my_cursor.fetchone()
            sid = "+".join([str(item) for item in sid]) if sid else "N/A"

            my_cursor.execute(f"SELECT Course FROM Students WHERE StudentID={std_id_predict}")
            c = my_cursor.fetchone()
            c = "+".join([str(item) for item in c]) if c else "N/A"

            my_cursor.execute(f"SELECT ClassDivision FROM Students WHERE StudentID={std_id_predict}")
            cd = my_cursor.fetchone()
            cd = "+".join([str(item) for item in cd]) if cd else "N/A"

            print(confidence)
            if confidence > 87:
                cv2.putText(img, f"Student ID : {sid}", (x, y - 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name : {sn}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Course : {c}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Class : {cd}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                
                cv2.putText(img, "Press Enter to Take Attendance", (30, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
                cv2.putText(img, "Hold Esc to Close", (1030, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
                key = cv2.waitKey(1)
                if key == 13:
                    MarkAttendance(sid, sn, c, cd)
                    cv2.putText(img, "Attendance Successful", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                    
                    notification.notify(
                        title="Attendance Marked",
                        message="Attendance has been marked successfully.",
                        # app_icon=None,
                        timeout=0.5
                    )
                    time.sleep(1)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, f"Unknown Face, please fill in your data through the librarian", (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, "Hold Esc to Close", (1030, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

            coord = [x, y, w, y]

        return coord

    def recognize(img, clf, faceCascade):
        coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return img

    faceCascade = cv2.CascadeClassifier("./Haarcascade/haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("./Model/Classifier.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, img = video_capture.read()
        img = recognize(img, clf, faceCascade)
        cv2.imshow("Let's Take Attendance", img)

        key = cv2.waitKey(1)
        if key==27:
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    App=Face_Recognition()