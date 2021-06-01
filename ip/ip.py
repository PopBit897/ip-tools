#codice tools ip red anonymus
#tools is made italy,tools is free

import socket
import uuid
print("***************************************************************")
print("""
         _              _  _ __        _              _     
 _ _  __| | __ _       (_)| '_ \      | |_  ___  ___ | | ___
| '_|/ _` |/ _` |      | || .__/      |  _|/ _ \/ _ \| |(_-/
|_|  \__/_|\__/_|      |_||_|          \__|\___/\___/|_|/__/


             """)
print("****************************************************************\n")
print("""my ip=1
my hostname=2
my  ip and hostname=3
scanerip=4
info=5
web ip=6
mac addres=7
github link=8\n""")
Search=input("Search ")
link="https://github.com/RedAnonymusITA/ip-tools"
hostname=socket.gethostname()
ip_addres= socket.gethostbyname(hostname)
scaner='not enabled'
ip_web='not enabled'
if Search=="2":
    print("you host name pc is: "+hostname)
    cerca=input("Search ")
    
if Search=="1":
    print("you ip pc: "+ip_addres)
    cerca=input("Search ")
    
elif Search=="3":
    print(hostname+" = "+ip_addres)
    Search=input("Search ")

if Search=="4":
    print(scaner)
    Search=input("Search ")

if Search=="7":
     print(hex(uuid.getnode()))
     Search=input("Search ")
     
if Search=="5":
     print(""" 
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▀█░██░███░▄▄▀█░▄▀█░▄▄▀
█░▄▄▀█░▀▀░███░▀▀▄█░█░█░▀▀░
█▄▄▄▄█▀▀▀▄███▄█▄▄█▄▄██▄██▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
     Search=input("Search ") 

if Search =='6':
    print(ip_web)
    Search=input("Search ")

if Search =="8":
    print(link)
    Search=input("Search ")

