import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

#---------------------------------------------------------------------------------------#
# This function establishes the connection to my local SQL database and retreives data.
def fetch_city_data(database):
    # 1. Establish connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database=database
    )
    # 2. Create cursor and read data
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM city")
    columns = [col[0] for col in cursor.description] # column heads
    rows = cursor.fetchall() # data
    # 3. Clean and return
    cursor.close()
    conn.close()
    return columns, rows

#---------------------------------------------------------------------------------------#
# This function populates the table displayed in the window.
def populateTable(columns, rows):
    # 1. Clear existing
    tree.delete(*tree.get_children())
    # 2. Populate
    tree["columns"] = columns
    tree["show"] = "headings"
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w", width=100)
        
    # 3. Makes it pretty by alternating colors to make data easier to read
    for index, row in enumerate(rows):
        tag = 'oddrow' if index % 2 else 'evenrow'
        tree.insert("", "end", values=row, tags=(tag,))
    tree.tag_configure('oddrow', background='lightgray')
    tree.tag_configure('evenrow', background='white')

#---------------------------------------------------------------------------------------#
# This function attempts to execute the program when the "Fetch" button is clicked.
def on_fetch_click():

    database = database_entry.get()
    try:
        columns, rows = fetch_city_data(database)
        populateTable(columns, rows)
    except mysql.connector.Error as e:
        messagebox.showerror("Connection Error", str(e))

#---------------------------------------------------------------------------------------#
# GUI Setup
root = tk.Tk()
root.title("Database Viewer")

# 1. Connection Input Section
    # Create frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.X)

    # Add Label for Database Name and followd by input field
tk.Label(input_frame, text="Database:").grid(row=0, column=0, sticky="e")
database_entry = tk.Entry(input_frame, width=20)

    # Use grid to format buttons
database_entry.grid(row=0, column=1, padx=5, pady=2)

    # DEMONSTRATION PURPOSE ONLY, COMMENT OUT LATER
database_entry.insert(0, "world") 

    # Fetch button
fetch_button = tk.Button(input_frame, text="Fetch", command=on_fetch_click, width=10)
fetch_button.grid(row=0, column=2, padx=(5, 20), pady=2)

    # Exit button
exit_button = tk.Button(input_frame, text="Exit", command=root.destroy, width=10)
exit_button.grid(row=0, column=3, padx=5, pady=2, sticky="e")

    # Make columns expand nicely if resized, but not input elements
input_frame.grid_columnconfigure(1, weight=0)
input_frame.grid_columnconfigure(3, weight=0)

# 2. Format Table Section
    # Create frame
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

    # Add and configure Scrollbars (ChatGPT used for formatting this... I'm rusty)
x_scrollbar = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
y_scrollbar = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
tree = ttk.Treeview(table_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
x_scrollbar.config(command=tree.xview)
y_scrollbar.config(command=tree.yview)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(fill=tk.BOTH, expand=True)

#---------------------------------------------------------------------------------------#
# Execute
root.mainloop()
