import tkinter as tk

# Constants
window = tk.Tk()
WIDTH = 900

# Frames
about_frame = tk.Frame(master=window, width=WIDTH//3, height=600, bg="red")
details_frame = tk.Frame(master=window, width=(WIDTH//3)*2, bg="yellow")
data_frame = tk.Frame(master=window, width=(WIDTH//3)*2, bg="green")
about_frame.pack(fill=tk.Y, side="left")
details_frame.pack(fill=tk.Y, side="left")
data_frame.pack(fill=tk.Y, side="left")
data_frame.pack_forget()

# About Frame
about_frame.columnconfigure(1, minsize=300)
about_frame.rowconfigure([1,2,3,4,5], minsize=120)

title_lbl = tk.Label(master=about_frame, text="DocFiller", bg="red", fg="white", font=("TkDefaultFont", 34, 'bold'))
# title_lbl.pack(fill=tk.X, side="top")
title_lbl.grid(row=1, column=1)

about_lbl = tk.Label(master=about_frame, text="This application can work\nwith both singular values\nand bulk values using CSV.", bg="red", fg="white", font=("TkDefaultFont", 14, 'bold'))
# about_lbl.pack(fill=tk.X)
about_lbl.grid(row=3, column=1, padx=10)

csv_button = tk.Button(master=about_frame, text="Upload CSV", width=50, height=3, font=("TkDefaultFont", 10, 'bold'))
# csv_button.pack(fill=tk.X, side="bottom")
csv_button.grid(row=5, column=1)

credit_lbl = tk.Label(master=about_frame, text="Made by MNK(22AD073)", bg='red', fg='white')
credit_lbl.grid(row=6, column=1)

window.mainloop()