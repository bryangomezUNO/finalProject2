import tkinter as tk
from logic2 import GradeManager

class GradesGUI:
    """Create and manage the GUI components for the grade management system."""
    def __init__(self, master: tk.Tk):
        """Initialize the GUI elements and bind them to the window."""
        self.master = master
        self.master.geometry('600x500')
        self.grade_manager = GradeManager()

        self.lbl_name = tk.Label(master, text="Student Name:")
        self.lbl_name.pack(fill=tk.X)
        self.entry_name = tk.Entry(master)
        self.entry_name.pack(fill=tk.X)

        self.lbl_attempts = tk.Label(master, text="No. of Attempts:")
        self.lbl_attempts.pack(fill=tk.X)
        self.entry_attempts = tk.Entry(master)
        self.entry_attempts.pack(fill=tk.X)

        self.attempts_button = tk.Button(master, text="Set Attempts", command=self.create_score_entries)
        self.attempts_button.pack(fill=tk.X)

        self.score_entries = []
        self.labels_scores = []

        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.pack(fill=tk.X)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

        self.submitted_label = tk.Label(master, text="")
        self.submitted_label.pack(side=tk.BOTTOM, pady=10)

    def create_score_entries(self):
        """Create score entry fields based on the number of attempts."""
        self.clear_score_entries()
        try:
            attempts = int(self.entry_attempts.get())
            if attempts > 4:
                self.error_label.config(text="Number of attempts cannot exceed 4.")
                return
            for i in range(attempts):
                label = tk.Label(self.master, text=f"Score {i + 1}:")
                label.pack(fill=tk.X)
                self.labels_scores.append(label)
                entry = tk.Entry(self.master)
                entry.pack(fill=tk.X)
                self.score_entries.append(entry)
        except ValueError:
            self.error_label.config(text="Please enter a valid number for attempts.")



    def submit(self):
        """Handle the submission of scores."""
        scores = [int(entry.get()) for entry in self.score_entries if entry.get().isdigit()]
        name = self.entry_name.get()
        final_grade = self.grade_manager.calculate_and_save_grade(name, scores)
        self.submitted_label.config(text=f"Final Grade: {final_grade}")

    def clear_score_entries(self):
        """Clear all score entry fields."""
        for label in self.labels_scores:
            label.destroy()
        for entry in self.score_entries:
            entry.destroy()
        self.score_entries = []
        self.labels_scores = []

def setup_gui(window: tk.Tk):
    """Setup the GUI for the window"""
    GradesGUI(window)

