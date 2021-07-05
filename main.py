from tkinter import *
#Create an instance of Tkinter frame
win= Tk()
win.geometry("500x500")             # fix windows size
win.resizable(False,False)

def callback(var):
   input = var1.get()
   print(input)

def callbackDropdown(event):
   print("user chenge : ",variable.get())


# define maxBytes
lst =[]
maxBytes = 10
for x in range(3,maxBytes):
   lst.append(x)

# create 
variable = StringVar(win)
variable.set(0) # default value
w = OptionMenu(win, variable, *lst,command = callbackDropdown).pack()
# var1 = StringVar()
# var1.trace("w", lambda name, index,mode, var=var1: callback(var))
# var2 = StringVar()
# var2.trace("w", lambda name, index,mode, var=var2: callback(var))

# #Create an Entry widget
# e1 = Entry(win, textvariable=var1)
# e1.pack()
# e2 = Entry(win, textvariable=var2)
# e2.pack()

# print("user select :",variable.get())
# win.mainloop()


# from tkinter import *
# import tkinter

# root = Tk()
# root.geometry("500x500")
# root.resizable(False,False)
# frame=Frame(root)
# Grid.rowconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 0, weight=1)
# frame.grid(row=0, column=0, sticky=N+S+E+W)
# grid=Frame(frame)
# grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
# Grid.rowconfigure(frame, 7, weight=1)
# Grid.columnconfigure(frame, 0, weight=1)

# active="red"
# default_color="white"

# def main(height=5,width=5):
#   for x in range(width):
#     for y in range(height):
#       btn = tkinter.Button(frame, bg=default_color)
#       btn.grid(column=x, row=y, sticky=N+S+E+W)
#       btn["command"] = lambda btn=btn: click(btn)

#   for x in range(width):
#     Grid.columnconfigure(frame, x, weight=1)

#   for y in range(height):
#     Grid.rowconfigure(frame, y, weight=1)

#    # tkinter.Text("heelo")

#   return frame

# def click(button):
#   if(button["bg"] == active):
#     button["bg"] = default_color
#   else:
#     button["bg"] = active

# w= main(10,10)
# tkinter.mainloop()