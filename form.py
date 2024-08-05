import tkinter as tk
from tkinter import messagebox

# Function to be called when submit button is clicked
def submit_action():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name or not email or not age:
        messagebox.showwarning("Input Error", "All fields are required")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Input Error", "Age must be a number")
        return

    # Here you can add code to save the data or process it
    # For now, we'll just show a success message
    messagebox.showinfo("Success", f"Name: {name}\nEmail: {email}\nAge: {age}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entry fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=3, columnspan=2, pady=20)

# Run the application
root.mainloop()
