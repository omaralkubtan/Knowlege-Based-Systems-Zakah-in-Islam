from tkinter import *

class window:
    def __init__(self):
        self.root = Tk()
        self.var = IntVar()
        self.label = Label(self.root,text = "start",font=("Arial", 20),wraplength=600)
        # input
        # Text(root, bg, fg, bd, height, width, font, ..)
        self.text = Text(self.root,width=30,heigh=1,font=("Arial", 20))
        self.button = Button(self.root,text="Next",font=("Arial", 13),command=lambda: self.var.set(1))
        self.root.bind('<Return>',lambda e: self.var.set(1))
        self.label.pack(side = TOP)
        self.text.pack(side = TOP)
        self.button.pack(side = BOTTOM,padx=5,pady=5,ipadx=5,ipady=5)
        self.root.geometry("800x300")


    def input(self,string):
        self.text.pack(side = TOP)
        self.label["text"]=string
        self.text.delete('1.0', END)
        self.var.set(0);
        self.button.wait_variable(self.var)
        out = self.text.get("1.0",END)
        self.text.delete('1.0', END)
        out =  out.strip()
        return out
    
    def radio(self,string,options):
        self.text.pack_forget()
        self.label["text"] = string
        self.var.set(0)
        radios = []
        v = IntVar(self.root)
        for i in range(len(options)):
            radios.append(Radiobutton(self.root, text = options[i], variable = v,
                value = i, indicator = 0,
                background = "light blue",font=("Arial", 15)))
            radios[-1].pack(fill = X, ipady = 5,padx=50)
        
        self.button.wait_variable(self.var)
        out = options[v.get()]
        for r in radios:
            r.pack_forget()
        return out

            

        
