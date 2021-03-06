# Hello, thanks for checking out my Horse Fatigue checker. I've never coded anything in my life and know hardly any
# code at all.This is the first thing i've ever written in python. I'm sure it could be cleaner or simpler, but hey, it works!
# If you have any questions, comments, or suggestions, feel free to contact me on twitter @Gags30poker
# Enjoy!


import tkinter as tk
from tkinter import *
from tkinter import messagebox
import http.client
import re
import datetime
import csv
import pandas as pd


headers_myhorses = ['Horse Name', 'Horse ID']
headers_api = ['API Key', 'none']


try:
    reader = pd.read_csv('api_key.txt')
    global api_key
    api_key = reader.iloc[0, 0]
except:
    with open('api_key.txt', 'a', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=headers_api)
        if f_output.tell() == 0:
            csv_output.writeheader()




# i don't know exactly how this part works, but it took me 3 hours to get this part to work, so fuck it, it's staying
# when program opens it checks to see if my_horses.txt exists, if it does, it doesn't do anything, if it doesn't, it
# creates it and writes headers
with open('my_horses.txt', 'a', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=headers_myhorses)
    f_output.seek(0, 2)

    if f_output.tell() == 0:
        csv_output.writeheader()

##Blank Variables:

horse_name_0 = ""
horse_name_1 = ""
horse_name_2 = ""
horse_name_3 = ""
horse_name_4 = ""
horse_name_5 = ""
horse_name_6 = ""
horse_name_7 = ""
horse_name_8 = ""
horse_name_9 = ""

horse_id_0 = ""
horse_id_1 = ""
horse_id_2 = ""
horse_id_3 = ""
horse_id_4 = ""
horse_id_5 = ""
horse_id_6 = ""
horse_id_7 = ""
horse_id_8 = ""
horse_id_9 = ""

horse_fatigue_0 = ""
horse_fatigue_1 = ""
horse_fatigue_2 = ""
horse_fatigue_3 = ""
horse_fatigue_4 = ""
horse_fatigue_5 = ""
horse_fatigue_6 = ""
horse_fatigue_7 = ""
horse_fatigue_8 = ""
horse_fatigue_9 = ""



### Functions: ###


#Horse Fatigue API Pull:

def fatigue_request(horse_id_input):
    conn = http.client.HTTPSConnection("api.zed.run")
    payload = ""
    headers = { 'Authorization': "Bearer " + api_key }
    conn.request("GET", "/api/v1/horses/fatigue/" + horse_id_input, payload, headers)
    res = conn.getresponse()
    data = res.read()
    fatigue_raw_output = (data.decode("utf-8"))

    # Not entirely sure how this works, I found a script to extract numbers from a string, found here:
    # https://www.geeksforgeeks.org/python-extract-numbers-from-string/
    # ??\_(???)_/??


    temp = re.findall(r'\d+', fatigue_raw_output)

    fatigue_output = list(map(int, temp))

    global final_fatigue_output
    final_fatigue_output = translate(str(fatigue_output))
    return




def translate(phrase): # Remove the brackets from the output
    translation = ""
    for letter in phrase:
        if letter in "[]":
            translation = translation + ""
        else:
            translation = translation + letter
    return translation

def update_time():
    label_updated_time['text']="Last Updated at: "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_horse_to_txt(): #function to add horses to .txt file
    try:
        entered_horse_id = id_entry.get() #pulls horse id from entry field
        horse_db = pd.read_csv('horse_db.csv') #loads horse_db.csv into pandas
        horse_name_output = horse_db['name'][int(entered_horse_id)] # open the horse_db.csv and look for horse with panda
        tup1 = (horse_name_output, entered_horse_id) # put name and id into tuple
        f = open("my_horses.txt", "a", newline="") #open the my_horses.txt and write
        writer = csv.writer(f)
        writer.writerow(tup1)
        f.close()
        id_entry.delete(0, END) #clears the entry field
        check_fatigue()
    except ValueError:
        messagebox.showerror(title="Invalid Entry!", message="Invalid Entry. Please only enter a horse ID#")
    except KeyError:
        messagebox.showerror(title="Horse Not Found!", message="The horse ID# you entered was not found. Please check "
                                                               "the ID# and try again.\n \nIf the ID is correct "
                                                               "then you likely need to update your horse_db.csv file. "
                                                               "\n \nFollow the instructions in 'Help and "
                                                               "Information' for further assistance.")



