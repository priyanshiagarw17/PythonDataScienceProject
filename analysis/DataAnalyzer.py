import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Analyzer:
    def __init__(self, file_path):

        self.df = pd.read_csv(file_path)
        print(self.df)

    def show_basic_info(self):

        print("First 5 rows:")
        print(self.df.head())
        print("\nLast 5 rows:")
        print(self.df.tail())
        print("\nDataset information:")
        print(self.df.info())
        print("\nSummary statistics:")
        print(self.df.describe())
        print("\nMissing values:")
        print(self.df.isnull().sum())

    def  rename(self):
        self.df.rename(columns={
            "Do you have Depression?": "Depression",
            "Do you have Anxiety?": "Anxiety",
            "What is your CGPA?": "CGPA",
            "marital status": "MaritalStatus",
            "Do you have Panic attack?" : "Panicattack",
            "Did you seek any specialist for a treatment?" : "Specialist",
            "Choose your gender" : "Gender",
            "What is your course?" : "Course",
            "Your current year of Study" : "Year"
        }, inplace=True)
        print(self.df)

