import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox as mbox
from tkinter.messagebox import showinfo
from degreeApp import DegreeApp

class UploadFile(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack(fill="both", expand=True) # assigns ttk.Frame to root application window
        self.filename = tk.StringVar()
        self.file_select_gui()


    # Handles the gui of the Upload File page
    def file_select_gui(self):
        self.style = ttk.Style(self)
        self.style.configure("BW.TLabel", font=("Roboto", 15), foreground="black", background="white")
        self.style.configure("GWSmall.TLabel", font=("Roboto", 12), foreground="Gray", background="white")
        self.style.configure("BWSmall.TLabel", font=("Roboto", 12), foreground="Blue", background="white")
        self.style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("picBkgd.TLabel", background="white")

        # Frame outline design
        self.frame = ttk.Frame(self, style="BlBord.TFrame")
        self.frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        self.frame.pack(fill=BOTH, expand=False, pady=20)  # frame padding

        # Decorative Image label and design
        self.doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
        self.lbl_image = ttk.Label(
            self.frame,
            image=self.doc_upload_photo,
            style="picBkgd.TLabel"
        )
        self.lbl_image.doc_upload_photo = self.doc_upload_photo  # Reference of Image to display image
        self.lbl_image.pack(side=TOP, fill=NONE, expand=5, padx=(20,0), pady=(20, 10))  # padding

        # Upload File text label and design
        lbl_upload = ttk.Label(self.frame, text="Upload File", style="BW.TLabel")
        lbl_upload.pack(fill=NONE, expand=False, padx=30, pady=10)  # text padding

        # subtext label and design
        lbl_upload = ttk.Label(self.frame, text="Click the button to select a file to upload: ",
                                    style="GWSmall.TLabel")
        lbl_upload.pack(fill=NONE, expand=False, padx=20, pady=10)  # text padding

        # Open Window's File Explorer button and design
        btn_file_browse = ttk.Button(
            self.frame,
            text="Browse Files",
            command=self.file_selection
        )
        btn_file_browse.pack(side=TOP, pady=20)  # button padding

        #file name (not file path) text label and design
        self.file_name = ttk.Label(self.frame, textvariable=self.filename, style="BWSmall.TLabel")
        self.file_name.pack(pady=10)


    # Opens file in read-only mode and returns if it's successful or not
    def open_file(self):
        if self.file_path:
            with open(self.file_path, "r") as f:
                return True
        else:
            return False


    # Gets file path of file selected from file explorer by the user and opens it
    def file_selection(self):
        pdf = "Adobe Acrobat Document"
        word_doc = "Microsoft Word Document"
        excel_sheet = "Microsoft Excel Worksheet"
        file_explorer = "\\"  # path start for windows
        file_err_msg = "File could not be opened or was not chosen."

        # opens Windows File Explorer and gets file path of the selected file
        self.file_path = filedialog.askopenfilename(initialdir=file_explorer, title="Open",
                                               filetypes=(("All Files", "*.*"), (pdf, "*.pdf*"),
                                                          (word_doc, "*.docx*"), (excel_sheet, "*.xlsx")))

        file_status = UploadFile.open_file(self)  # calls function to open file

        # Displays name of file that user selected and opened
        if file_status:
            file_name = "Uploaded File: " + os.path.basename(self.file_path)
            self.filename.set(file_name)
        else:
            mbox.showerror("Error", file_err_msg)  # failed opening file message box