import time 
import os 

dane = "dane.txt"
wyniki = "wyniki.txt"

while True: 
    if os.path.getsize(dane) > 0:
        with open(dane, "r") as f:
            liczba = f.readline()
            liczba = int(liczba)
            wynik = liczba * 2
        with open(wyniki, "w") as f:
            f.write(str(wynik))
    time.sleep(1)
