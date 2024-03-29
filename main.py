import tkinter as tk
from tkinter import ttk
import subprocess


process_2py = None
process_SW3 = None

def run_2_py():
    global process_2py, process_SW3
    
    process_2py = subprocess.Popen(['python', 'game.py'])
    process_SW3 = subprocess.Popen(['python', 'SW3.py'])

def end_2_py():
    global process_2py, process_SW3
    if process_2py:
       
        process_2py.terminate()
        process_2py = None
    if process_SW3:
        
        process_SW3.terminate()
        process_SW3 = None

def create_gui():
    root = tk.Tk()
    root.title("Gesture Control Game By Gaurav And Kishan")
    root.iconbitmap("icon.ico")
    root.geometry("300x100")
    root.configure(bg="#825ad1")

    start_button = ttk.Button(root, text="Start Playing", command=run_2_py)
    start_button.pack()

    end_button = ttk.Button(root, text="End", command=end_2_py)
    end_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
