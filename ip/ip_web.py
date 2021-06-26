print("write the name of the website with the second domain example (site name. com)")
while True:
    import socket
    Search=input("site name:  ")
    ip= socket.gethostbyname(Search)
    print("here is the ip "+ip)
   
 

    