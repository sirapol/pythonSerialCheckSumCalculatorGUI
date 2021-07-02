import tkinter as tk

windows = tk.Tk()

windows.geometry("500x500")               #   set windows size
windows.resizable(False,False)          #   fix size

T = tk.Text(windows, height=1, width=4)
T.pack()
T.insert(tk.END, "0000")

windows.mainloop()