import sys
import face_recognition as fr
import pickle
import cv2
import os

def locking():
        video_capture = cv2.VideoCapture(0)
        face_is_match = False
        face_encodings = []
        known_face_encodings = pickle.load(open('encode.pickle','rb'))
        
        while True:
                ret, frame = video_capture.read()
                face_locations = fr.face_locations(frame, model="hog")
                face_encodings = fr.face_encodings(frame, face_locations)
                
                face_names = []
                name = "Unknown"
                for face_encoding in face_encodings:
                        matches = fr.compare_faces(known_face_encodings, face_encoding, 0.4)
                
                        #find first match
                        if True in matches:
                                first_known_face = matches.index(True)
                                face_is_match = True
                                print("Welcome")
                                print("Intializing JARVIS....")
                                video_capture.release()
                                os.system('python jarvis.py')
                                sys.exit(0)

                        else:
                                print("Access Denied")
                                quit()