import os
import json

server_fifo = "/tmp/server_fifo"
client_fifo = "/tmp/client_fifo"

request_id = input("Podaj id: ")
request = {
    "id": int(request_id),
    "client_queue": client_fifo
}

if not os.path.exists(client_fifo):
    os.mkfifo(client_fifo)

with open(server_fifo, "w") as server_fifo_path:
    server_fifo_path.write(json.dumps(request))

with open(client_fifo, "r") as client_fifo_path:
    response = client_fifo_path.readline().strip()
    print(response)
    os.unlink(client_fifo)
