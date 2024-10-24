import time 
import os 

dane = "dane.txt"
wyniki = "wyniki.txt"

liczba = input("Enter a number: ")

with open(wyniki, "w") as f:
    pass
with open(dane, "w") as f:
        f.write(str(liczba))
with open(wyniki, "r") as f:
        while True:
            if os.path.getsize(wyniki) > 0:
                result = f.readline()
                print(result)
                break
            time.sleep(1)
