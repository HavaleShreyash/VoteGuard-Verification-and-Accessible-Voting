import os
#import biometric as bio
import pwinput
import pandas as pd

def create_account():
    # Create an empty dataframe with columns, 'username' and 'password'
    user_name = pd.DataFrame(columns=['user_id', 'password', 'voting status'])
    # Ask the user for their username and password
    aadr = input("Enter your Aadhar ID: ")
    aadr="u"+aadr
    password1 = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    # password = input("Enter your password: ")
    # Append the username and password to the dataframe as a new row
    # Append the username and password to the dataframe as a new row
    new_row = pd.DataFrame({'user_id': aadr, 'password': password1, 'voting status': 0}, index=[0])
    user_name = pd.concat([new_row], ignore_index=False)

    #user_name = user_name.append({'aadr': aadr, 'password': password1, 'voting status': 0}, ignore_index=True)
    
    # Write the dataframe to a CSV file
    user_name.to_csv('C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/users.csv', mode='a',header=False, index=False)
    # user_name.to_csv('C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/users.csv', mode='a', header=not os.path.exists('D:/EPICS/Beta_V01/users.csv'),header=False, index=False)
    
    #Biometric ka code
    information(aadr,password)
    print("\n\nAccount Created!")
    

def information(adrnum,password):

    aadr_info = pd.read_csv("C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/aadr.csv")
    # Get the index of the row where 'aadhar' column matches the given 'adrnum'
    if adrnum in aadr_info['aadhar'].values:

        index = aadr_info.loc[aadr_info['aadhar'] == adrnum]
        
        # Create a new dataframe with the user information
        user_information = pd.DataFrame({
            'Aadhar': [index['aadhar'].values[0]],
            'Name': [index['name'].values[0]],
            'Age': [index['age'].values[0]],
            'Gender': [index['gender'].values[0]]
        }).set_index('Aadhar')


        print(user_information)
        # user_information.to_csv('user.csv', mode='a', header=False, index=False)
    else:
        print("Aadhar number not found. Please try again.", adrnum)
        create_account()



if __name__ == "__main__":
    create_account()




