# 'Write' deletes everything in the folder and writes the new input. Use "a" in the open file and then insert in line.

Folder = open("Animals.txt", "a")

def Write():                                               # This will Open the specified file and print in it.
    (Folder.write("Rat"))
    print(Folder.write("\nHen"))

def Write1():
    Folder_2 = open("Birbs.txt", "w")                      # This will open a text file and print the given in it.
    Folder_2.write("Hawk")

def Write2():                                              # This will make a HTML file and the given in it.
    HTML = open("insect.html", "w")
    HTML.write("<p> HTML Bugsies </p>")

Write()
Folder.close()
