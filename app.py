import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to get PDF files from a folder
def get_pdfs(folder_path):
    return [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

# Function to load or create Excel file
def load_excel(excel_file):
    if os.path.exists(excel_file):
        return pd.read_excel(excel_file)
    else:
        df = pd.DataFrame(columns=["Book Name", "Completed"])
        df.to_excel(excel_file, index=False)
        return df

# Function to update the Excel file
def update_excel(df, excel_file):
    df.to_excel(excel_file, index=False)

# Function to mark a book as completed
def mark_completed():
    selected_book = pending_listbox.get(tk.ACTIVE)
    if selected_book:
        # Move the book to completed status in Excel
        df.loc[df["Book Name"] == selected_book, "Completed"] = "Yes"
        update_excel(df, excel_file)
        refresh_gui()
        messagebox.showinfo("Completed", f"'{selected_book}' marked as completed.")
    else:
        messagebox.showwarning("Selection Error", "Please select a book first.")

# Function to open the selected book (PDF)
def open_book():
    selected_book = pending_listbox.get(tk.ACTIVE)
    if selected_book:
        # Get the full path of the selected book
        book_path = os.path.join(folder_path, selected_book)
        os.startfile(book_path)  # Open the PDF file using the default reader
    else:
        messagebox.showwarning("Selection Error", "Please select a book first.")

# Function to refresh the GUI (listboxes and Excel)
def refresh_gui():
    # Clear the listboxes
    pending_listbox.delete(0, tk.END)
    completed_listbox.delete(0, tk.END)
    
    # Reload PDFs and Excel sheet
    pdf_files = get_pdfs(folder_path)
    
    for pdf in pdf_files:
        # Check if the book exists in the Excel sheet, if not add it
        if pdf not in df["Book Name"].values:
            df.loc[len(df)] = [pdf, "No"]
            update_excel(df, excel_file)

        # Add the book to the appropriate listbox (pending or completed)
        if df.loc[df["Book Name"] == pdf, "Completed"].values[0] == "Yes":
            completed_listbox.insert(tk.END, pdf)
        else:
            pending_listbox.insert(tk.END, pdf)

# Set up the folder and Excel file path
folder_path = r"D:/Books"  # Update this to your folder path
excel_file = r"D:/VSS/Library/books_list.xlsx"

# Load the Excel file
df = load_excel(excel_file)

# Set up the GUI window
window = tk.Tk()
window.title("PDF Book Manager")

# Adjust the window size and add padding
window.geometry("1900x800")  # Set a larger window size

# Create and grid the "Pending Books" label and listbox
pending_label = tk.Label(window, text="Pending Books", font=("Arial", 14, "bold"))
pending_label.grid(row=0, column=0, pady=15)

pending_listbox = tk.Listbox(window, height=15, width=80, font=("Arial", 12))
pending_listbox.grid(row=1, column=0, pady=10)

# Create and grid the "Completed Books" label and listbox
completed_label = tk.Label(window, text="Completed Books", font=("Arial", 14, "bold"))
completed_label.grid(row=0, column=1, pady=15)

completed_listbox = tk.Listbox(window, height=15, width=80, font=("Arial", 12))
completed_listbox.grid(row=1, column=1, pady=10)

# Create and grid the "Open" button
open_book_button = tk.Button(window, text="Open", command=open_book, font=("Arial", 12))
open_book_button.grid(row=2, column=0, pady=20)

# Create and grid the "Mark as Completed" button
completed_button = tk.Button(window, text="Mark as Completed", command=mark_completed, font=("Arial", 12))
completed_button.grid(row=2, column=1, pady=20)

# Refresh the GUI to load initial data
refresh_gui()

# Start the GUI event loop
window.mainloop()
