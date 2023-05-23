from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
#import matplotlib.pyplot as plt
def next_page():
    import main.py
    root.destroy()
    
root = tk.Tk()

# number_entry = tk.Entry(root)

# Add validation to the entry widget to ensure that only numbers are entered


root.background_image = ImageTk.PhotoImage(Image.open("D:\Harshal\main\wp8379331-desktop-stocks-wallpapers.png"))
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(relwidth=1, relheight=1)


title_label = tk.Label(root, text="New Budget", font=("Arial", 24), bg="turquoise", fg="black")

# Use pack() method to place the title label at the top of the window
title_label.pack(side='top', padx=5, pady=5)


# Create a frame for the date widgets
date_frame = tk.Frame(root)

# Create the start date label and date widget
start_date_label = tk.Label(date_frame, text="Start Date:", font="Helvetica 12", bg="aquamarine", fg="black")
start_date_widget = DateEntry(date_frame, width=18, background='aquamarine',
                              foreground='black', borderwidth=8)

# Create the end date label and date widget
end_date_label = tk.Label(date_frame, text="End Date:", font="Helvetica 12", bg="aquamarine", fg="black")
end_date_widget = DateEntry(date_frame, width=18, background='aquamarine',
                            foreground='black', borderwidth=8)

# Use pack() method to place the date widgets one below the other
start_date_label.pack(side='top', padx=5, pady=5)
start_date_widget.pack(side='top', padx=5, pady=5)
end_date_label.pack(side='top', padx=5, pady=5)
end_date_widget.pack(side='top', padx=5, pady=5)

# Pack the date frame
date_frame.pack(side='top', padx=10, pady=10)

# Create the label for income
income_label = tk.Label(root, text="Your Budget (In Rupees):", font="Helvetica 12", bg="aquamarine", fg="black")
income_label.pack(side='top', padx=5, pady=5)
# Create the entry box for income
income_entry = tk.Entry(root, width=20)
def validate_number(new_value):
    if new_value.isnumeric() or new_value == "":
        return True
    else:
        return False

vcmd = (root.register(validate_number), '%P')
income_entry.configure(validate="key", validatecommand=vcmd)

# Create the database connection and table
def connect_to_database():
    conn = sqlite3.connect('numbers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS numbers (number real)''')

# Add the function to store the number in the database


# Create the button to store the number
# store_button = tk.Button(root, text="Store", command=next_button)

# Pack the widgets into the window

def add():
    number = income_entry.get()
    conn = sqlite3.connect('numbers.db')
    c = conn.cursor()
    if number.isnumeric():
        c.execute("INSERT INTO numbers VALUES (?)", (float(number),))
        conn.commit()
        messagebox.showinfo("Income Added", "The income you entered has been added to the database succesfully!!")
    else:
        messagebox.showerror("Error", "Please enter a valid number")

# def print_everything():


add_button = tk.Button(padx=5, pady=5, text='Done', font=('Bold', 12), bg="aqua", fg="black", command=add)

# Use pack() method to place the label and entry box one below the other

income_entry.pack(side='top', padx=5, pady=5)
add_button.pack(anchor="center", fill="both", expand="True")
add_button.place(relx=0.476, rely=0.51)
#Create a next button

# button = tk.Button(padx=15, pady=5, text='Back', font=('Bold', 12), bg="aqua", fg="black")
# button.pack(side=tk.LEFT, padx=10)
# button.place(relx=0.426, rely=0.55)

next_button = tk.Button(padx=15, pady=5, text='Next', font=('Bold', 12), bg="aqua", fg="black",command=next_page)
next_button.pack(side=tk.LEFT, padx=10)
next_button.place(relx=0.472, rely=0.61)

#Income tax slab
root.geometry("1200x550")
#tk.maxsize("1200x550")
# Create an object of Style widget
# style = ttk.Style()
# style.theme_use('clam')

# # Add a Treeview widget
# tree = ttk.Treeview(root, column=("Index", "Slab", "Tax Slab Rates"), show='headings', height=5)
# tree.column("# 1", anchor="center")
# tree.heading("# 1", text="Index")
# tree.column("# 2", anchor="center")
# tree.heading("# 2", text="Slab")
# tree.column("# 3", anchor="center")
# tree.heading("# 3", text="Tax Slab Rates")
# tree.pack(padx=10, pady=10)


# # Insert the data in Treeview widget
# tree.insert('', 'end', text="1", values=('1) ', '₹3,00,000-₹5,00,000', '5%'))
# tree.insert('', 'end', text="1", values=('2) ','₹5,00,000-₹6,00,000', '10%'))
# tree.insert('', 'end', text="1", values=('3) ','₹6,00,000-₹7,50,000', '10%'))
# tree.insert('', 'end', text="1", values=('4) ','₹7,50,000-₹9,00,000', '15%'))

# tree.pack()

# # Load PNG image using PIL
# bg_image = Image.open("wp8379331-desktop-stocks-wallpapers.png")

# # Resize image to fit window size
# bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# # Convert image to PhotoImage object
# bg_image_tk = ImageTk.PhotoImage(bg_image)

# # Create Label widget with background image
# label = tk.Label(root, image=bg_image_tk)
# label.pack()

# # Set image as background
# label.configure(image=bg_image_tk)
# label.place(x=0, y=0, relwidth=1, relheight=1)



# Center the buttons in the window

# root.update_idletasks()
# window_width = root.winfo_width()
# button_width = button.winfo_width()
# button1_width = button1.winfo_width()
# x_offset = (window_width - button_width - button1_width - 10) / 2
# button.place(relx=x_offset/window_width, rely=0.36, anchor='center')
# button1.place(relx=(x_offset + button1_width + 10)/window_width, rely=0.36, anchor='center')
# expenses = {'Housing': 1200, 'Food': 500, 'Transportation': 200, 'Utilities': 300, 'Other': 250}

# # create a pie chart
# labels = list(expenses.keys())
# values = list(expenses.values())
# plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

# # add a title
# plt.title('Monthly Expenses')

# # display the chart
# plt.show()


root.mainloop()
