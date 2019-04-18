from socket import *
from sys import *
server = "localhost"
port = 12000

 print('UNIVERSITETI I PRISHTINES')
    print('HASAN PRISHTINA')
    print('Fakulteti i Inxhinierise Elektrike dhe Kompjuterike')
print("Per te zgjedhur sherbimin shkruani fjalet:")
print("IPADRESA, NUMRIIPORTIT, PRINTO, EMRIIKOMPJUTERIT, KOHA, BASHTINGLLORE, KONVERTO, FIBONNACI\n")

while True:
    kerkesa= var.upper()
    
    elif kerkesa== 'IPADRESA':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
        print('IP ADRESA e juaj eshte: ' + data)
    elif kerkesa == 'PRINTIMI':
        s.sendall(str.encode(kerkesa))
     zgjedhja = input('Shkruani nje fjali:')
        s.sendall(str.encode(zgjedhja))
         data=s.recv(128).decode('utf-8')
      print('Fjalia e dhene eshte:' +data)
      elif kerkesa=='BASHTINGELLORE':
        s.sendall(str.encode(kerkesa))
   Zgjedhja=input('Shtypni fjalin tuaj: ')
    s.sendall(str.encode(Zgjedhja))
        data=s.recv(128).decode('utf-8')
        print('Numri i bashtingelloreve ne fjaline e shtypur eshte: '+data)
    elif kerkesa=='EMRIIKOMPJUTERIT':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
     print('Emri juaj eshte: '+data)

        if kerkesa=='NUMRIIPORTIT':
        s.sendall(str.encode(kerkesa))

     emriportit= str(klientPort)
        s.sendall(str.encode(emriportit))
         data=s.recv(128).decode('utf-8')
        print('Porti juaj eshte: '+str(klientPort))
     elif kerkesa == 'KOHA':
        s.sendall(str.encode(kerkesa))
    data=s.recv(128).decode('utf-8')
        print(data)   
    elif kerkesa =='LOJA':
     s.sendall(str.encode(kerkesa))
     data=s.recv(128).decode('utf-8')
        print('Numrat random te gjeneruar jane:'+data)
    elif kerkesa == 'FIBONACCI':
        s.sendall(str.encode(kerkesa)) 
        numri= input('Jepni nje numer')
  s.sendall(str.encode(numri))

    data=s.recv(128).decode('utf-8')
        print('Fibonacci i numrit te dhene eshte ' +data)
    elif kerkesa == 'KONVERTIMI': 
        s.sendall(str.encode(kerkesa))
        print('Ju mund te beni keto konvertime: \nKilowattToHorsepower \nHorsepowerToKilowatt \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons')
     metoda= input('Zgjedhni nje opsion: ')
        s.sendall(str.encode(metoda))
          sasia = input('Jepni numrin qe doni te konvertoni')
        s.sendall(str.encode(sasia))
        data=s.recv(128).decode('utf-8')
        print('Madhesia e konvertuar: '+data)
    elif kerkesa=='1':
        break
    else:
        print('Ju lutem shenoni komanden e duhur')
    print()
s.close()




