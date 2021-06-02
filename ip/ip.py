#codice tools ip red anonymus
#tools is made italy,tools is free if Sewhile True:
while True:
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
    print("""ip del pc=1
hostname del pc=2
ip e hostname del pc=3
scanerip=4
info=5
ip dei siti web=6
mac addres=7
github link=8\n""")
    Search=input("cerca ")
    link="https://github.com/RedAnonymusITA/ip-tools"
    hostname=socket.gethostname()
    ip_addres= socket.gethostbyname(hostname)
            #scaner
    scaner='non abilitato'
     
            #code if and elif 
    if Search=="2":
        print("hostname del pc: "+hostname)
        cerca=input("cerca ")
    
    if Search=="1":
       print("nome host del pc :"+hostname)
       cerca=input("cerca ")
    
    elif Search=="3":
         print(hostname+" = "+ip_addres)
         Search=input("carca ")

    if Search=="4":
       print(scaner)
       Search=input("cerca ")

    if Search=="7":
       print(hex(uuid.getnode()))
       Search=input("cerca ")
     
    if Search=="5":
       print("""
     una volta scelto premere invia e dopo una altra volta per ricaricare .creato:
     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
     █░▄▄▀█░██░███░▄▄▀█░▄▀█░▄▄▀
     █░▄▄▀█░▀▀░███░▀▀▄█░█░█░▀▀░
     █▄▄▄▄█▀▀▀▄███▄█▄▄█▄▄██▄██▄
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
          loso  ci possono stare molti problemi ma faro di tutto per risolvere :)          """)
       Search=input("cerca ") 

    if Search =='6':
        import ip_web
    


    if Search =="8":
        print(link)
        Search=input("cerca ")