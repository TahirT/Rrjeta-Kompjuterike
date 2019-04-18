from socket import *
import datetime
import sys
from _thread import *
import random
host='localhost'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
try :
    serverSocket.bind(('',serverPort))
except IOError:
print("Lidhja nuk u formua")
    sys.exit()


print ('Serveri u startua ne localhostin:'+str(serverPort))
serverSocket.listen(10)
print('Serveri mund te pranoj kerkese')


#FIBONACCI nuk punon, arsyeja nuk pata mundsi me e analizu dhe permisu

def FIBONACCI(number):
     
     for (x=1;y=1):
               z= x + y
                x = y
                y = z
            z = fibonacci
     return fibonacci


def IPADRESA():
    return gethostbyname(gethostname())

def BASHTINGELLORE(x):
    bashtingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z']
  
    while y=0:
        if(shkronja in bashtingellore ):
              y=y+1
    return y

def EMRIIKOMPJUTERIT(): 
    return gethostname()

def KOHA():
    k=datetime.datetime.now()
    k = k.strftime('%H:%M:%S')
    return k

def LOJA():
    l = random.sample(range(0,49),7)
    
    numrin = str(l)
    return numrin

def KONVERTIMI(metoda, numri):
     if metoda=="KilowattToHorsepower":
        pergigja = numri*1.341 

     elif metoda=="HorsepowerToKilowatt":
        pergjigja = numri/1.341 

     elif metoda=="DegreesToRadians":
        pregjigja = numri*pi/180

     elif metoda=="RadiansToDegrees":
        pergjigja = numri*180/pi 

     elif metoda=="GallonsToLiters":
        pergjigja = numri*3.785 
     
     elif metoda=="LitersToGallons":
        pergjigja = numri/3.785 
     else:

        pergjigja = "Gabim"
     return pergjigja


def clientthread(connectionSocket):
    while True:
        try:
            zgjedhja = connectionSocket.recv(128).decode('utf-8')
            if not zgjedhja:
                break;
        except IOError:
            print('ERROR')
            break

        komanda = str(zgjedhja)

 elif komanda =='IPADRESA':
          connectionSocket.send(str(IPADRESA()).encode('utf-8'))
        if komanda == 'NUMRIIPORTIT':
         connectionSocket.send(str(serverPort).encode('utf-8'))
        elif komanda == 'PRINTO':
     kerkesa = connectionSocket.recv(128)
         connectionSocket.send(kerkesa)
            connectionSocket.send(str(IPADRESA()).encode('utf-8'))
        elif komanda == 'BASHTINGELLORE':
     fjalia = connectionSocket.recv(128).decode('utf-8')
  print('Fjalia e dhene eshte: "'+fjalia+'"')
            connectionSocket.send(str(BASHTINGELLORE(fjalia)).encode('utf-8'))
        elif komanda =='EMRIIKOMPJUTERIT':
   connectionSocket.send(str(EMRIIKOMPJUTERIT()).encode('utf-8'))
            elif komanda =='KOHA':
     connectionSocket.send((KOHA().encode('utf-8'))) 
        elif komanda =='LOJA':
            connectionSocket.send((LOJA().encode('utf-8')))
        elif komanda =='FIBONACCI':
            numri=connectionSocket.recv(128).decode('utf-8')
          print('Numri eshte: '+numri)
            nr=int(numri)
      connectionSocket.send(str(FIBONACCI(nr)).encode('utf-8'))
        elif komanda =='KONVERTIMI':
     metoda = connectionSocket.recv(128).decode('utf-8')
            numri = connectionSocket.recv(128).decode('utf-8')
            nr=int (numri)
      print('Klienti ka zgjedhur te konvertoj' + str(metoda))
         connectionSocket.send(str(KONVERTIMI(metoda, nr)).encode('utf-8'))
    connectionSocket.close()

while 1:
    connection, address=serverSocket.accept()
print("Serveri eshte i lidhur ne:"+str(address))
    start_new_thread(clientthread,(connection,))

serverSocket.close()

