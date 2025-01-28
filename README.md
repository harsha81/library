Overview:
This program enables you to:

Load PDF files from a specified folder.
Track the completion status of each book (PDF).
Open the PDFs using the default reader.
Mark books as "completed" and update the status in an Excel file.
Key Features:
PDF File Management:

The program lists all PDF files in a specified folder and displays them in a pending books listbox.
Completion Tracking:

Each book has a "Completed" status stored in an Excel file.
If a book is marked as completed, it will move to the completed books listbox.
Excel Integration:

It loads and saves the completion status of books in an Excel sheet. If a book is not already listed, it adds it.
Book Opening:

You can click "Open" to open a selected book (PDF) using the default PDF reader.
Marking a Book as Completed:

You can mark a book as completed by selecting it and clicking "Mark as Completed", which updates the status in the Excel file and refreshes the UI.
Important Functions:
get_pdfs(folder_path):

Returns a list of PDF filenames in the specified folder.
load_excel(excel_file):

Loads the Excel file (or creates a new one if it doesn't exist) to track book names and completion status.
update_excel(df, excel_file):

Updates the Excel file with the current DataFrame, reflecting the status of the books.
mark_completed():

Marks the selected book as "Completed" in the Excel file and updates the UI.
open_book():

Opens the selected PDF using the default system PDF reader.
refresh_gui():

Refreshes the GUI by clearing the listboxes and reloading the books from the folder and Excel file.
GUI Layout:
The window has two main sections: Pending Books and Completed Books, each with a listbox.
Buttons:
Open: Opens the selected book (PDF).
Mark as Completed: Marks the selected book as completed and moves it to the completed list.
User Experience:
The program automatically checks for any new PDFs in the specified folder and adds them to the list of pending books if they are not already in the Excel sheet.
It keeps track of which books have been completed and displays them in a separate list.
