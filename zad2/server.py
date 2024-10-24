import time 
import os
import keyboard
while True:
    if os.path.getsize("bufor.txt") > 0:
        with open("bufor.txt", "r") as f:
            lines = f.readlines()
            output = lines[0].strip()
            next_line = "".join(lines[1:])
            with open(output, "w") as out:
                out.write(next_line)
                out.write("\n")
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
                    out.write(line + "\n")
                
                keyboard.unhook_all()
                os.unlink("lockfile")
                print("Zapisano")
        with open("bufor.txt", "w") as f:
            pass
    time.sleep(1)
