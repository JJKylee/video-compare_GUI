# A Very Simple GUI for video-compare by JKyle
# v1 (2021-06-02)
# Free to modify and redistribute

# video-compare: https://github.com/pixop/video-compare
# video-compare_GUI.exe should be put in the same folder as video-compare.exe.

# To build an executable, run the following command line
# pyinstaller -w -F .\video-compare_GUI.py

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import subprocess

root = Tk()
root.title("A Very Simple GUI for video-compare by JKyle")
root.geometry("700x140")
root.resizable(True, True)

# function that centers the main window
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

center(root)

chk_DPIvar = IntVar() # variable for "Allow high DPI mode"

# File 1 path
def file1_path():
    path_selected = filedialog.askopenfilename(title="Select Video 1", filetypes=(("Video Files", "*.avi *.mkv *.mp4 *.mpg *.mpeg"), ("All Files", "*.*")))
    if path_selected == '': # if selection is canceled
        msgbox.showwarning("Confirm", "You canceled the selection of Video 1")
        return
    entry_file1.delete(0, END)
    entry_file1.insert(END, path_selected)

# File 2 path
def file2_path():
    path_selected = filedialog.askopenfilename(title="Select Video 2", filetypes=(("Video Files", "*.avi *.mkv *.mp4 *.mpg *.mpeg"), ("All Files", "*.*")))
    if path_selected == '': # if selection is canceled
        msgbox.showwarning("Confirm", "You canceled the selection of Video 2")
        return
    entry_file2.delete(0, END)
    entry_file2.insert(END, path_selected)

# Run video-compare
def video_compare():
    try:
        dpi_var = "-d"
        if chk_DPIvar ==0:
            dpi_var = ""
        # video-compare.exe should be in the same folder.
        subprocess.Popen(["video-compare.exe", dpi_var, str(entry_file1.get()), str(entry_file2.get())])
        
    except Exception as err: #Exception
        msgbox.showerror("Error", err)

# Start
def start(): 
    # Confirm file selections
    if len(entry_file1.get()) == 0:
        msgbox.showwarning("Warning", "Please select Video 1")
        return

    if len(entry_file2.get()) == 0:
        msgbox.showwarning("Warning", "Please select Video 2")
        return
    
    video_compare()

# FIle 1 frame
file1_frame = Frame(root)
file1_frame.pack(fill="x", padx=5, pady=3)

entry_file1 = Entry(file1_frame)
entry_file1.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

btn_file1 = Button(file1_frame, text="Video 1", width=10, command=file1_path)
btn_file1.pack(side="right", padx=5, pady=5)

# File 2 frame
file2_frame = Frame(root)
file2_frame.pack(fill="x", padx=5, pady=3)

entry_file2 = Entry(file2_frame)
entry_file2.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

btn_file2 = Button(file2_frame, text="Video 2", width=10, command=file2_path)
btn_file2.pack(side="right", padx=5, pady=5)

# Run frame
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=3)

chk_DPI = Checkbutton(run_frame, text="Allow high DPI mode", variable=chk_DPIvar)
chk_DPI.select() # high DPI selected by default
chk_DPI.pack(side="left", padx=5, pady=3)

btn_close = Button(run_frame, text="Quit", width=12, padx=5, pady=5, command=root.quit)
btn_close.pack(side="right", padx=5, pady=3)

btn_start = Button(run_frame, text="Start", width=12, padx=5, pady=5, command=start)
btn_start.pack(side="right", padx=5, pady=3)

root.mainloop()