def check_fatigue():
    #OKAY....first we load the my_horses.txt, then we pull id numbers off it and
    # assign them to horse_id_ variables
    try:
        reader = pd.read_csv('my_horses.txt')
        try:
            global horse_id_0
            global horse_name_0
            horse_id_0 = reader.iloc[0, 1]
            horse_name_0 = reader.iloc[0, 0]
        except IndexError:
            tk.messagebox.showerror(title='No Horses Found!', message='Your saved list of horses is empty. Please enter them by ID# and then you may check their fatigue.')
            return
        try:
            global horse_id_1
            global horse_name_1
            horse_id_1 = reader.iloc[1, 1]
            horse_name_1 = reader.iloc[1, 0]
        except IndexError:
            horse_id_1 = ""
        try:
            global horse_id_2
            global horse_name_2
            horse_id_2 = reader.iloc[2, 1]
            horse_name_2 = reader.iloc[2, 0]
        except IndexError:
            horse_id_2 = ""
        try:
            global horse_id_3
            global horse_name_3
            horse_id_3 = reader.iloc[3, 1]
            horse_name_3 = reader.iloc[3, 0]
        except IndexError:
            horse_id_3 = ""
        try:
            global horse_id_4
            global horse_name_4
            horse_id_4 = reader.iloc[4, 1]
            horse_name_4 = reader.iloc[4, 0]
        except IndexError:
            horse_id_4 = ""
        try:
            global horse_id_5
            global horse_name_5
            horse_id_5 = reader.iloc[5, 1]
            horse_name_5 = reader.iloc[5, 0]
        except IndexError:
            horse_id_5 = ""
        try:
            global horse_id_6
            global horse_name_6
            horse_id_6 = reader.iloc[6, 1]
            horse_name_6 = reader.iloc[6, 0]
        except IndexError:
            horse_id_6 = ""
        try:
            global horse_id_7
            global horse_name_7
            horse_id_7 = reader.iloc[7, 1]
            horse_name_7 = reader.iloc[7, 0]
        except IndexError:
            horse_id_7 = ""
        try:
            global horse_id_8
            global horse_name_8
            horse_id_8 = reader.iloc[8, 1]
            horse_name_8 = reader.iloc[8, 0]
        except IndexError:
            horse_id_8 = ""
        try:
            global horse_id_9
            global horse_name_9
            horse_id_9 = reader.iloc[9, 1]
            horse_name_9 = reader.iloc[9, 0]
        except IndexError:
            horse_id_9 = ""


        fatigue_request(str(horse_id_0)) #fatigue request to zed api to get current fatigue
        horse_fatigue_0 = final_fatigue_output

        fatigue_request(str(horse_id_1))
        horse_fatigue_1 = final_fatigue_output

        fatigue_request(str(horse_id_2))
        horse_fatigue_2 = final_fatigue_output

        fatigue_request(str(horse_id_3))
        horse_fatigue_3 = final_fatigue_output

        fatigue_request(str(horse_id_4))
        horse_fatigue_4 = final_fatigue_output

        fatigue_request(str(horse_id_5))
        horse_fatigue_5 = final_fatigue_output

        fatigue_request(str(horse_id_6))
        horse_fatigue_6 = final_fatigue_output

        fatigue_request(str(horse_id_7))
        horse_fatigue_7 = final_fatigue_output

        fatigue_request(str(horse_id_8))
        horse_fatigue_8 = final_fatigue_output

        fatigue_request(str(horse_id_9))
        horse_fatigue_9 = final_fatigue_output



        # Update all the labels with most recent data:
        label_horse_name_0['text'] = horse_name_0
        label_horse_id_0['text'] = horse_id_0
        label_horse_fatigue_0['text'] = horse_fatigue_0

        label_horse_name_1['text'] = horse_name_1
        label_horse_id_1['text'] = horse_id_1
        label_horse_fatigue_1['text'] = horse_fatigue_1

        label_horse_name_2['text'] = horse_name_2
        label_horse_id_2['text'] = horse_id_2
        label_horse_fatigue_2['text'] = horse_fatigue_2

        label_horse_name_3['text'] = horse_name_3
        label_horse_id_3['text'] = horse_id_3
        label_horse_fatigue_3['text'] = horse_fatigue_3

        label_horse_name_4['text'] = horse_name_4
        label_horse_id_4['text'] = horse_id_4
        label_horse_fatigue_4['text'] = horse_fatigue_4

        label_horse_name_5['text'] = horse_name_5
        label_horse_id_5['text'] = horse_id_5
        label_horse_fatigue_5['text'] = horse_fatigue_5

        label_horse_name_6['text'] = horse_name_6
        label_horse_id_6['text'] = horse_id_6
        label_horse_fatigue_6['text'] = horse_fatigue_6

        label_horse_name_7['text'] = horse_name_7
        label_horse_id_7['text'] = horse_id_7
        label_horse_fatigue_7['text'] = horse_fatigue_7

        label_horse_name_8['text'] = horse_name_8
        label_horse_id_8['text'] = horse_id_8
        label_horse_fatigue_8['text'] = horse_fatigue_8

        label_horse_name_9['text'] = horse_name_9
        label_horse_id_9['text'] = horse_id_9
        label_horse_fatigue_9['text'] = horse_fatigue_9

        update_time() #finally, update time
    except NameError:
        messagebox.showerror(title="No API Key Found!", message="API Key not found, please add API key!")

