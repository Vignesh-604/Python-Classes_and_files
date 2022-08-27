# r = read only , w = writeable , a = append/add new text without modifying previous entries , r+ = read and writeable.

folder = open("Animals.txt", "r")

def Read():
    print(folder.readable())
    print(folder.readline())
    print(folder.readline())
    print(folder.readlines()[1])
    # print(Coolio.readlines()) -> Will print every item n the file.

def Loop():
    for animal in folder:
        print(animal)

Read()
folder.close()
