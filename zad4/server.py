import time
import signal
import os
import json
import threading

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
        with open(client_queue, "w") as client_fifo_path:
            client_fifo_path.write(response)
    except Exception as e:
        print(str(e))


def handle_signals(signum, frame):
    if signum == signal.SIGHUP or signum == signal.SIGTERM:
        print("Ignoring signal {signum}")
    elif signum == signal.SIGUSR1:
        os.unlink(server_fifo)
        print("Exiting")
        exit(0)

def main():
    if not os.path.exists(server_fifo):
        os.mkfifo(server_fifo)
    signal.signal(signal.SIGHUP, handle_signals)
    signal.signal(signal.SIGTERM, handle_signals)
    signal.signal(signal.SIGUSR1, handle_signals)
    while True:
        with open(server_fifo, "r") as server_fifo_path:
            client_queue = server_fifo_path.readline().strip()
            try:
                request = json.loads(client_queue)
                requested_id = request["id"]
                client_queue = request["client_queue"]
                thread = threading.Thread(target=handle_client_req, args=(client_queue, requested_id))
                thread.start()
            except Exception as e:
                print(str(e))

main()

                

            