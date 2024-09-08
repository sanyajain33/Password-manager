import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.passwords = {}

        self.site_label = tk.Label(master, text="Website/Service:")
        self.site_entry = tk.Entry(master)

        self.username_label = tk.Label(master, text="Username:")
        self.username_entry = tk.Entry(master)

        self.password_label = tk.Label(master, text="Password:")
        self.password_entry = tk.Entry(master, show="*")

        self.store_button = tk.Button(master, text="Store Password", command=self.store_password)
        self.retrieve_button = tk.Button(master, text="Retrieve Password", command=self.retrieve_password)

        # Grid layout
        self.site_label.grid(row=0, column=0, sticky=tk.E)
        self.site_entry.grid(row=0, column=1)
        self.username_label.grid(row=1, column=0, sticky=tk.E)
        self.username_entry.grid(row=1, column=1)
        self.password_label.grid(row=2, column=0, sticky=tk.E)
        self.password_entry.grid(row=2, column=1)
        self.store_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

    def store_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not site or not username or not password:
            messagebox.showwarning("Incomplete Information", "Please enter all fields.")
            return

        # Store the information in-memory
        self.passwords[(site, username)] = password

        messagebox.showinfo("Stored Password", f"Password for {site} stored successfully!")

        # Clear the entry fields
        self.site_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def retrieve_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()

        if not site or not username:
            messagebox.showwarning("Incomplete Information", "Please enter both site and username.")
            return

        password = self.passwords.get((site, username))

        if password:
            messagebox.showinfo("Retrieved Password", f"Password for {site}: {password}")
        else:
            messagebox.showwarning("Not Found", "No password found for the given site and username.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
