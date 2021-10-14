from tkinter import *
import algorithm

root = Tk()
root.title("Love Calculator")

# Vars
result = StringVar()
name = StringVar()
partner = StringVar()

# Frame
Label(root, text="Your name").grid(row=0, column=0)
Entry(root, textvariable=name, borderwidth=5).grid(row=0, column=1)
Label(root, text="Your partner's name").grid(row=1, column=0)
Entry(root, textvariable=partner, borderwidth=5).grid(row=1, column=1)
Label(root, text="      ").grid(row=2, column=0)
Button(root, text="Calculate", command=lambda: algorithm.algorithm(result, name.get(),partner.get())).grid(row=2, column=1)
Label(root, text="Status").grid(row=3, column=0)
Entry(root, textvariable=result, borderwidth=5).grid(row=3, column=1)

root.mainloop()