def add_api_key():
    entered_api_key = id_entry.get()
    f = open('api_key.txt', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow([entered_api_key])
    f.close()
    global api_key
    api_key = entered_api_key
    id_entry.delete(0, END)  # clears the entry field

def clear_api_key():
    MsgBox = tk.messagebox.askquestion('Clear API Key?', 'You are about to clear the saved API key. You may not check fatigue '
                                                         'without an API key. Are you sure you want to clear the API '
                                                         'key?')
    if MsgBox == 'yes':
        with open('api_key.txt', 'r+') as in_file:
            in_file.seek(1)
            in_file.truncate(13)
            api_key = ""
    else:
        return


def information_message():
    tk.messagebox.showinfo(title="Help and Information", message="How to Use:\n1. Enter your API key into the entry box and "
                                                                 "click 'Add API Key'\n***You MUST enter the API key "
                                                                 "you retrieve from the command console. How to do this "
                                                                 "can be found here: https://docs.zed.run/getting-started/api-keys\n2. Enter a horse by it's ID# and "
                                                                 "click 'Add Horse'\n3. The horse's name and fatigue will "
                                                                 "automatically be shown\n4. You may only enter horses "
                                                                 "one at a time, but you may save up to 10 horses."
                                                                 "\n5. Your list of horses will automatically be saved "
                                                                 "and recalled the next time you open the program.\n6. "
                                                                 "To clear your saved list of horses simply click 'Clear"
                                                                 " Saved Horses'\n7. If your API Key expires, or you need"
                                                                 " to change your key for any reason, click the 'Clear "
                                                                 "API Key' button and re-enter your API key\n8. ** The "
                                                                 "db of horse names does not update automatically **. If "
                                                                 "you try to enter a horse and it is not found in the "
                                                                 "list you likely need to update the horse_db file. Go "
                                                                 "to https://zed-odds.netlify.app/ and download the "
                                                                 "latest horse_db.zip. Inside will be a .csv file. Extract "
                                                                 "it and place it into the install directory of this "
                                                                 "program and overwrite the existing horse_db file.\n\n"
                                                                 "The program works by connecting to the Zed.run API. "
                                                                 "You must be connected to the internet for this program"
                                                                 " to work.\n\nPlease be patient when checking fatigue. "
                                                                 "If you have many horses saved it may take several seconds"
                                                                 " for all fatigue stats to load.\n\n\n\n"
                                                                 "Created by Gags30\n\nFor questions, comments, or suggestions "
                                                                 "reach out @Gags30poker on twitter\n\n\nEnjoy, and good "
                                                                 "luck on the track!")

def clear_horses():
    MsgBox = tk.messagebox.askquestion('Clear all horses?', 'This will clear the entire saved list of horses. Are you sure you want to clear all horses?')
    if MsgBox == 'yes':
        with open('my_horses.txt', 'r+') as in_file:
            in_file.seek(0)
            in_file.truncate(20)

            global horse_name_0
            global horse_name_1
            global horse_name_2
            global horse_name_3
            global horse_name_4
            global horse_name_5
            global horse_name_6
            global horse_name_7
            global horse_name_8
            global horse_name_9

            global horse_id_0
            global horse_id_1
            global horse_id_2
            global horse_id_3
            global horse_id_4
            global horse_id_5
            global horse_id_6
            global horse_id_7
            global horse_id_8
            global horse_id_9

            global horse_fatigue_0
            global horse_fatigue_1
            global horse_fatigue_2
            global horse_fatigue_3
            global horse_fatigue_4
            global horse_fatigue_5
            global horse_fatigue_6
            global horse_fatigue_7
            global horse_fatigue_8
            global horse_fatigue_9


            horse_name_0 = ""
            horse_name_1 = ""
            horse_name_2 = ""
            horse_name_3 = ""
            horse_name_4 = ""
            horse_name_5 = ""
            horse_name_6 = ""
            horse_name_7 = ""
            horse_name_8 = ""
            horse_name_9 = ""

            horse_id_0 = ""
            horse_id_1 = ""
            horse_id_2 = ""
            horse_id_3 = ""
            horse_id_4 = ""
            horse_id_5 = ""
            horse_id_6 = ""
            horse_id_7 = ""
            horse_id_8 = ""
            horse_id_9 = ""

            horse_fatigue_0 = ""
            horse_fatigue_1 = ""
            horse_fatigue_2 = ""
            horse_fatigue_3 = ""
            horse_fatigue_4 = ""
            horse_fatigue_5 = ""
            horse_fatigue_6 = ""
            horse_fatigue_7 = ""
            horse_fatigue_8 = ""
            horse_fatigue_9 = ""

            label_horse_name_0['text'] = horse_name_0
            label_horse_id_0['text'] = horse_id_0
            label_horse_fatigue_0['text'] = horse_fatigue_0

            label_horse_name_1['text'] = horse_name_1
            label_horse_id_1['text'] = horse_id_1
            label_horse_fatigue_1['text'] = horse_fatigue_1

            label_horse_name_2['text'] = horse_name_2
            label_horse_id_2['text'] = horse_id_2
            label_horse_fatigue_2['text'] = horse_fatigue_2

            label_horse_name_3['text'] = horse_name_3
            label_horse_id_3['text'] = horse_id_3
            label_horse_fatigue_3['text'] = horse_fatigue_3

            label_horse_name_4['text'] = horse_name_4
            label_horse_id_4['text'] = horse_id_4
            label_horse_fatigue_4['text'] = horse_fatigue_4

            label_horse_name_5['text'] = horse_name_5
            label_horse_id_5['text'] = horse_id_5
            label_horse_fatigue_5['text'] = horse_fatigue_5

            label_horse_name_6['text'] = horse_name_6
            label_horse_id_6['text'] = horse_id_6
            label_horse_fatigue_6['text'] = horse_fatigue_6

            label_horse_name_7['text'] = horse_name_7
            label_horse_id_7['text'] = horse_id_7
            label_horse_fatigue_7['text'] = horse_fatigue_7

            label_horse_name_8['text'] = horse_name_8
            label_horse_id_8['text'] = horse_id_8
            label_horse_fatigue_8['text'] = horse_fatigue_8

            label_horse_name_9['text'] = horse_name_9
            label_horse_id_9['text'] = horse_id_9
            label_horse_fatigue_9['text'] = horse_fatigue_9

    else:
        return



#### GUI #####



height = 400
width = 430


root = tk.Tk()
root.resizable(False, False)
root.title('Horse Fatigue Tracker')
root.iconbitmap('horse_icon.ico')


canvas = tk.Canvas(root, height=height, width=width, bg='black')
canvas.pack()


frame = tk.Frame(root, bg='#6e6750', bd=5, width=width, height='200')
frame.place(relx=0, rely=0, relwidth=1, relheight=0.26)

output_frame = tk.Frame(root, bg='#e0d3a6', bd=5)
output_frame.place(relx=0, rely=0.22, relwidth=1, relheight=1)

### Buttons:

id_entry = tk.Entry(frame, text="Enter Horse ID Here", font=40, width=25)
id_entry.grid(row=0, column=0, columnspan=2)

add_button = tk.Button(frame, text="Add Horse", command=add_horse_to_txt, width=9)
add_button.grid(row=0, column=2, padx=3, rowspan=2, sticky=tk.N+tk.S)


check_fatigue_button = tk.Button(frame, text="Check Fatigue", command=check_fatigue, width=15, height=4)
check_fatigue_button.grid(row=0, column=3, rowspan=3, stick=tk.N+tk.S)

add_api_key_button = tk.Button(frame, text="Add API Key", command=add_api_key, width=9)
add_api_key_button.grid(row=2, column=2)

clear_api_key_button = tk.Button(frame, text="Clear API Key", command=clear_api_key, width=15)
clear_api_key_button.grid(row=2, column=1)

information_button = tk.Button(frame, text="Information and Help", command=information_message)
information_button.grid(row=1, column=0, pady=2, columnspan=2, stick=tk.W+tk.E)

clear_horses_button = tk.Button(frame, text="Clear Saved Horses", command=clear_horses, width=15)
clear_horses_button.grid(row=2, column=0)

###Horse Output labels:

label_name_title = tk.Label(output_frame, text="Horse Name:", font='Arial 15 bold', background='#e0d3a6')
label_name_title.grid(row=0, column=0)

label_name_title_id = tk.Label(output_frame, text="Horse ID#:", font='Arial 15 bold', background='#e0d3a6')
label_name_title_id.grid(row=0, column=1)

label_fatigue_title_id = tk.Label(output_frame, text="Fatigue:", font='Arial 15 bold', background='#e0d3a6')
label_fatigue_title_id.grid(row=0, column=2)

label_horse_name_0 = tk.Label(output_frame, text=horse_name_0, font='bold', bg='#e0d3a6')
label_horse_name_0.grid(row=1, column=0, sticky=W)
label_horse_name_1 = tk.Label(output_frame, text=horse_name_1, font='bold', bg='#e0d3a6')
label_horse_name_1.grid(row=2, column=0, sticky=W)
label_horse_name_2 = tk.Label(output_frame, text=horse_name_2, font='bold', bg='#e0d3a6')
label_horse_name_2.grid(row=3, column=0, sticky=W)
label_horse_name_3 = tk.Label(output_frame, text=horse_name_3, font='bold', bg='#e0d3a6')
label_horse_name_3.grid(row=4, column=0, sticky=W)
label_horse_name_4 = tk.Label(output_frame, text=horse_name_4, font='bold', bg='#e0d3a6')
label_horse_name_4.grid(row=5, column=0, sticky=W)
label_horse_name_5 = tk.Label(output_frame, text=horse_name_5, font='bold', bg='#e0d3a6')
label_horse_name_5.grid(row=6, column=0, sticky=W)
label_horse_name_6 = tk.Label(output_frame, text=horse_name_6, font='bold', bg='#e0d3a6')
label_horse_name_6.grid(row=7, column=0, sticky=W)
label_horse_name_7 = tk.Label(output_frame, text=horse_name_7, font='bold', bg='#e0d3a6')
label_horse_name_7.grid(row=8, column=0, sticky=W)
label_horse_name_8 = tk.Label(output_frame, text=horse_name_8, font='bold', bg='#e0d3a6')
label_horse_name_8.grid(row=9, column=0, sticky=W)
label_horse_name_9 = tk.Label(output_frame, text=horse_name_9, font='bold', bg='#e0d3a6')
label_horse_name_9.grid(row=10, column=0, sticky=W)

label_horse_id_0 = tk.Label(output_frame, text=horse_id_0, font='bold', bg='#e0d3a6')
label_horse_id_0.grid(row=1, column=1)
label_horse_id_1 = tk.Label(output_frame, text=horse_id_1, font='bold', bg='#e0d3a6')
label_horse_id_1.grid(row=2, column=1)
label_horse_id_2 = tk.Label(output_frame, text=horse_id_2, font='bold', bg='#e0d3a6')
label_horse_id_2.grid(row=3, column=1)
label_horse_id_3 = tk.Label(output_frame, text=horse_id_3, font='bold', bg='#e0d3a6')
label_horse_id_3.grid(row=4, column=1)
label_horse_id_4 = tk.Label(output_frame, text=horse_id_4, font='bold', bg='#e0d3a6')
label_horse_id_4.grid(row=5, column=1)
label_horse_id_5 = tk.Label(output_frame, text=horse_id_5, font='bold', bg='#e0d3a6')
label_horse_id_5.grid(row=6, column=1)
label_horse_id_6 = tk.Label(output_frame, text=horse_id_6, font='bold', bg='#e0d3a6')
label_horse_id_6.grid(row=7, column=1)
label_horse_id_7 = tk.Label(output_frame, text=horse_id_7, font='bold', bg='#e0d3a6')
label_horse_id_7.grid(row=8, column=1)
label_horse_id_8 = tk.Label(output_frame, text=horse_id_8, font='bold', bg='#e0d3a6')
label_horse_id_8.grid(row=9, column=1)
label_horse_id_9 = tk.Label(output_frame, text=horse_id_9, font='bold', bg='#e0d3a6')
label_horse_id_9.grid(row=10, column=1)

label_horse_fatigue_0 = tk.Label(output_frame, text=horse_fatigue_0, font='bold', bg='#e0d3a6')
label_horse_fatigue_0.grid(row=1, column=2)
label_horse_fatigue_1 = tk.Label(output_frame, text=horse_fatigue_1, font='bold', bg='#e0d3a6')
label_horse_fatigue_1.grid(row=2, column=2)
label_horse_fatigue_2 = tk.Label(output_frame, text=horse_fatigue_2, font='bold', bg='#e0d3a6')
label_horse_fatigue_2.grid(row=3, column=2)
label_horse_fatigue_3 = tk.Label(output_frame, text=horse_fatigue_3, font='bold', bg='#e0d3a6')
label_horse_fatigue_3.grid(row=4, column=2)
label_horse_fatigue_4 = tk.Label(output_frame, text=horse_fatigue_4, font='bold', bg='#e0d3a6')
label_horse_fatigue_4.grid(row=5, column=2)
label_horse_fatigue_5 = tk.Label(output_frame, text=horse_fatigue_5, font='bold', bg='#e0d3a6')
label_horse_fatigue_5.grid(row=6, column=2)
label_horse_fatigue_6 = tk.Label(output_frame, text=horse_fatigue_6, font='bold', bg='#e0d3a6')
label_horse_fatigue_6.grid(row=7, column=2)
label_horse_fatigue_7 = tk.Label(output_frame, text=horse_fatigue_7, font='bold', bg='#e0d3a6')
label_horse_fatigue_7.grid(row=8, column=2)
label_horse_fatigue_8 = tk.Label(output_frame, text=horse_fatigue_8, font='bold', bg='#e0d3a6')
label_horse_fatigue_8.grid(row=9, column=2)
label_horse_fatigue_9 = tk.Label(output_frame, text=horse_fatigue_9, font='bold', bg='#e0d3a6')
label_horse_fatigue_9.grid(row=10, column=2)

label_updated_time = tk.Label(output_frame, text="Last Updated at: "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
label_updated_time.grid(row=11, column=1, columnspan=3)



root.mainloop()



