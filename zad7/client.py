import socket

serverAdresPort = ("127.0.0.1", 5001)
bufSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

score = 0

while True:
    znak = input("Podaj znak lub napisz koniec by zakonczyc: ")
    if znak == "koniec":
        UDPClientSocket.sendto(znak.encode(), serverAdresPort)
        print("Koniec gry")
        break
    UDPClientSocket.sendto(znak.encode(), serverAdresPort)
    data, _= UDPClientSocket.recvfrom(bufSize)
    data = data.decode()
    print("Przeciwnik wybral: ", data)
    if data == "koniec":
        print("Koniec gry")
        break
    if znak == data:
        print("Remis")
    elif (znak == "kamien" and data == "nozyce") or (znak == "papier" and data == "kamien") or (znak == "nozyce" and data == "papier"):
        print("Wygrales")
        score += 1
    else:
        print("Przegrales")
    print("Twoj wynik: ", score)
