import time
try:
    my_file = open('file.txt')
    print("Reading the file:")
    print("-----------------")
    while True:
        line = my_file.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('\nYou stopped the reading of the file.')
finally:
    my_file.close()
    print('\nCleanup: Closed the file')
