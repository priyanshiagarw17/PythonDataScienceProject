import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Analyzer:
    def __init__(self, file_path):

        self.df = pd.read_csv(file_path)

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

