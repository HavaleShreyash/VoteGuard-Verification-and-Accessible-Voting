import pandas as pd
import biometric as bio

vts = pd.read_csv("votes.csv")
usr = pd.read_csv("users.csv")

def voter_list_update(login_id):
    # find the row index that matches the user ID
    row_index = usr.index[usr['user_id'] == login_id].tolist()[0]
    # update the flag value in the dataframe
    usr.at[row_index, 'voting status'] = 1
    # write the updated dataframe back to the CSV file
    usr.to_csv('users.csv', index=False)

def cand_list_update(cand_id):
    # find the row index that matches the user ID
    row_index = vts.index[vts['Candidate'] == cand_id].tolist()[0]
    # update the flag value in the dataframe
    vts.at[row_index, 'Votes'] += 1
    # write the updated dataframe back to the CSV file
    vts.to_csv('votes.csv', index=False)
    print("\nVoted Successfully")

def vote_candidate():
    lst = vts[['Candidate','Party']]
    print("List of candidates and Parties are given below")
    print(lst)
    while True:
        candidate = input("Please input the candidate you have selected ")
        verify = input("For verification rewrite the candidate name ")
        if candidate == verify:
            cand_lst = lst['Candidate'].str.contains(candidate, case=False)
            cand_row = lst[cand_lst]
            print("Chosen candidate\n\n",cand_row)
            cand_flg = bio.bio_flag
            while True:
                if cand_flg:
                    cand_list_update(candidate)
                    return(True)
                    break
                else: 
                    print("Incorrect Biometrics!")
                    i = 0
                    i += 1
                    if i == 5:
                        return(False)
                break
        else:
            print("Error: Values don't match\n")


def vote(login_id): 
    login_id = login_id
    # Filter for rows where the 'user_id' column contains "login_id"
    voter_rows = usr.loc[usr['user_id'].str.contains(login_id, case=False)]

    # Get the values of the 'voting status' column for the 'login_id' rows
    voter_flag = voter_rows.loc[:, 'voting status']

    voter_flag = voter_flag.iloc[0]


    while True:
        if login_id in usr['user_id'].values:
            if voter_flag == 0:
                success_flg = vote_candidate()
                if success_flg:
                    voter_list_update(login_id)
                    break
            elif voter_flag == 1:
                print("You have already voted")
                break
            else:
                print("Error: Wrong Voter Flag ID")
        else:
            print("Sorry you are not a listed voter")
            break


# vote("u4567");