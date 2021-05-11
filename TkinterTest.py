from tkinter import *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist.append(result)
    E1.delete(0, END)
def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text= "week 1", bg= "white", command = week1)
    B1Main = Button(column= 0, row = 2)
    B2Main = Button(text = "week 2", bg = "white")
    B2Main.grid(column= 0, row = 3)
    B3Main = Button(text = "week 3", bg = "white")
    B3Main.grid(column= 0, row = 4)
def week1():
    clearWindow()
    def results():
        results = E1.get()
        playlist.append(result)
        E1.delete(0, END)

    # This is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    # This is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    # This is a Button widget
    B1 = Button(text= " + ", bg = "white", command= results)
    B1.grid(column= 1, row= 2)

    B2 = Button(text= " print ",bg = "light blue", command= printList)
    B2. grid(column= 2, row=2)

    B3 = Button(text = "Export List", bg = "blue", command = exportList)
    B3.grid(column = 0, row= 3)

    Bexit = Button(text= "Clear Window", bg = "red", command = mainMenu)
    Bexit.grid(column = 1, row = 3)

def week2():
    clearWindow()
    B1Week2 = Button()
    L1Week2 = Label()
    L2Week2 = Label()
    L3Week2 = Label()
    E1Week2 = Entry()
    E2Week2 = Entry()






if __name__== "__main__":
    mainMenu()
top.mainloop()
 
