import tkinter as tk
import subprocess


def launch_program():
    program_path = "C:\\Users\\LP226\\Desktop\\bbracing.lnk"  # Replace with the path to your .lnk file
    process = subprocess.Popen(program_path, shell=True)
    return process


launch_program()

