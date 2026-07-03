import tkinter as tk

window = tk.Tk()

## Title of window
window.title("Frank's Books")

## Banner for window
banner = tk.Label(
    window, text="Frank's Books",
    width = 10,
    height = 5    
)
banner.pack()

## Login text boxes
usernameLabel = tk.Label(text = "Username")
usernameEntry = tk.Entry(
    width = 20
)
usernameLabel.pack()
usernameEntry.pack()

passwordLabel = tk.Label(text = "Password")
passwordEntry = tk.Entry(
    width = 20
)
passwordLabel.pack()
passwordEntry.pack()

## Button to submit login credentials
submitButton = tk.Button (
    text = "Login",
    width = 5,
    height = 2
)
submitButton.pack()

window.mainloop()