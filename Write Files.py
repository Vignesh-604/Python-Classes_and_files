# Write deletes everything inm the folder and writes the new input. Use "a" in the open file and then insert in line.

Folder = open("Animals.txt", "a")

def Write():
    (Folder.write("Rat"))
    print(Folder.write("\nHen"))

def Write1():
    Folder_2 = open("Birbs.txt", "w")
    Folder_2.write("Hawk")

def Write2():
    HTML = open("insect.html", "w")
    HTML.write("<p> HTML Bugsies </p>")

Write()
Folder.close()
