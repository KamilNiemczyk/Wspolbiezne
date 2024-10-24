import os  
import time  
import errno  
import keyboard

bufor = "bufor.txt"
while True:  
    try:
        fd = os.open("lockfile", os.O_CREAT|os.O_EXCL|os.O_RDWR)
        break  
    except OSError as e:  
        if e.errno != errno.EEXIST:  
            raise   
        print("Serwer zajety, proszę czekać")
        time.sleep(1)  
time.sleep(1)  

with open(bufor, "a") as f:
    file = input("Podaj nazwe pliku: ")
    f.write(file + ".txt\n")
    print("Podaj tekst (naciśnij ESC, aby zakończyć):")
    lines = []
    def on_esc(event):
        global esc_pressed
        esc_pressed = True
    esc_pressed = False
    keyboard.on_press_key("esc", on_esc)
    while not esc_pressed:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    for line in lines:
        f.write(line + "\n")
    
    keyboard.unhook_all()