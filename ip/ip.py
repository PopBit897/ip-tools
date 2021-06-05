#cod tools ip red anonymus
#tools is made italy,tools is free 

print("***************************************************************")
print("""
             _              _  _ __        _              _     
     _ _  __| | __ _       (_)| '_ \      | |_  ___  ___ | | ___
    | '_|/ _` |/ _` |      | || .__/      |  _|/ _ \/ _ \| |(_-/
    |_|  \__/_|\__/_|      |_||_|          \__|\___/\___/|_|/__/
             """)
print("****************************************************************\n")
print("""
pc ip = 1
pc hostname = 2
pc ip and hostname = 3
scanerip = 4
info = 5
website ip = 6
mac addres pc (hex) = 7
github link = 8\n""")
while True:
    import socket
    import uuid
    Search=input("Search ")
    link="https://github.com/RedAnonymusITA/ip-tools"
    hostname=socket.gethostname()
    ip_addres= socket.gethostbyname(hostname)
            #scaner
    scaner='not enabled, wait for the next update can be added :('
     
            #code if and elif 
    if Search =="1":
       print("pc ip is : "+ip_addres)

    if Search == "2":
       print("pc hostname is: "+hostname)

    elif Search =="3":
       print("pc ip is : "+ip_addres+" and hostname : "+hostname)

    if Search =="4":
       print(scaner)   
               

    if Search=="5":
       print("""
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
     █░▄▄▀█░██░███░▄▄▀█░▄▀█░▄▄▀
     █░▄▄▀█░▀▀░███░▀▀▄█░█░█░▀▀░
     █▄▄▄▄█▀▀▀▄███▄█▄▄█▄▄██▄██▄
     ▀▀▀▀▀         """)
       Search=input("Search: ") 

    if Search =='6':
        import ip_web
    
    if Search =="7":
        print(hex(uuid.getnode()))


    if Search =="8":
        print(link)
        Search=input("Search: ")