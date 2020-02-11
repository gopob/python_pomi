from tkinter import filedialog
from tkinter import *

counter = {}
string = ''

def find_symbols(text):
    for word in text:
        counter[word] = counter.get(word, 0) + 1

    for key in counter:
        print(key + ' -> ' + str(counter[key]))

def file():
    file = filedialog.askopenfile(mode="r", initialdir="/", title="select file",
                                   filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    text = file.read()
    find_symbols(text)
    file.close()


root = Tk()
root.geometry("100x100")

b = Button(root, text="open text file", command = file)
b.pack()

root.mainloop()


