#cod tools ip red anonymus
#tools is made italy,tools is free
# cod ita and eng
# menu
print("choose between Italian or English")
print("write ita for the Italian language or also en for English (write lowercase)")
login = input("choose Italian or English: ")
   # login ita lengueg :)
if login =='ita':
    text = """  ip pc = 1
    nome locale del pc = 2
    ip  e nomelocale del pc = 3
    scanerip = 4
    info = 5
    sitoweb ip = 6
    indirizzio pc  (hex) = 7
    \t"""
    
    print("***************************************************************") 
    print("""
             _              _  _ __        _              _     
     _ _  __| | __ _       (_)| '_ \      | |_  ___  ___ | | ___
    | '_|/ _` |/ _` |      | || .__/      |  _|/ _ \/ _ \| |(_-/
    |_|  \__/_|\__/_|      |_||_|          \__|\___/\___/|_|/__/
             """)
    print("****************************************************************\n")
    print(text)

    while True:
       import webbrowser
       import socket
       import uuid
       Search=input("cerca ")
       link="https://github.com/RedAnonymusITA/ip_tools_GUI"
       hostname=socket.gethostname()
       ip_addres= socket.gethostbyname(hostname)
            #scaner
       scaner='not enabled, wait for the next update can be added :('



       def web_ip():
            print("scrivi il nome del sito web come l'esempio (www.nome sito web.com o nomelocale")
            
            
            while True:
            
                import socket
                Search=input("nome del sito:  ")
                ip= socket.gethostbyname(Search)
                print("l'ip e questo "+ip)
                
 

    

       if Search =='6':
          web_ip()
    
       if Search =="7":
           print(hex(uuid.getnode()))
       
     
            #code if and elif 
       if Search =="1":
            print("ip pc e : "+ip_addres)

       if Search == "2":
             print("nomelocale pc e: "+hostname)

       elif Search =="3":
             print("ip pc e  : "+ip_addres+" e nome locale : "+hostname)

       if Search =="4":
             print(scaner)   
               

       if Search=="5":

           
           print("""
           _     _  _                _       
          | |__ | || |       _ _  __| | __ _ 
          |  _ \ \_. |      | '_|/ _` |/ _` |
          |____/ |__/       |_|  \__/_|\__/_|
          
          piu app: ip_tools/GUI ALPHA V0.1.1
          scrivi il numero 8 per aprire il mio repository o premi invia per continuare
          """)
           
           Search1 =input("scrivi ")
           if Search1 == '8': 
                print("sto aprendo il tuo browser")
                webbrowser.open(link)
           
        


      
    # login en login lengueg 
if login =='en':
    
    text = """  pc ip = 1
    pc hostname = 2
    pc ip and hostname = 3
    scanerip = 4
    info = 5
    website ip = 6
    mac addres pc (hex) = 7
    \t"""

    print("***************************************************************")
    print("""
             _              _  _ __        _              _     
     _ _  __| | __ _       (_)| '_ \      | |_  ___  ___ | | ___
    | '_|/ _` |/ _` |      | || .__/      |  _|/ _ \/ _ \| |(_-/
    |_|  \__/_|\__/_|      |_||_|          \__|\___/\___/|_|/__/
             """)
    print("****************************************************************\n")
    print(text)

    while True:
       import webbrowser
       import socket
       import uuid
       Search=input("Search ")
       link="https://github.com/RedAnonymusITA/ip_tools_GUI"
       hostname=socket.gethostname()
       ip_addres= socket.gethostbyname(hostname)
            #scaner
       scaner='not enabled, wait for the next update can be added :('



       def web_ip():
            print("write the name of the website example (www.site name. com or hosname)")
            while True:
            
                import socket
                Search=input("site name:  ")
                ip= socket.gethostbyname(Search)
                print("here is the ip"+ip)
                
 

    

       if Search =='6':
          web_ip()
    
       if Search =="7":
           print(hex(uuid.getnode()))
       
     
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
           _     _  _                _       
          | |__ | || |       _ _  __| | __ _ 
          |  _ \ \_. |      | '_|/ _` |/ _` |
          |____/ |__/       |_|  \__/_|\__/_|
          
          more app : ip_tools/GUI ALPHA V0.1.1
          write the number 8 if you want to open my repository or press submit to continue""")
           
           Search1 =input("write ")
           if Search1 == '8': 
                print("open you browser")
                webbrowser.open(link)
          
     
        


      

    


      
