from socket import *
import platform 
from time import gmtime, strftime
import math
import ipaddress
import random 
port = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

try:
    serverSocket.bind(('',port))
    kondita = True
except:
    print("Vetem nje instance e serverit eshte e lejuar!")
    kondita = False
    pass

if kondita:
    print("FIEK UDP Serveri eshte i gatshem...\n")

while kondita:
    try:
        kerkesa, clientAddress = serverSocket.recvfrom(2048)
        kushti = kerkesa.decode("ASCII")
        socketName = socket.getsockname(serverSocket)
        print(str(clientAddress[0]) + ":" + str(clientAddress[1]) + " Komanda " + kushti.split(" ")[0] + " eshte pranuar...")
    except:
        continue
        pass

    if kushti == "IPADRESA":
        pergjigja =  "IP adresa e klientit eshte " + str(clientAddress[0])
    elif kushti == "NUMRIIPORTIT":
        pergjigja = "Klienti eshte duke perdorur portin " + str(socketName[1])
    elif kushti[0:6] == "BASHTINGLLORE":
        if kushti[0:7] == "BASHTINGLLORE ":
            string = kushti[7:len(kushti)]
            string = string.replace(" ", "")
            numri_bashtinglloreve = 0
            for i in string:
                if i == 'B' or i == 'C' or i == 'Q' or i == 'D' or i == 'F' or i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'P' or i == 'R' or i == 'S' or i == 'T' or i == 'V' or i == 'W'or i == 'X' or i == 'Z':
                     numri_bashtinglloreve += 1

            pergjigja = " Teksti derguar permban " + str(numri_bashtinglloreve) + " bashtingllore.  "
        else:
            pergjigja = "Formati: BASHTINGLLORE [teksti]";
    elif kushti[0:6] == "PRINTO":
        if kushti[0:7] == "PRINTO ":
            pergjigja = kushti[7:len(kushti)].lower().capitalize()
        else:
            pergjigja = "Formati: PRINTO [teksti]"

    elif kushti[0:3] == "AGE":
        if kushti[3:4] == " ":
            kushti = kushti.split(" ")

            num1 = str(kushti[1])
            num2 = str(kushti[2])
            num3 = int(kushti[3])
            num4 = int(kushti[4])

            if (num3 > num4):
                pergjigja = "ME I MADH ESHTE personi 1" 
            else:
                pergjigja = "Me i Madh eshte personi 2" 
        else:
            pergjigja = "EMRI1 EMRI2 [numri] [numri]"
            
            
    elif kushti == "EMRIIKOMPJUTERIT":
        try:
            h = platform.uname()[1]
            pergjigja = "Emri i klientit eshte " + h
        except:
            pergjigja = "Emri i klientit nuk dihet"
    elif kushti == "KOHA":
        pergjigja = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    elif kushti[0:6] == "NOTIMI":
        if kushti[6:7] == " ":
            string = kushti.split(" ")
            if string[1] == 'XHON' :
                pergjigja = "MATH:9\nENGLISH:10\nBIO:8\nGJEO:9\nFIZIKE:7\nTECH:10"
            elif string[1] == 'CARL':
                pergjigja = "MATH:8\nENGLISH:10\nBIO:10\nGJEO:8\nFIZIKE:10\nTECH:9"
            elif string[1] == 'TASHA':
                pergjigja = "MATH:7\nENGLISH:9\nBIO:9\nGJEO:7\nFIZIKE:8\nTECH:10"
            elif string[1] == 'TED':
                pergjigja = "MATH:10\nENGLISH:10\nBIO:8\nGJEO:10\nFIZIKE:9\nTECH:8"
            elif string[1] == 'BRITNY':
                pergjigja = "MATH:10\nENGLISH:9\nBIO:7\nGJEO:10\nFIZIKE:9\nTECH:10"
            elif string[1] == 'XHEJMI':
                pergjigja = "MATH:8\nENGLISH:10\nBIO:9\nGJEO:9\nFIZIKE:10\nTECH:9"
        else:
            pergjigja = "Formati: EMRI [XHON,CARL,TASHA,TED,BRITNY,XHEJMI]"
            
           
    elif kushti[0:8] == "KONVERTO":
        if kushti[8:9] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigja = str(float(string[2]) + 273.15)
            elif string[1] == '2':
                pergjigja = str(float(string[2]) * 1.8 + 32)
            elif string[1] == '3':
                pergjigja = str(float(string[2]) * 9 / 5 - 459.67)
            elif string[1] == '4':
                pergjigja = str(float(string[2]) - 273.15)
            elif string[1] == '5':
                pergjigja = str((float(string[2]) - 32) / 1.8)
            elif string[1] == '6':
                pergjigja = str(float(string[2]) + 459.67)
            else:
                pergjigja = "Shkruaj njerin nga opsionet "
        else:
            pergjigja = "Formati: KONVERTO [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigja += "\n 1:- CelsiusToKelvin"
            pergjigja += "\n 2:- CelsiusToFahrenheit" 
            pergjigja += "\n 3:- KelvinToFahrenheit" 
            pergjigja += "\n 4:- KelvinToCelsius"
            pergjigja += "\n 5:- FahrenheitToCelsius"
            pergjigja += "\n 6:- FahrenheitToKelvin"
         

    elif kushti[0:9] =="FIBONNACI":
        ardhshme = 1 
        paraprake = -1
        if kushti[9:10] == " ":
            for i in range(0, int(kushti[10:len(kushti)])):
                shuma = ardhshme + paraprake
                paraprake = ardhshme
                ardhshme = shuma
            pergjigja = str(shuma)
        else:
            pergjigja = "Formati: FIBONNACI [numri]";
    
    try:
        serverSocket.sendto(pergjigja.encode("ASCII"), clientAddress)
        print( clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(clientAddress[0] + ":" + str(clientAddress[1]) + " Pergjigja nuk mund te dergohet!")
        pass
