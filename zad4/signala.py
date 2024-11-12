import os 
import signal 
import time 

server_fifo = "/tmp/server_fifo"

def send_signal(signal_number):
    if not os.path.exists(server_fifo):
        print("Server is not running")
        return
    with open(server_fifo, "w") as server_fifo_path:
        server_fifo_path.write(f"{signal_number}")


signal.signal(signal.SIGHUP, lambda signum, frame: send_signal(signum))
signal.signal(signal.SIGTERM, lambda signum, frame: send_signal(signum))
signal.signal(signal.SIGUSR1, lambda signum, frame: send_signal(signum))

def main():
    print("Signal Server is running")
    while True:
        inp = input("Enter signal number 1) SIGHUP 2) SIGTERM 3) SIGUSR1 4) Exit: ")
        if inp == "1":
            send_signal(signal.SIGHUP)
        elif inp == "2":
            send_signal(signal.SIGTERM)
        elif inp == "3":
            send_signal(signal.SIGUSR1)
        elif inp == "4":
            break
        else:
            print("Invalid signal number")

main()