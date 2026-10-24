#email automation
#otp authentication
import random
import math
import smtplib#simple mail transfer protocal library

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("lohithr618@gmail.com","zgki mzjm jrok mkkk")
user="lohithr618@gmail.com"
email=input("enter the mail which you want to send otp")
s.sendmail(user,email,msg)
while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("otp is incorrect")
