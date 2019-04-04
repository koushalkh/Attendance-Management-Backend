import csv
import random
import string
import copy
import smtplib
from smtplib import SMTP as smtp
from email.mime.text import MIMEText as text

SENDER_ADDRESS = "rnsit.attendance@gmail.com"
SENDER_PASSWORD = "rnsit123"

li=[]
i=0

#Modify the path in 'input_file' to point to the new users input file
# USN, First Name, Last Name, EmailID
# Generated Username: FirstName.LastName
# Generated Password: <random string of length 10>
input_file = 'inputs.csv' 
with open(input_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        li.append(row)
        i=i+1


def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

out=[]
inside=[]
passlist=[]
for it in li:
    second=it[1].replace(" ","").replace("'","").lower()+'.'+it[2].replace(" ","").replace("'","").lower()
    inside.append(second)
    inside.append(randomString())
    passlist.append(copy.copy(inside))
    inside.append(it[3])
    out.append(copy.copy(inside))
    del inside[:]

for mb in out:

    msg=''' This is your credentials for RNSIT Attendance Management  
    Username: '''+mb[0]+'''
    Password: '''+mb[1]
    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(SENDER_ADDRESS, SENDER_PASSWORD)
    m = text(msg)
    m['Subject'] = 'RNSIT Attendance login credentials'
    m['From'] = SENDER_ADDRESS
    m['To'] = mb[2]
    s.sendmail(SENDER_ADDRESS, mb[2], m.as_string())      
    s.quit()

# Function to return Username and Password   
def get_new_users(plist):
    print(plist)

#get_new_users(passlist)

