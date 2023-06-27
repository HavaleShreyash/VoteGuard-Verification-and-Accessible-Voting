#Import libraries
import os
import pandas as pd
import ac_creation as ac
import login_func_v02 as lg

#Datasets
usr = pd.read_csv("C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/users.csv")
aadr = pd.read_csv("C:/Users/nakul/OneDrive/Desktop/EPICS/Beta_V01/aadr.csv")

print("Welcome to the E-Voting System!\n")
print("Do you have a pre-existing account?\n")
val = input("Enter 'y' for yes and 'n' for no: ")

if val == 'y' or val == 'Y':
    #Login and voting
    lg.login()
else:     
    #Account creaetion
    ac.create_account()

    #Login and voting
    lg.login()
