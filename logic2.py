import csv
import os

class GradeManager:
    """Manage the grading logic and CSV file operations for storing grades."""
    def __init__(self):
        """Initialize the GradeManager and ensure the CSV file is ready."""
        self.csv_file = 'grades.csv'
        self.initialize_csv()

    def initialize_csv(self):
        """Initialize the CSV file with the correct headers if not already present."""
        if not os.path.exists(self.csv_file) or os.stat(self.csv_file).st_size == 0:
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final (Average)'])

    def calculate_grade(self, scores: list) -> str:
        """Calculate the highest grade based on a list of scores."""
        if not scores:
            return 'F'
        average_score = sum(scores) / len(scores)
        if average_score >= 90:
            return 'A'
        elif average_score >= 80:
            return 'B'
        elif average_score >= 70:
            return 'C'
        elif average_score >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_and_save_grade(self, name: str, scores: list) -> str:
        """Calculate the final grade and save the results to a CSV file."""
        scores = (scores + [0]*4)[:4]
        valid_scores = [score for score in scores if score > 0]
        average = sum(valid_scores) / len(valid_scores) if valid_scores else 0
        final_grade = self.calculate_grade(valid_scores)
        grade_with_average = f"{final_grade} ({average:.2f})"
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name] + scores + [grade_with_average])
        return grade_with_average
