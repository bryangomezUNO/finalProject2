import tkinter as tk
from gui2 import setup_gui

def main():
    """Initialize the main window and set up the GUI."""
    window = tk.Tk()
    window.title('Grades App')
    window.geometry('600x500')
    window.resizable(False, False)

    setup_gui(window)

    window.mainloop()

if __name__ == '__main__':
    main()

