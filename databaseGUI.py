import tkinter as tk

window = tk.Tk()

window.title("Frank's Books")

label = tk.Label(window, text="Frank's Books")


tk.Label(window, text="Username").grid(row=0, column=0)
tk.Label(window, text="Password").grid(row=1, column=0)

entry1 = tk.Entry(window)
entry2 = tk.Entry(window)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


window.mainloop()