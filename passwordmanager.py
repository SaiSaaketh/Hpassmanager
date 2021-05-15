import string
import random
import os

os.listdir()
print("Please Enter the Username:")
user = input()
print("Please Enter Your Email Address which You Have Given For the Account:")
email = input()
print("For which platform do you wanna sign up")
platform = input()
print("Please Enter Date when you Created the Account:")
date = input()
print("Please Enter The Recovery Number:")
number = int(input())
print("Generating your Secure Password")
alplower = string.ascii_lowercase
alphigher = string.ascii_uppercase
digi = string.digits
punc = string.punctuation
passwordtmp = alplower+alphigher+digi+punc
length = 8
password1 = random.sample(passwordtmp,length)
password = "".join(password1)
print(password)
print("Press enter to exit")
exitpro = input()
file = open("./passwordDB.txt","a")
sentences= [f'''platform:{platform}
                Username:{user}
                Email:{email}
                Password:{password}
                Date of Creation:{date}
                Mobile Number:{number}\n''']
file.write("\n".join(sentences))