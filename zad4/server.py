import time
import os
import json
import threading
import signal
database = {
    1 : "Witam",
    2 : "Guten Tag",
    3 : "Hello",
    4 : "Bonjour",
    5 : "Ciao"
}

server_fifo = "/tmp/server_fifo"

def handle_client_req(client_queue, requested_id):
    time.sleep(5)
    try:
        if requested_id in database:
            response = database[requested_id] 
        else:
            response = "Nie ma"
        if os.path.exists(client_queue):
            with open(client_queue, "w") as client_fifo_path:
                client_fifo_path.write(response)
            os.unlink(client_queue)
    except Exception as e:
        print(str(e))

# def handle_signal(signal):
#     print(f"Signal {signal} received")
#     if signal == 1:
#         print("SIGHUP")
#     elif signal == 15:
#         print("SIGTERM")
#     elif signal == 10:
#         os.unlink(server_fifo)
#         print("Koniec dzialania seerwera")
#         exit(0)
#     else:
#         print("Nieznany sygnal")

# signal.signal(signal.SIGHUP, handle_signal(1))
# signal.signal(signal.SIGTERM, handle_signal(15))
# signal.signal(signal.SIGUSR1, handle_signal(10))


def main():
    if not os.path.exists(server_fifo):
        os.mkfifo(server_fifo)
    while True:
        with open(server_fifo, "r") as server_fifo_path:
            client_queue = server_fifo_path.readline().strip()
            try:
                request = json.loads(client_queue)
                if isinstance(request, dict):
                    requested_id = request["id"]
                    client_queue = request["client_queue"]
                    thread = threading.Thread(target=handle_client_req, args=(client_queue, requested_id))
                    thread.start()
                else:
                    if client_queue == "10":
                        os.unlink(server_fifo)
                        print("Koniec dzialania seerwera")
                        exit(0)
                    elif client_queue == "1":
                        print("SIGHUP")
                    elif client_queue == "15":
                        print("SIGTERM")

                    
            except Exception as e:
                print(str(e))

main()
##ps aux
##kill -1 PID