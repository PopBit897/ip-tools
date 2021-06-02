while True:
    import socket
    Search=input("nome del sito:  ")
    ip= socket.gethostbyname(Search)
    print(ip)
   
 

    