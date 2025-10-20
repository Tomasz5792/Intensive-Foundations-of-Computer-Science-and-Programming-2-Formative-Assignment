import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Table Example")

# Create Treeview
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Insert data
data = [
    (1, "Alice", 28),
    (2, "Bob", 34),
    (3, "Charlie", 25),
    (1, "Alice", 28),
    (2, "Bob", 34),
    (3, "Charlie", 25),
    (1, "Alice", 28),
    (2, "Bob", 34),
    (3, "Charlie", 25),
]
for row in data:
    tree.insert("", "end", values=row)

# Add scrollbar
#scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
#tree.configure(yscroll=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
#scrollbar.pack(side="right", fill="y")

root.mainloop()
