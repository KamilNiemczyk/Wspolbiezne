import sysv_ipc
import time 
import os
import signal 

dictionary = {
    "czerwony": "red",
    "zielony": "green",
    "niebieski": "blue",
    "czarny": "black",
    "fioletowy" : "purple",
}

key_input_queue = 1111
key_output_queue = 2222

def delete_queues():
    try:
        input_queue = sysv_ipc.MessageQueue(key_input_queue)
        input_queue.remove()
    except sysv_ipc.ExistentialError:
        pass

    try:
        output_queue = sysv_ipc.MessageQueue(key_output_queue)
        output_queue.remove()
    except sysv_ipc.ExistentialError:
        pass

def signal_handler(sig, frame):
    delete_queues()
    sys.exit(0)

def main():
    input_queue = sysv_ipc.MessageQueue(key_input_queue, sysv_ipc.IPC_CREAT)
    output_queue = sysv_ipc.MessageQueue(key_output_queue, sysv_ipc.IPC_CREAT)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        message, pid = input_queue.receive()
        message = message.decode("utf-8")
        translated = dictionary.get(message, "Nie znam takiego słowa")
        output_queue.send(translated.encode("utf-8"), type=pid)
        
main()

        
