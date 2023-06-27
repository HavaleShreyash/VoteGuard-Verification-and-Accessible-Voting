import face_recog as frg

def face_b_flag(user_id):
    #Fingerprint code 
    bool_flg = frg.detect_face(user_id)
    print(bool_flg)
    return(bool_flg)

def finger_b_flag():
    #Facecode goes here
    print("Finger")
    return(True)

def bio_flag(uid):

    argument = input("\nChoose type of biometric verification\n\nFingerprint\nFace\n\n")
    match argument:
        case "fingerprint" | "Fingerprint":
            return finger_b_flag()
        case "face" | "Face":
            return face_b_flag(uid)
        case default:
            return "Error: Data not found"

