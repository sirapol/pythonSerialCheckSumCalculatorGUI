from tkinter import *

root = Tk()

# add widget

root.title("Serial Checksum Calculator")
root.option_add("*Font", "consolas 12")
# root.geometry("600x600")
# root.resizable(False, False)

# define nom
# lst = [StringVar()]* (10+1)
lst = []
for xxx in range(3, 10):
    lst.append(xxx)

print(lst)

lstEntry = []
lstText = []
checkSum = StringVar()
checkSumWithData = StringVar()


# click for test
def onClickTest():
    for widget in root.winfo_children():
        widget.destroy()


# click for copy
def onClickCopy():
    root.clipboard_clear()
    root.clipboard_append(checkSumWithData.get())


def textChange():
    checkSumI = 0
    checkSumD = ""
    for a in lstText:
        checkSumI = checkSumI ^ int(a.get(), base=16)
        strbuf = "{:02x}".format(int(a.get(), base=16))
        checkSumD = checkSumD+strbuf
    checkSumD = checkSumD + str(hex(checkSumI)).lstrip("0x")
    checkSumD = "\\x"+checkSumD
    checkSumWithData.set(checkSumD)
    checkSum.set("0x{:02x}".format(checkSumI))
    print(checkSum.get())
    print("checksum : ", checkSum.get())


def createWidget(nom):
    # lstEntry=[]
    # lstText = []
    # checkSum=StringVar()
    # checkSumWithData = StringVar()
    Label(root,text="Address").grid(row=1,column=0)
    Label(root,text="Hex").grid(row=1,column=1)
    for x in range(0, nom-1):
       
        Label(root, text=f'0x{"{:02x}".format(x)}',
              width=5).grid(row=x+2, column=0)
        lstText.append(StringVar())
        lstEntry.append(
            Entry(root, text="0x00", textvariable=lstText[x], width=6, justify=CENTER))
        lstEntry[x].insert(END, "0x00")
        lstEntry[x].bind('<Return>', (lambda _: textChange()))
        lstEntry[x].grid(row=x+2, column=1)

    e1 = Entry(root, textvariable=checkSumWithData, width=30, justify=CENTER)
    e2 = Entry(root, textvariable=checkSum, justify=CENTER)
    e1.config(state=DISABLED)
    e2.config(state=DISABLED)
    e1.grid(row=nom+1, columnspan=2)
    e2.grid(row=nom+2, columnspan=2)

    Button(root, text="Copy", command=onClickCopy,
           justify=CENTER).grid(row=nom+3, columnspan=2)
    Button(root, text="Close", command=clear,
           justify=CENTER).grid(row=nom+4, columnspan=2)


def selectArray(event):
    print(variable.get())
   #  onClickTest()
    createWidget(int(variable.get()))

def init():
   Label(root, text="Data sizes : ").grid(row=0, column=0)
   OptionMenu(root, variable, *lst, command=selectArray).grid(row=0, column=1)

def clear():
   exit()


# main
variable = StringVar(root)
variable.set(lst[0])  # default value
init()

root.mainloop()