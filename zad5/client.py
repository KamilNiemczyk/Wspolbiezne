import sysv_ipc
import os

def main():
    key_input_queue = 1111
    key_output_queue = 2222

    input_queue = sysv_ipc.MessageQueue(key_input_queue)
    output_queue = sysv_ipc.MessageQueue(key_output_queue)

    pid = os.getpid()
    print("Client with pid ", pid, " is running")
    while True:
        for i in range (5):
            word = "czerwony"
            input_queue.send(word.encode("utf-8"), type=pid)
            print(f"Sent message {word} to server")
            message, _ = output_queue.receive(type=pid)
            message = message.decode("utf-8")
            print(f"Received translation {message}")
        break

main()