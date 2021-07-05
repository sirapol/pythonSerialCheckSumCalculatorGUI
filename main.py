from tkinter import *

root =Tk()

# add widget

root.title("Serial Checksum Calculator")
root.option_add("*Font","consolas 12")
root.geometry("600x600")
root.resizable(False,False)


# define maxBytes
maxBytes = 10
# lst = [StringVar()]* (maxBytes+1)
lstEntry=[]
lstText = []
checkSum=StringVar()
checkSumWithData = StringVar()

def onClickCopy():
   root.clipboard_clear()
   root.clipboard_append(checkSumWithData.get())

def textChange():
   checkSumI=0
   checkSumD=""
   for a in lstText:
      checkSumI = checkSumI ^ int(a.get(),base=16)
      strbuf = "{:02x}".format(int(a.get(),base=16))
      checkSumD = checkSumD+strbuf
   checkSumD = checkSumD + str(hex(checkSumI)).lstrip("0x")
   checkSumD = "\\x"+checkSumD
   checkSumWithData.set(checkSumD)
   checkSum.set("0x{:02x}".format(checkSumI))
   print(checkSum.get())
   print("checksum : ",checkSum.get())

for x in range(0,maxBytes):
   Label(root,text=f'0x{"{:02x}".format(x)}').pack(side=TOP)
   lstText.append(StringVar())
   lstEntry.append(Entry(root,text="0x00",textvariable=lstText[x],width=4))  
   lstEntry[x].insert(END,"0x00")
   lstEntry[x].bind('<Return>',(lambda _:textChange()))
   lstEntry[x].pack(side=TOP)
   # Entry(root,textvariable=lst[x],width=4).bind('<Return>',(lambda _:callback(e))).pack()
   # print(lst[x])

# Label(root,text= "Data sizes : ").pack(side=LEFT)
# variable = StringVar(root)
# variable.set(0) # default value
# OptionMenu(root, variable, *lst).pack(side=LEFT)

e1 = Entry(root,textvariable=checkSumWithData,width=30)
e2 = Entry(root,textvariable=checkSum)
e1.config(state=DISABLED)
e2.config(state=DISABLED)
e1.pack()
e2.pack()

Button(root,text="Copy",command=onClickCopy).pack(side=BOTTOM)

root.mainloop()

