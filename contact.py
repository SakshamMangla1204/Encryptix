import tkinter as tk
from tkinter import messagebox
import json


contacts = []


def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []


def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts()
        view_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone are required.")

def view_contacts():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    query = search_entry.get().lower()
    contacts_listbox.delete(0, tk.END)
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    for contact in results:
        contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}")

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            save_contacts()
            view_contacts()
            clear_entries()
            return
    messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts()
    view_contacts()
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Manager")


tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Address:").pack(pady=5)
address_entry = tk.Entry(root)
address_entry.pack(pady=5)


tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=5)


tk.Label(root, text="Search:").pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack(pady=5)


contacts_listbox = tk.Listbox(root, width=50, height=10)
contacts_listbox.pack(pady=10)


load_contacts()
view_contacts()

root.mainloop()
