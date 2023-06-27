import cv2, time
from simple_facerec import SimpleFacerec
from capture_img import take_photos
 
# Encode faces from a folder
# take_photos()
sfr = SimpleFacerec()
sfr.load_encoding_images("C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/images")

# Load Camera
cap = cv2.VideoCapture(0)
def detect_face(user_id):
    timeOut=time.time() + 10
    while time.time()<timeOut:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        if(face_names.count(user_id)!=0):
            return True
        int_user_id=str(user_id)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            # print(type(user_id))
            # print(type(name))
            # userName=str(name)
            # print(type(int_user_id))
            # print(type(userName))

            # if(userName==int_user_id):
            #     return True

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return False

if __name__ == "__main__":
    user_id=input("Enter user_id: ")
    d=detect_face(user_id)
    print(d)


