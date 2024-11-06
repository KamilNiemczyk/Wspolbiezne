import multiprocessing
import sys
import re
def count_words(file, word, process_queue):
    count = 0
    processes = []
    with open(file, "r") as f:
        for line in f:
            if line.startswith('\input{'):
                file_name = line[7:-2]
                process = multiprocessing.Process(target=count_words, args=(file_name, word, process_queue))
                process.start()
                processes.append(process)
            else:
                line = re.sub(r'[^\w\s]', '', line.lower())
                count += line.split().count(word.lower())

    for process in processes:
        process.join()
    process_queue.put(count)

def main(file, word):
    result_queue = multiprocessing.Queue()
    parent = multiprocessing.Process(target=count_words, args=(file, word, result_queue))
    parent.start()
    parent.join()
    res = 0
    while not result_queue.empty():
        res += result_queue.get()
    print(f"Słowo {word} występuje {res} razy")

if __name__ == "__main__":
    file = sys.argv[1]
    word = sys.argv[2]
    main(file, word)

            


