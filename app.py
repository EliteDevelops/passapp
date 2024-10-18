import tkinter as tk
from tkinter import messagebox

# Define the version
VERSION = "1.0"

# Define the password
PASSWORD = "magicpassword"

def show_password():
    # Show the password in a messagebox
    messagebox.showinfo("Password", f"The password is: {PASSWORD}")

# Create the main application window
root = tk.Tk()
root.title("Password App")
root.geometry("300x200")  # Set a fixed size
root.resizable(False, False)  # Make the window non-resizable

# Create a label with the version number
version_label = tk.Label(root, text=f"Version: {VERSION}", font=("Helvetica", 12))
version_label.pack(pady=10)

# Create a button to show the password
show_button = tk.Button(root, text="Show Password", command=show_password, font=("Helvetica", 14))
show_button.pack(pady=20)

# Start the application
root.mainloop()