import sysv_ipc


key = 11
NULL_CHAR = '\0'

def pisz(mem, s):
    s += NULL_CHAR
    s = s.encode()
    mem.write(s)

def czytaj(mem):
    s = mem.read()
    s = s.decode()
    i = s.find(NULL_CHAR)
    if i != -1:
        s = s[:i]
    return s

def main():
    try:
        sem1 = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREX, 0o700, 0)
        sem2 = sysv_ipc.Semaphore(key + 1, sysv_ipc.IPC_CREX, 0o700, 0)
        mem = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREX)
        print("Player 1")
        player1 = True
    except sysv_ipc.ExistentialError:
        sem1 = sysv_ipc.Semaphore(key)
        sem2 = sysv_ipc.Semaphore(key+1)
        mem = sysv_ipc.SharedMemory(key)
        print("Player 2")
        player1 = False

    if player1:
        pisz(mem, "")

    score1 = 0
    score2 = 0

    for i in range(3):
        if player1:
            letter1 = input("Player 1(A, B, C): ").upper()
            pisz(mem, letter1)
            sem1.release()
            sem2.acquire()
            letter2 = czytaj(mem)
        else:
            sem1.acquire()
            letter1 = czytaj(mem)
            letter2 = input("Player 2(A, B, C): ").upper()
            pisz(mem, letter2)
            sem2.release()

        if letter1 == letter2:
            print("Player 2 wins!")
            score2 += 1
        else:
            print("Player 1 wins!")
            score1 += 1
        print("Player 1: ", score1, "Player 2: ", score2)

    if score1 > score2:
        print("Player 1 wins!")
    elif score1 < score2:
        print("Player 2 wins!")

    if player1:
        sem1.remove()
        sem2.remove()
        mem.remove()

if __name__ == "__main__":
    main()



