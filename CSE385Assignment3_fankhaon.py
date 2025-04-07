import tkinter as tk
from tkinter import ttk
import mysql.connector

#---------------------------------------------------------------------------------------#
# This function connects to my local SQL server and retrieves data as columns and rows
def fetch_city_data():
    # Driver Manager style connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="world"
    )
    
    # Retrieve data and store it as columns and rows
    cursor = conn.cursor() # connect with cursor
    cursor.execute("SELECT * FROM city") # taken from assignment description
    columns = [col[0] for col in cursor.description] # Column names
    rows = cursor.fetchall() # Data
    
    # Cleanup and return
    cursor.close()
    conn.close()
    return columns, rows

#---------------------------------------------------------------------------------------#
# This function takes in table rows and columns and makes them viewable in a window
def populateTable(columns, rows):
    tree["columns"] = columns
    tree["show"] = "headings"
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w", width=100)
    for row in rows:
        tree.insert("", "end", values=row)

#---------------------------------------------------------------------------------------#
# Main: 

# Create a window
root = tk.Tk()
root.title("Table Viewer")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add horizontal and vertical scrollbars to view data
x_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
y_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add frame to viewable window with elements
tree = ttk.Treeview(frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
tree.pack(fill=tk.BOTH, expand=True)

x_scrollbar.config(command=tree.xview)
y_scrollbar.config(command=tree.yview)

# Attempt to connect and populate table in window
try:
    columns, rows = fetch_city_data() # Connect
    populateTable(columns, rows) # Populate
except mysql.connector.Error as err:
    # Throw exception if no connection can be made.
    tk.messagebox.showerror("Coonection Error", str(err))

root.mainloop()
