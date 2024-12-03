# import struct
import socket

IP = "127.0.0.1"
port = 5001
bufSize = 1024

UDPServerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServerSocket.bind((IP,port))

print("Server UDP działa")

player1score = 0
player2score = 0

while True:
    gracz1_znak, gracz1_adres = UDPServerSocket.recvfrom(bufSize)
    gracz1_znak = gracz1_znak.decode()
    gracz2_znak, gracz2_adres = UDPServerSocket.recvfrom(bufSize)
    gracz2_znak = gracz2_znak.decode()
    if gracz1_znak == "koniec" or gracz2_znak == "koniec":
        if gracz1_znak == "koniec" and gracz2_znak == "koniec":
            player1score = 0
            player2score = 0
            print("Reset gry do stanu początkowego")
        elif gracz1_znak == "koniec":
            print("Gracz1 zakończył grę")
            UDPServerSocket.sendto("koniec".encode(), gracz2_adres)
            player1score = 0
            player2score = 0
        else:
            print("Gracz2 zakończył grę")
            UDPServerSocket.sendto("koniec".encode(), gracz1_adres)
            player1score = 0
            player2score = 0
    if gracz1_znak == gracz2_znak:
        print("Remis")
        UDPServerSocket.sendto(gracz1_znak.encode(), gracz2_adres)
        UDPServerSocket.sendto(gracz2_znak.encode(), gracz1_adres)
    if (gracz1_znak == "kamien" and gracz2_znak == "nozyce") or (gracz1_znak == "papier" and gracz2_znak == "kamien") or (gracz1_znak == "nozyce" and gracz2_znak == "papier"):
        print("Gracz1 wygrał")
        player1score += 1
        UDPServerSocket.sendto(gracz2_znak.encode(), gracz1_adres)
        UDPServerSocket.sendto(gracz1_znak.encode(), gracz2_adres)
    elif (gracz2_znak == "kamien" and gracz1_znak == "nozyce") or (gracz2_znak == "papier" and gracz1_znak == "kamien") or (gracz2_znak == "nozyce" and gracz1_znak == "papier"):
        print("Gracz2 wygrał")
        player2score += 1
        UDPServerSocket.sendto(gracz1_znak.encode(), gracz2_adres)
        UDPServerSocket.sendto(gracz2_znak.encode(), gracz1_adres)
    print("Gracz1: ", player1score, "Gracz2: ", player2score)
