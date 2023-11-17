from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None
        self.pack()
        self.createWidget()

    def createWidget(self):
        menubar = Menu(root)

        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        menubar.add_cascade(label="File", menu=menuFile)
        menubar.add_cascade(label="Edit", menu=menuEdit)
        menubar.add_cascade(label="Help", menu=menuHelp)

        menuFile.add_command(label="New", accelerator="ctrl+n", command=self.newfile)
        menuFile.add_command(label="Open", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="Save", accelerator="ctrl+s", command=self.savefile)
        menuFile.add_command(label="Quit", accelerator="ctrl+q", command=self.exit)

        menuEdit.add_command(label="Clear", accelerator="ctrl+c", command=self.test)
        menuEdit.add_command(label="Withdraw", accelerator="ctrl+z", command=self.test)


        menuHelp.add_command(label="HelpDocuments", accelerator="ctrl+h", command=self.test)

        root["menu"] = menubar

        self.textpad = Text(root, width=50, height=50)
        self.textpad.pack()

        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="BackgroundColor", command=self.openAskColor)

        root.bind("<Button-3>", self.createContextMenu)

    def newfile(self):
        asksaveasfilename(title="Sava as", initialfile="No Name.txt",
                          filetypes=[("Documents","*.txt")],
                          defaultextension=".txt")
        self.savefile()

    def openfile(self):
        self.textpad.delete("1.0","end")
        with askopenfile(title="打开文本文件") as f:
            self.textpad.insert(INSERT,f.read())
            self.filename = f.name

    def savefile(self):
        with open(self.filename, "w") as f:
            c = self.textpad.get(1.0,END)
            f.write(c)

    def exit(self):
        root.quit()

    def test(self):
        pass

    def openAskColor(self):
        s1 = askcolor(color="red",title="Select background color")
        self.textpad.config(bg=s1[1])


    def createContextMenu(self, event):
         self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+100+200")
    app = Application(master=root)
    root.mainloop()