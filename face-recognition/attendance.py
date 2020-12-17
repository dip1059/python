import cv2
import face_recognition
import numpy
import os


def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode_list.append(face_recognition.face_encodings(img)[0])
    return encode_list


sample_path = "resources/samples"
file_names = os.listdir(sample_path)
names = []
images = []

for file_name in file_names:
    img = cv2.imread(f"{sample_path}/{file_name}")
    images.append(img)
    names.append(os.path.splitext(file_name)[0])

print("Encoding Processing ...")
known_encode_list = find_encodings(images)
print("Encoding Completed.")

capture = cv2.VideoCapture(0)
capture.set(10, 10)
while True:
    success, img = capture.read()
    #img = cv2.resize(img,(0,0),fx=0.25, fy=0.25)
    face_locations_from_current_frame = face_recognition.face_locations(img)
    face_encodings_from_current_frame = face_recognition.face_encodings(img)

    for loc, encoding in zip(face_locations_from_current_frame, face_encodings_from_current_frame):
        matches = face_recognition.compare_faces(known_encode_list, encoding)
        face_distances = face_recognition.face_distance(known_encode_list, encoding)
        match_index = numpy.argmin(face_distances)
        if matches[match_index]:
            y1, x2, y2, x1 = loc
            cv2.rectangle(img,(x1, y1),(x2, y2),(0, 255, 0), 2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0, 255, 0), cv2.FILLED)
            cv2.putText(img, names[int(match_index)], (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255, 255), 2)

    cv2.imshow("out", img)
    if cv2.waitKey(1) == 27: #esc key
        break
