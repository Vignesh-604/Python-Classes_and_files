# r = read only , w = writeable , a = append/add new text without modifying previous entries , r+ = read and writeable.

folder = open("Animals.txt", "r")                  # open(file_name, file_mode)

def Read():
    print(folder.readable())                       # Checks if the file is the readable or not. Depends on the mode specified before.

    print(folder.readline())                       # Reads the first line. Once the line is printed, it won't be taken into consideration.

    print(folder.readline())                       # Reads the second line. Since these lines aren't considered, their indexes are also changed.

    print(folder.readlines()[1])                   # Since indexes are changed, it'll count the lines which aren't read. Can be used only once.

    #print(folder.readlines())                      # Will print every item in a list. If the code is wriiten before, this will print an empty list.

def Loop():                                         # Prints each item.
    for animal in folder:
        print(animal)

#Loop()
Read()
folder.close()
