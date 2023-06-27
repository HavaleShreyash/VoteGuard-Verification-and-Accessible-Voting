
#Imporing Libraries
import pandas as pd
import pwinput
import biometric
import voting_v6



def login():
    #Importing datasets
    usr = pd.read_csv("C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/users.csv")
    #Taking user ID input
    login_id = input("\nEnter your login ID: ")
    login_id="u"+login_id

    #Taking a masked input for password
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    # if login_id in usr['user_id'].values:
    #     print(True)

    # Check if the username and password match any rows in the dataframe
    match = usr[(usr["user_id"] == login_id) & (usr["password"] == password)]
    print(match)
    # If there is a match, we go futher to voting
    if not match.empty:
        biometric_flag = biometric.bio_flag(login_id)
        if biometric_flag:
            print("\n\nLogin successful!\n")
            voting_v6.vote(login_id)
        else:
            print("Invalid Biometric")
    else:
        print("\n\nInvalid username or password. Please try again.\n")
    
if __name__ == "__main__":
    login()



