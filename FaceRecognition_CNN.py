from pathlib import Path
import platform
import time
from tkinter import Frame, Label, Tk, Button, PhotoImage, Toplevel
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
from keras.models import load_model
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras import layers, models


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

def preprocess_image_cnn(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    img_gray_resized = cv2.resize(img_gray, (450, 450))  
    img_gray_resized = img_gray_resized.reshape((450, 450, 1))  
    img_gray_resized = img_gray_resized / 255.0  
    return img_gray_resized


def load_nim_to_id_mapping():
    with open('Model/id_to_nim_mapping_cnn.pkl', 'rb') as file:
        mapping = pickle.load(file)
        print("Loaded mapping:", mapping)

        return mapping

def fetch_student_details_from_database(student_id):
    # Replace these database connection details with your actual values

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="libralink_attendance_db")
    cursor = conn.cursor()

    # Replace the SQL query with your actual query to fetch student details
    query = f"SELECT StudentName, Course, ClassDivision FROM Students WHERE StudentID={student_id}"

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            sn, c, cd = result
            return sn, c, cd
        else:
            return "N/A", "N/A", "N/A"
    except Exception as e:
        print(f"Error fetching student details: {str(e)}")
        return "N/A", "N/A", "N/A"
    finally:
        cursor.close()
        conn.close()

def recognize_with_cnn(img, clf, face_cascade, nim_mapping):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    coord = []

    for x, y, w, h in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
        face_roi = gray_image[y:y + h, x:x + w]
        face_roi_resized = cv2.resize(face_roi, (450, 450))
        face_roi_resized = face_roi_resized.reshape((1, 450, 450, 1)) 
        face_roi_resized = face_roi_resized / 255.0 

        prediction = clf.predict(face_roi_resized)
        predicted_label = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        print(predicted_label)
        student_id = nim_mapping.get(predicted_label, "Unknown")
        if isinstance(student_id, int):
            student_id = str(student_id)
        print(confidence)
        if confidence > 90:
            sn, c, cd = fetch_student_details_from_database(student_id)

            cv2.putText(img, f"Student ID: {student_id}", (x, y - 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Name: {sn}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Course: {c}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Class: {cd}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

            cv2.putText(img, "Press Enter to Take Attendance", (30, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            cv2.putText(img, "Hold Esc to Close", (1030, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            key = cv2.waitKey(1)
            if key == 13:
                MarkAttendance(student_id, sn, c, cd)
                cv2.putText(img, "Attendance Successful", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                notification.notify(
                    title="Attendance Marked",
                    message="Attendance has been marked successfully.",
                    timeout=0.5
                )
                time.sleep(1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(img, "Unknown Face, please fill in your data through the librarian", (x, y - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, "Hold Esc to Close", (1030, 680), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

        coord = [x, y, w, y]

    return coord



def Face_Recognition():
    id_to_nim = load_nim_to_id_mapping()
    cnn_model = load_model("Model/CNN_Model.h5")

    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("./Haarcascade/haarcascade_frontalface_default.xml")

    while True:
        ret, img = video_capture.read()
        coord = recognize_with_cnn(img, cnn_model, face_cascade, id_to_nim)
        cv2.imshow("Let's Take Attendance", img)

        key = cv2.waitKey(1)
        if key == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Face_Recognition()
