from tkinter.filedialog import *
from tkinter import *


#   窗口的宽度和高度
win_width = 900
win_height = 450
class Application(Frame):

    def __init__(self, master=None, bgcolor="#000000", fgcolor="#ff0000"):
        super().__init__(master)
        self.master = master
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.x = 0
        self.y = 0
        self.lastdraw = 0
        self.startDrawflag = False
        self.pack()
        self.createWidget()


    def createWidget(self):
        #   创建画图区域
        drawpad = Canvas(root, width=win_width, height=win_height, bg=self.bgcolor)
        drawpad.pack()

        #   创建按钮
        btn_start = Button(root,text="开始",name="start")
        btn_start.pack(side="left",padx="10")

        btn_pen = Button(root,text="画笔",name="pen")
        btn_pen.pack(side="left",padx="10")

        btn_rect = Button(root,text="矩形",name="rect")
        btn_rect.pack(side="left",padx="10")

        btn_clear = Button(root,text="清屏",name="clear")
        btn_clear.pack(side="left",padx="10")

        btn_erasor = Button(root,text="橡皮擦",name="easor")
        btn_erasor.pack(side="left",padx="10")

        btn_line = Button(root,text="直线",name="line")
        btn_line.pack(side="left",padx="10")

        btn_lineArrow = Button(root,text="箭头",name="lineArrow")
        btn_lineArrow.pack(side="left",padx="10")

        btn_color = Button(root,text="颜色",name="color")
        btn_color.pack(side="left",padx="10")

        btn_pen.bind_class("Button","<1>",self.eventManager)
        # self.drawpad.bind("<ButtonRelease-1>",self.stopDraw)

    def eventManager(self,event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawpad.bind("<B1-Motion>",self.myline)
        elif name =="lineArrow":
            self.drawpad.bind("<B1-Motion>",self.mylineArrow)
        elif name == "rect":
            self.drawpad.bind("<B1-Motion>", self.myrect)

    def startDraw(self,event):
        self.drawpad.delete(self.lastdraw)
        if not self.startDrawflag:
            self.startDrawflag = True
            self.x = event.x
            self.y = event.y
    def stopDraw(self,event):
        self.startDrawflag = False
        self.lastdraw = 0

    def myline(self,event):
        self.startDraw(event)
        self.lastdraw = self.drawpad.create_line(self.x,self.y,event.x,event.y,file=self.fgcolor)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastdraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,arrow=LAST,file=self.fgcolor)
    def myRect(self, event):
        self.startDraw(event)
        self.lastdraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)



if __name__ == "__main__":
    root = Tk()
    root.geometry("900x500+200+300")
    root.title("画图")
    app = Application(master=root)
    root.mainloop()
